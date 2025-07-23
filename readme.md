A simple gear planner for the [MMORPG Lord of the Rings Online](https://lotro.com/), pulling item data from the [Lotro Wiki](https://lotro-wiki.com/) and saving the gear config in the browser's local storage or as a convenient export string.

Live demo available at https://lotro-csp.onrender.com/

### Known issues:
- Gear with scaling stats (e.g. from Epic Battles) is displayed on the Wiki with stat ranges instead of a unique value per stat. The item will be loaded in the respective slot but it will not be included in the stat sheet calculations.
- The app cannot handle Legacy of Morgoth slot-specific essences. Regular essences are limited to single-stat ones.

Border images and the CSS style to use them seen at [Giseldah](https://giseldah.github.io/).