"""
    From a terminal opened in the root project folder, call py -m build.build_pipeline
"""

from build.items_db.build_itemsdb import parseItems
from build.items_icons.build_itemicons import parseIcons

import logging
import os

from config import LOGS_DIR

# this ensures that INFO messages do end up streamed to the terminal
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s:%(levelname)s:%(message)s'
)

# this is needed to give the same style to the WARNING messages
formatter = logging.Formatter(
    fmt = '%(asctime)s:%(levelname)s:%(message)s'
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# --------------------
# ITEMSDB
# --------------------

if os.path.exists(LOGS_DIR / 'itemsdb_build.log'):
    os.remove(LOGS_DIR / 'itemsdb_build.log')

itemsdb_file_handler = logging.FileHandler(LOGS_DIR / 'itemsdb_build.log')

itemsdb_file_handler.setLevel(logging.WARNING)
itemsdb_file_handler.setFormatter(formatter)

logger_itemsdb = logging.getLogger('build.items_db.build_itemsdb')
logger_itemsdb.addHandler(itemsdb_file_handler)
logger_itemsdb.addHandler(console_handler)

parseItems()

# --------------------
# ITEMS_ICONS
# --------------------

if os.path.exists(LOGS_DIR / 'icons_build.log'):
    os.remove(LOGS_DIR / 'icons_build.log')

icons_file_handler = logging.FileHandler(LOGS_DIR / 'icons_build.log')

icons_file_handler.setLevel(logging.WARNING)
icons_file_handler.setFormatter(formatter)

logger_icons = logging.getLogger('build.item_icons.build_itemicons')
logger_icons.addHandler(icons_file_handler)
logger_icons.addHandler(console_handler)

parseIcons()