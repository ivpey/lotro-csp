"""
    From a terminal opened in the root project folder, call py -m build.build_pipeline
"""

from build.items_db.build_itemsdb import parseItems
from build.items_icons.build_itemicons import parseIcons

import logging
import os

from config import LOGS_DIR

import argparse

parser = argparse.ArgumentParser(description = "split the build step into parts")
parser.add_argument("--items", action = 'store_true')
parser.add_argument("--items-count", type = int, default = None)
parser.add_argument("--icons", action = 'store_true')
cli_args = parser.parse_args()

# all levels go to the terminal
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s:%(levelname)s:%(message)s'
)

# turning off the following annoying messages:
# DEBUG:Starting new HTTPS connection (1)
# and
# DEBUG:STREAM b'IHDR'
logging.getLogger('urllib3.connectionpool').setLevel(logging.INFO)
logging.getLogger('PIL.PngImagePlugin').setLevel(logging.INFO)

# this is needed to give the same style to the WARNING messages
formatter = logging.Formatter(
    fmt = '%(asctime)s:%(levelname)s:%(message)s'
)

# --------------------
# ITEMSDB
# --------------------

if cli_args.items is True:

    print('Executing itemsdb step...')

    if os.path.exists(LOGS_DIR / 'itemsdb_build.log'):
        os.remove(LOGS_DIR / 'itemsdb_build.log')

    itemsdb_file_handler = logging.FileHandler(LOGS_DIR / 'itemsdb_build.log')

    itemsdb_file_handler.setLevel(logging.INFO)
    itemsdb_file_handler.setFormatter(formatter)

    logger_itemsdb = logging.getLogger('build.items_db.build_itemsdb')
    logger_itemsdb.addHandler(itemsdb_file_handler)

    parseItems(count = cli_args.items_count)

# --------------------
# ITEMS_ICONS
# --------------------

if cli_args.icons is True:

    print('Executing icons step...')

    if os.path.exists(LOGS_DIR / 'icons_build.log'):
        os.remove(LOGS_DIR / 'icons_build.log')

    icons_file_handler = logging.FileHandler(LOGS_DIR / 'icons_build.log')

    icons_file_handler.setLevel(logging.INFO)
    icons_file_handler.setFormatter(formatter)

    logger_icons = logging.getLogger('build.items_icons.build_itemicons')
    logger_icons.addHandler(icons_file_handler)

    parseIcons()

print(f'Processed the following: ITEMS = {cli_args.items} // ICONS = {cli_args.icons}')