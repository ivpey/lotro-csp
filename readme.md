# UPDATE 18.06.2026
I revisited this project after almost a year and it seems the Lotro Wiki has introduced Cloudflare which blocks the requests from this app (any programmatic requests really). As I was relying on the Wiki for item data and character stat derivations, this is a breaking change.

Using the Wiki in such way was not the most reliable, but it was the only way I was aware of at the time.

I can attempt to rewrite these modules using [lotro-items-db](https://github.com/LotroCompanion/lotro-items-db) and [CalcStat](https://www.lotrointerface.com/downloads/info1022-CalcStat.html) but I cannot judge the amount of effort it will take or when I will have time to do it.

As of today, Lotro Character Stat Panel is frozen in an unfortunately unusable state.

---

A simple gear planner for the [MMORPG Lord of the Rings Online](https://lotro.com/), pulling item data from the [Lotro Wiki](https://lotro-wiki.com/) and saving the gear config in the browser's LocalStorage or as a convenient export string.

Live demo available at https://lotro-csp.onrender.com/

### How to use:
- Item names can be copied into the app from in-game with the surrounding parentheses. Special characters remain as-is.
- Every update of an item or an essence displays instantly the gained or lost stats.
- To remove an essence, enter 0 for its value and click the Update button.
- User profiles are not supported. Although the app saves the gear config in LocalStorage, the browser session eventually expires so make sure to copy and save the export string yourself.
- **Pro-tip**: if you create a gearset and overwrite it by importing an existing string, the stat values panel will show the difference between the two sets.

### Known issues (initial release - July 2025):
- Gear with scaling stats (e.g. from Epic Battles) is displayed on the Wiki with stat ranges instead of a unique value per stat. The item will be loaded in the respective slot but it will not be included in the stat sheet calculations.
- ~~The app cannot handle Legacy of Morgoth slot-specific essences.~~
- - (Update - September 2025) Slot-specific essences are now treated as regular ones and handled correctly.
- Regular essences are limited to single-stat ones.
- ~~Baseline character stats coming from level are **not** taken into account.~~
- - (Update - October 2025) Level-based base stats are now included thanks to Giseldah's CalcStat module.

Border images and the CSS style to use them seen at [Giseldah](https://giseldah.github.io/).