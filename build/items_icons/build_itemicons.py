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

from PIL import Image
import requests
from requests.exceptions import HTTPError
import logging
import sqlite3
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor

from config import DATA_DIR

logger = logging.getLogger(__name__)

IMGS_FINAL = DATA_DIR / 'final-imgs'

def retrieveIconFile(icon: tuple[int, str]) -> Image.Image | None:
    """
        Pillow can read either a physical file or a byte stream. The images are small (~2KB each)
        so they can be stored in memory, there is no need to constantly write and read from disk.

        Args:
            icon: tuple[int, str] - the output of enumerate() so we can log the index of the currently processed image
    """
    
    raw_link = f'https://raw.githubusercontent.com/LotroCompanion/lotro-icons/refs/heads/master/items/{icon[1]}.png'
    
    logger.debug(f'Downloading image #{icon[0]}')

    response = requests.get(raw_link)
    try:
        response.raise_for_status()
    except HTTPError as e:
         logger.warning(f'{icon[1]} - retrieve failed with message: {e}')
         return None

    return Image.open(BytesIO(response.content))

def parseIcons():
    """
        Process the item icon reference by layering the components on top of each other.

        In case of errors, saves a log of failed images.

        Does not check the output for correctness - e.g. whether the glow is on top of the item-specific icon.
    """

    logger.info('Started processing icons')

    with sqlite3.connect(DATA_DIR / 'lotro-csp.db') as conn:
        # offloading to sqlite the transformation tuple -> list
        conn.row_factory = lambda cursor, row: row[0]
        # e.g. 1090519726-1090519044-1090519727-1090623637
        unique_full_icons: list[str] = conn.cursor().execute(
            """
                select distinct icon
                from items
            """
        ).fetchall()

    # breaking down full images (e.g. 1090519726-1090519044-1090519727-1090623637)
    # into their individual components, and deduplicating by transforming to a set first
    unique_single_icons = list(set([icon_part for icon in unique_full_icons for icon_part in icon.split('-')]))

    with ThreadPoolExecutor(max_workers = 10) as executor:
        # calling a list resolves all of the promises into their output objects
        resolved_img_futures = list(executor.map(retrieveIconFile, enumerate(unique_single_icons)))

    # since we are keeping all images in memory, we need a mapping between their ID and the PIL object
    downloaded_images = {
         str(t[0]): t[1] for t in list(zip(unique_single_icons, resolved_img_futures))
    }

    for idx, full_icon in enumerate(unique_full_icons):

        logger.debug(f'Combining image {idx} / {len(unique_full_icons)}')

        # from left to right, they are always in this order even if a shadow or glow is missing:
        # item-specific icon -> rarity-specific background -> black shadow  -> blue glow
        img_components = full_icon.split('-')

        # the first layer is always the rarity-specific background in 2nd position
        #
        # we need .copy() to get around the lazy loading behavior of Image.open()
        # which would mix images in our case and would overlay an image component
        # over an entire previously processed image
        base_img: Image.Image = downloaded_images[img_components.pop(1)].copy()

        # if download has failed for some reason, it was already logged
        if base_img is None:
            continue

        # the rest of the components will be stacked starting from the rightmost one and going left
        img_components.reverse()

        try:
            for component in img_components:
                base_img.paste(downloaded_images[component], (0, 0), downloaded_images[component])
            base_img.save(IMGS_FINAL /  (full_icon + '.png'))
        except Exception as e:
            logger.warning(f'{full_icon} - failed to combine image components with error message: {e}')
            continue

    logger.info('Finished processing icons')

if __name__ == "__main__":
    parseIcons()