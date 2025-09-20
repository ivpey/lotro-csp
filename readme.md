A simple gear planner for the [MMORPG Lord of the Rings Online](https://lotro.com/), pulling item data from the [Lotro Wiki](https://lotro-wiki.com/) and saving the gear config in the browser's LocalStorage or as a convenient export string.

Live demo available at https://lotro-csp.onrender.com/

### How to use:
- Item names can be copied into the app from in-game with the surrounding parentheses. Special characters remain as-is.
- Every update of an item or an essence shows instantly the gained or lost stats.
- User profiles are not supported. Although the app saves the gear config in LocalStorage, the browser session expires after 24hrs so make sure to copy and save the export string yourself.
- **Pro-tip**: if you create a gearset and overwrite it by importing an existing string, the stat values panel will show the difference between the two sets.

### Known issues:
- Gear with scaling stats (e.g. from Epic Battles) is displayed on the Wiki with stat ranges instead of a unique value per stat. The item will be loaded in the respective slot but it will not be included in the stat sheet calculations.
- The app cannot handle Legacy of Morgoth slot-specific essences. Regular essences are limited to single-stat ones.
- Baseline character stats coming from level are **not** taken into account.

Border images and the CSS style to use them seen at [Giseldah](https://giseldah.github.io/).