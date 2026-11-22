"""
    Item icons live in the lotro-items-db XML file as references to
    the components of the final image, e.g. 1090529611-1090519043-1090529613-1090529612
    where this follows the order from left to right:
    item-specific icon -> rarity-specific background -> black shadow  -> blue glow

    Each component is available separately at https://github.com/LotroCompanion/lotro-icons

    We use pillow to combine them as they are PNGs. Three specific icons are impossible
    to combine because some alpha channels are not recognized properly. They can be done
    manually but I haven't bothered.
"""

from PIL import Image, ImageFile
import urllib.request
import os
import logging
import sqlite3

from config import SRC_DIR, DATA_DIR, LOGS_DIR

logger = logging.getLogger(__name__)

raw_link = 'https://raw.githubusercontent.com/LotroCompanion/lotro-icons/refs/heads/master/items/'

IMGS_FINAL = DATA_DIR / 'final-imgs'
IMGS_INTERM = SRC_DIR  / 'intermediate-imgs'

logs_filepath = LOGS_DIR / 'icons_build.log'

def retrieveIconFile(uniqueID:str) -> ImageFile.ImageFile|None:
    """
        Pillow can read either a physical file or a byte stream, ergo
        we need to download the icon first before loading it into pillow.

        If the image file already exists because it was used by a previously processed file,
        we use that copy instead of downloading another - nevermind that downloading is quick.
    """
    try:
        img = Image.open(IMGS_INTERM / (uniqueID + '.png'))
    except FileNotFoundError:
        urllib.request.urlretrieve(
            # source
            raw_link + uniqueID + '.png',
            # destination - not temporary!
            IMGS_INTERM / (uniqueID + '.png')
        )
        img = Image.open(IMGS_INTERM / (uniqueID + '.png'))
    except Exception as e:
        logger.warning(f'{uniqueID} - failed to download image. Error message: {e}')
        img = None
    return img

def parseIcons():
    """
        Process the item icon reference by layering the components on top of each other.

        In case of errors, saves a log of failed images.

        Does not check the output for correctness - e.g. whether the glow is on top of the item-specific icon.
    """

    with sqlite3.connect(DATA_DIR / 'lotro-csp.db') as conn:
        crsr = conn.cursor()
        icons = crsr.execute(
            """
                select distinct icon
                from items
            """
        ).fetchall()
        icons:list[str] = [icon[0] for icon in icons]

    for idx, icon in enumerate(icons):

        logger.info(f'Processing image {idx} / {len(icons)}')

        # if a previously processed item uses the same icon, no need to repeat
        if os.path.isfile(IMGS_FINAL / (icon + '.png')):
            continue

        # from left to right, they are always in this order even if a shadow or glow is missing:
        # item-specific icon -> rarity-specific background -> black shadow  -> blue glow
        imgs_refs = icon.split('-')

        # we always start from the rarity-specific background...
        base_img = retrieveIconFile(imgs_refs.pop(1))

        # download failed for some reason
        if base_img is None:
            continue

        # ... then from right to left...
        imgs_refs.reverse()

        # ... start layering on top of it
        try:
            for img_ref in imgs_refs:
                add_on_top = retrieveIconFile(img_ref)
                base_img.paste(add_on_top, (0, 0), add_on_top)
            base_img.save(IMGS_FINAL /  (icon + '.png'))
        except Exception as e:
            logger.warning(f'#{idx} - {icon} - failed to combine image components with error message: {e}')
            continue

if __name__ == "__main__":
    parseIcons()