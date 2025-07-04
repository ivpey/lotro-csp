A simple gear planner for the MMORPG Lord of the Rings Online, pulling item data from the Lotro Wiki and saving the gear config in the browser's local storage.

### Known issues:
- Gear with scaling stats (e.g. from Epic Battles) is displayed on the Wiki with stat ranges instead of a unique value per stat. The item will be loaded in the respective slot but it will not be included in the stat sheet calculations.
- The app cannot handle Legacy of Morgoth slot-specific essences. Regular essences are limited to single-stat ones.