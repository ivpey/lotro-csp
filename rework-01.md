# Stage 1 - getting data

## Before

The options I was aware of for retrieving item data were two:
- the [Item Treasury](https://www.lotrointerface.com/downloads/info870-ItemTreasury.html) plugin which I suspected might maintain [its own items database](https://github.com/dt192/item-treasury-database). Unfortunately, I discovered that this database is a great source of item names but lacks item stats.
- [Lotro Wiki](https://lotro-wiki.com/wiki/Main_Page) which I found had an API.


I will be the first to admit that I had zero experience with the [MediaWiki API](https://www.mediawiki.org/wiki/API). In my hurry to get started on my project, I went for the Action API (advertised as providing "a much broader set of functionality") instead of the REST API.

Example output of the Action API:
```
"__NOTOC__<onlyinclude>{{Item Tooltip\n| mode={{{mode|}}}\n| arg={{{arg|}}}\n| name            = Veteran Sage's Coat\n| disambigpage    = Item:Veteran Sage's Coat\n| item_id         = 1879514857\n| icon            = 1093054727-1090519044-1091947416\n| quality         = Incomparable\n| item_level      = 567{{Color|lime|+}}\n| type            = Light Armour\n| slot            = Chest\n| bind            = BtAoA\n| armour          = 20,995\n| attrib          = +3,783 Vitality <br> +18645 Critical Rating <br> +4631 Tactical Mastery Rating\n| essences        = 2\n| durability      = 35\n| dur_class       = Normal\n| level           = 160\n| set             = Will of the Sage\n| sell            = {{Worth|s=136|c=23}}\n| disenchants     = {{disenchants|embers=300}}\n| first-category  = Update 46 new items\n}}</onlyinclude>\n== Item Information ==\n{{ScaledItem}}\n\n== Drop Info ==\nThis item is a possible drop from the following [[The Lord of the Rings Online: Kingdoms of Harad|Kingdoms of Harad]] Instances:\n* [[K\u00f4th Rau, the Wailing Hold]] ''(Tier 1 - Tier 3)''\nThis item is a possible drop from the [[Legion of Lhaereth]] in [[The Folly of Nagakh\u00eadi]] Raid."
```

Yup. Raw MediaWiki page template syntax (like you would use when editing a WikiPedia page for example) instead of pretty and structured JSON. There was a lot of splitting by `\n` and `=` and `<br>` and playing around with the results until I got it to a usable structure. Two other notable downsides:
- with the Action API you call up a single Wiki page and get its contents and metadata. Unlike a database, you can't run a few `GROUP BY` queries and see what the admissible values are for the fields you work with. Fetch a few dozen pages and make your own mental model, scrub. Or learn to use REST.
- you need to know exactly what you are looking for. No partial or fuzzy search - you have to get the name of the page 100% correct. This includes diacritics and special characters, even if the search function on the Wiki website normalizes the item names allowing e.g. "Damaged M `û`rai Artifact" to be found when typing "Damaged M`u`rai Artifact".

I really wish I had started off with the REST API instead like a normal person even though ultimately I worked out a stable way to process this data.

## After

By some luck I stumbled upon the [Lotro Companion items database](https://github.com/LotroCompanion/lotro-items-db) which contains full item data in XML format.

The first way I found to read XML in Python was `xml.etree.ElementTree` which exposes iterator objects for tree traversal. Convenient, but not practical or performant for direct usage in an app as every lookup becomes a loop over all items.

Still, data exploration was infinitely easier now. Visualizing the structure
```
root:ET.Element = ET.parse(SRC_DIR / 'items.xml').getroot()
for idx, unknown in enumerate(root.iter()):
    if idx >= 5:
        break
    print(unknown, unknown.attrib)
```

and finding all the unique values of the interesting fields
```
items:ET.Element = ET.parse(SRC_DIR / 'items.xml').getroot()
unique_categories = []
for idx, item in enumerate(items.iter('item')):
    c = item.get('category')
    if c not in unique_categories:
        unique_categories.append(c)
```
was a breeze, and allowed me to quickly identify the items about which I do not care in my app - cosmetics, mounts, recipes, housing decorations, grey items without stats, etc.

Ultimately, I needed to maintain the subset of items which are relevant for me somewhere. I settled on a SQLite database that I would have to develop a build pipeline for.

### Database design

The biggest challenge was finding out how to parse the item stats which in the XML file were not final values, but instead certain identifiers which meant nothing to me. I ended up `asking AI` (full disclosure) to explain to me how to read this. Turns out that in game development, handling item / character / whatever stats is done via stat curves, multiples of which can exist for one and the same stat (to be applied to different items e.g. to let one item grow stronger quicker than another as its level increases).

To get the final stat value you find the points between which the level of the item / character / whatever falls and then perform linear interpolation. The identifiers in the XML file were IDs of stat progressions (curves) which lived in another XML file.

In the end, I created two tables in SQLite:
- `items` - containing basic information about the item. I maintain both the original (with diacritics) item name for display purposes, as well as a normalized version computed as follows (thanks, StackOverflow!)
    ```
    import unicodedata
    ''.join(c for c in unicodedata.normalize('NFD', item_dict['display_name']) if unicodedata.category(c) != 'Mn')
    ```
    which will be used for searching the database. Important to note that the search term should **also** be normalized before giving it to the query, to cover for the cases where the user themselves inputs a name with diacritics, e.g. Anórien.
    
    Furthermore, I save both 1/ calculated stats after interpolation (using `numpy.interp()`) at the item's base level, and 2/ the progression IDs themselves. This is important if we want to allow the users to work with items at arbitrary item levels, e.g. to plan their gearset around a juicy T3 drop (higher difficulty = higher item level, above the base one). Both columns in the database are JSON `BLOB`s because:
    
    - it is easier to keep them as a dictionary in a single column rather than split into 19 separate columns, most of which will hold 0 for most items
    - I do not expect to need to perform any operations on the values through the database - even though SQLite is able to parse JSON pretty efficiently according to its documentation
    - having them as a convenient Python object is one `json.loads()` call away.

- `progressions` - ID column, and a JSON `BLOB` column where the points are saved as a list of tuples.

For the build pipeline, I saved my schemas in a `.sql` file as simple `CREATE TABLE` statements which are read and executed during DB set-up. The processing script loops through the XML source files, applies exclusion criteria to the items, precalculates their stats and saves the entries into SQLite.

### Item icons???

Having found the Lotro Companion GitHub repo, I quickly found where the item icons were [collected](https://github.com/LotroCompanion/lotro-icons). I expected I would simply need a way to download them or link to them (hurray for raw links in GitHub!) but curiously, an item icon in the item data XML file looks like this:
```
1090520031-1090519042-1090520032-1090526862
```
while all the item icons in the repo have names like this:
```
1090519041.png
```

Right, I would need another pipeline.

The repo holds the individual components of an item's image which are transparent `.png` files representing:
- an item-specific icon
- a rarity-specific border
- a black shadow in the shape of the item-specific icon
- a blue glow in the shape of the item-specific icon

I found a Python package called `Pillow` which lets us manipulate images - also including combining multiple images into one. `Pillow` can read either a physical file or a byte stream, so my pipeline ended up like so:
1. grab all the unique full icons (e.g. `1090520031-1090519042-1090520032-1090526862`) from the items database
2. split them up into their components and remove any duplicated components
3. using ThreadPoolExecutor, parallelize the download of each component from the GitHub raw link - before this change, the icons pipeline used to take 30+ minutes, now it finishes in less than 2 minutes
4. start layering the components - the layering order was a bit of a trial-and-error until I stopped getting errors about incompatible channels and such.

With ThreadPoolExecutor I also stopped saving the image components to disk; we are looking at ~7k images of ~2KB each - nothing that can't fit into memory. This unlocked a funny problem, though - because `PIL.Image.open()` provides lazy loading, the currently processed image component would often be overlaid on top of the previously processed full image. A `.copy()` command solved this.

### Logging

For both pipelines, I save a `.log` with the reason why a certain item was not processed. DEBUG level logs (e.g. "processing item X out of XYZ") are streamed to the terminal only, INFO level logs (e.g. "starting processing of icons") and WARNING level logs (e.g. "inadmissible item" or "failed to download image") additionally go to the file.

It is important to note that when setting up a logger in a `.py` file as `logger = logging.getLogger(__name__)`, it should be referenced by its full module path if we are indeed calling the build script as a module. In my case I am calling it from the main project directory as
```
py -m build.build_pipeline
```
hence my itemsdb logger ends up being called `build.items_db.build_itemsdb`. If it was only called `build_itemsdb` then it would not match the actual logger name and the file will end up empty (ask me how I know...).

### CLI arguments

Given the number of times I wanted to process just a small number of items and icons to test something, I should have added CLI arguments much earlier:
- `py -m build.build_pipeline --items` to run only items pipeline
- `py -m build.build_pipeline --icons` to run only the icons pipeline. It reads from the `sqlite` db, so it only works on the items which have already been processed (duh)
- `py -m build.build_pipeline --items --items-count=100` to process only 100 items
- `py -m build.build_pipeline --items --items-count=100 --icons` to process only 100 items and their icons