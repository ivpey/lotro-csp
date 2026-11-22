from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

# final output of the build steps:
#   - the sqlite database
#   - item images
DATA_DIR = PROJECT_ROOT / 'data'

# logs of the build steps:
#   - for items: name and why it was not processed and inserted in sqlite
#   - for icons: images which failed to be combined
LOGS_DIR = PROJECT_ROOT / 'logs'

# the build scripts themselves
BUILD_SCRIPTS_ITEMS_DIR = PROJECT_ROOT / 'build/items_db'
BUILD_SCRIPTS_ICONS_DIR = PROJECT_ROOT / 'build/items_icons'

# source files - XML and component images
SRC_DIR = PROJECT_ROOT / 'src'