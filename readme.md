# What this is

A hobby programming project to help me learn the Python package Flask. Incidentally, I ended up learning much much more than just Flask with this project.

In 2025, I set out to create a personal-use gear planner for a game which holds a special place in my heart - Lord of the Rings Online. The idea was simple:
- keep the familiar interface of the Character Panel from in-game
- show live stat deltas as items are swapped around
- give option to import/export gear configurations without maintaining a database of the gearsets everyone has ever made
- (eventually) allow simulation of gear combinations
- most importantly - **no app to download or install; pure web version, no login or registration needed**

Version 1 of this project used the Lotro Wiki as a data source, and would query its API any time an item lookup was needed - that is, no data was stored locally at any point. At the time, I was not aware of any other place I could get item data from, and I did not care to learn how to webscrape the Wiki in order to create my own database. Not to mention that this being my very first Flask app, the code was a complete mess that did not follow any sane programming / SWE conventions. It did work, though!

The need for Version 2 arose a year later when Lotro Wiki introduced CloudFlare and my app's API requests started getting blocked. Rather than look for a way around this, I decided to completely rework the project following best practices which I had (hopefully) picked up since starting to code almost exclusively in Python at my job.

I will be documenting my progress in a few chronological `.md` files broken down by topic as I tackle each stage of the rewrite.

# Running the build step

Make sure that the `/src` folder contains `items.xml` from https://github.com/LotroCompanion/lotro-items-db and `progressions.xml` from https://github.com/LotroCompanion/lotro-data/tree/master/lore

Then from the project's root folder execute `py -m build.build_pipeline`.