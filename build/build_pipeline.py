"""
    From a terminal opened in the root project folder, call py -m build.build_pipeline
"""

from build.items_db.build_itemsdb import parseItems
from build.items_icons.build_itemicons import parseIcons

import logging
import os

from config import LOGS_DIR

# we want to stream all levels to the terminal, but only save select ones to file,
# those will be set for each file handler separately
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s:%(levelname)s:%(message)s'
)

# this is needed to give the same style to the WARNING messages
formatter = logging.Formatter(
    fmt = '%(asctime)s:%(levelname)s:%(message)s'
)

# --------------------
# ITEMSDB
# --------------------

if os.path.exists(LOGS_DIR / 'itemsdb_build.log'):
    os.remove(LOGS_DIR / 'itemsdb_build.log')

itemsdb_file_handler = logging.FileHandler(LOGS_DIR / 'itemsdb_build.log')

itemsdb_file_handler.setLevel(logging.INFO)
itemsdb_file_handler.setFormatter(formatter)

logger_itemsdb = logging.getLogger('build.items_db.build_itemsdb')
logger_itemsdb.addHandler(itemsdb_file_handler)

parseItems()

# --------------------
# ITEMS_ICONS
# --------------------

if os.path.exists(LOGS_DIR / 'icons_build.log'):
    os.remove(LOGS_DIR / 'icons_build.log')

icons_file_handler = logging.FileHandler(LOGS_DIR / 'icons_build.log')

icons_file_handler.setLevel(logging.INFO)
icons_file_handler.setFormatter(formatter)

logger_icons = logging.getLogger('build.item_icons.build_itemicons')
logger_icons.addHandler(icons_file_handler)

parseIcons()