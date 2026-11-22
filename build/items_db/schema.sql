CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    display_name TEXT,        -- original item name with diacritics
    name_normalized TEXT,     -- original item name with stripped diacritics
    icon TEXT,
    slot TEXT,
    quality TEXT,
    base_level INTEGER,
    type TEXT,
    stats_at_base_level TEXT, -- JSON dictionary with
                              --    key = stat name as used in CalcStat
                              --    value = pre-calculated value from applicable progression_id at base level
    progression_ids TEXT,     -- JSON dictionary with
                              --    key = stat name as used in CalcStat
                              --    value = progression ID
                              -- this is used for recalculating stats at an item level different than base_level
    essence_slots TEXT        -- JSON dictionary with
                              --    key = type of essence
                              --    value = number of slots of this type
);

CREATE TABLE progressions (
    id INTEGER PRIMARY KEY,
    points TEXT               -- JSON list of tuples representing x,y points in the progression curve
);