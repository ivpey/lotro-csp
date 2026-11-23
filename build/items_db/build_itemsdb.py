"""
    In the very first version of this project, the Lotro Wiki was used as the source for item data,
    and its API was queried on an item-by-item basis, it wasn't scraped in bulk.

    After they introduced Cloudflare, this access stopped working and I had to find an alternative source.

    A comprehensive item database is maintained over at https://github.com/LotroCompanion/lotro-items-db
    but the XML format needs to be transformed into something more appropriate for quick lookups like JSON or sqlite.

    I went for sqlite, and this is the build step.
"""

import sqlite3
import xml.etree.ElementTree as ET
import json
import numpy as np
import unicodedata
import logging

from build.items_db.db_setup import setup_db
from build.items_db.db_transforms import parse_essence_slot, parse_slot, parse_type
from stat_names_map import stat_names_map

from config import SRC_DIR

logger = logging.getLogger(__name__)

# comes from https://github.com/LotroCompanion/lotro-items-db
items:ET.Element = ET.parse(SRC_DIR / 'items.xml').getroot()
# comes from https://github.com/LotroCompanion/lotro-data/tree/master/lore
progressions:ET.Element = ET.parse(SRC_DIR / 'progressions.xml').getroot()

def parseItems(count: int | None = None):
    
    db_loc = setup_db('lotro-csp.db')
    db_conn = sqlite3.connect(db_loc)
    crsr = db_conn.cursor()

    logger.info('Started processing items.')

    # according to the documentation https://docs.python.org/3/library/xml.etree.elementtree.html
    # we take the root element and start iterating over its children.
    # we can discover the structure as
    # for unknown in root.iter():
    # print(unknown, unknown.attrib)
    # and repeating this for as long as there are levels.
    # this way we find that item has a stats element with children stat containing the name of the stat and its progressionID
    for idx, item in enumerate(items.iter('item')):

        if count is not None:
            if idx >= count:
                break

        logger.debug(f'Processing item {idx} / {len(items)}')

        c = item.get('category')
        s = item.get('slot')

        # cosmetics do not have any stats and we do not want to process them;
        # an item will always have a "stats" element which can contain 0 or more children with tag 'stat'
        #
        # similarly, legendary items do not have any stats of their own either
        #
        # grey/yellow items from the very early game also fall within this category
        if len(item.findall('stats')[0].findall('stat')) == 0:
            logger.warning(f'{item.get('key')} - {item.get('name')} - skipping due to no stats.')
            continue

        # lootbox/embers gear has category = ITEM and admissible slots;
        # however, category = ITEM includes also mounts, recipes, housing decorations, traceries, etc. which do not have slot,
        # and anything without a slot does not meet the requirements
        if (c not in ['ARMOUR', 'WEAPON', 'ESSENCE']) and not (
            c == 'ITEM' and s in [
                'EAR', 'NECK', 'WRIST', 'FINGER', 'POCKET',
                'HEAD', 'SHOULDER', 'BACK', 'CHEST', 'HAND', 'LEGS', 'FEET',
                'MAIN_HAND', 'OFF_HAND', 'RANGED_ITEM', 'CLASS_SLOT'
            ]
        ):
            logger.warning(f'{item.get('key')} - {item.get('name')} - inadmissible item.')
            continue        

        item_dict = {}

        # includes diacritics
        item_dict['display_name'] = item.get('name')
        item_dict['unique_id'] = item.get('key')
        item_dict['icon'] = item.get('icon')

        item_dict['slot'] = parse_slot(item)
                

        item_dict['quality'] = item.get('quality')
        item_dict['level'] = int(item.get('level'))

        item_dict['type'] = parse_type(item)

        item_dict['essence_slots'] = parse_essence_slot(item.get('slots'))

        item_dict['stats'], item_dict['progression_ids'] = parseStats(item, db_conn)

        if len(item_dict['stats']) == 0:
            logger.warning(f'{item.get('key')} - {item.get('name')} - no stats were processed.')
            continue
    
        if len(item_dict['progression_ids']) == 0:
            logger.warning(f'{item.get('key')} - {item.get('name')} - no progressionIDs were processed.')
            continue
    
        with db_conn:
            crsr.execute(
                """
                INSERT INTO items
                VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    # id
                    item_dict['unique_id'],
                    # name
                    item_dict['display_name'],
                    # name_normalized
                    ''.join(c for c in unicodedata.normalize('NFD', item_dict['display_name']) if unicodedata.category(c) != 'Mn'),
                    # icon
                    item_dict['icon'],
                    # slot
                    item_dict['slot'],
                    # quality
                    item_dict['quality'],
                    # base_level
                    item_dict['level'],
                    # type
                    item_dict['type'],
                    # stats_at_base_level
                    json.dumps(item_dict['stats']),
                    # progression_ids
                    json.dumps(item_dict['progression_ids']),
                    # essence_slots
                    json.dumps(item_dict['essence_slots'])
                )
            )

    logger.info('Finished processing items.')

def parseStats(
    item,
    db_conn:sqlite3.Connection,
    stats_to_process:list = [v['itemsdb'] for k, v in stat_names_map.items()]
) -> tuple[dict, dict]:
    
    stats_dict = {}
    progressions_dict = {}

    for stat in item.iter('stat'):
        # e.g. Lucky Horseshoe passes all the filters for processing but has
        # no progressionID associated with its only stat, Fate - instead it has a constant
        #
        # sometimes scaling is None because it is actually "ranged" - e.g. Greater Dextrous Boots of Finesse
        # and other scalable items for which one progression is applied between lvls 10-50 and another after lvl 50
        if stat.get('scaling') is None:
            logger.warning(f'{item.get('key')} - {item.get('name')} - no progressionID available for {stat.get('name')}.')
            continue

        idb_stat_name = stat.get('name')

        # we are only interested in parsing stats which we can process and display,
        # i.e. we skip Skill_AreaEffect_Damage, Skill_OverTime_Damage, etc. percentage modifiers
        if idb_stat_name in stats_to_process:

            # this is the best time to convert the stat names to the uniform style that we want
            mapped_stat_name = [map['calcstat'] for stat_display_name, map in stat_names_map.items() if map['itemsdb'] == idb_stat_name][0]

            points = []
            try:
                for progr in progressions:
                    if progr.get('identifier') == stat.get('scaling'):
                        for pt in progr.iter('point'):
                            points.append(
                                tuple([
                                    float(pt.get('x')),
                                    float(pt.get('y'))
                                ])
                            )
            except:
                stats_dict[mapped_stat_name] = '???'
                continue
            
            xs, ys = zip(*points)

            interpolated_stat = int(round(np.interp(int(item.get('level')), xs, ys), 0))

            stats_dict[mapped_stat_name] = interpolated_stat
            progressions_dict[mapped_stat_name] = int(stat.get('scaling'))

            # try-except is the lazy way to check if the progression already exists
            # since the ID is a primary key
            try:
                with db_conn:
                    crsr = db_conn.cursor()
                    crsr.execute(
                        """
                        INSERT INTO progressions
                        VALUES
                        (?, ?)
                        """,
                        (int(stat.get('scaling')), json.dumps(points))
                    )
            except sqlite3.IntegrityError: # in case progression ID already exists
                pass
            except Exception as e:
                raise e

    return stats_dict, progressions_dict

if __name__ == '__main__':
    parseItems()