# from calcstat import CalcStat

# stat = 'Might'

# ilvl = 44

# lvl = 44

# b = CalcStat(stat, ilvl)
# c = CalcStat(stat+'T', lvl)

# print(f'Base item {stat} at ilvl {ilvl} is {b}. Player {stat} at lvl {lvl} is {c}. Total = {b+c}')



a = {
    'a': {
        'item-info-1': 'str',
        'item-info': {}
    },
    'b': {
        'item-info-1': 'str',
        'item-info': {}
    },
    'c': {
        'item-info-1': 'str',
        'item-info': {}
    },
    'd': {
        'item-info-1': 'str',
        'item-info': {}
    },
    'e': {
        'item-info-1': 'str',
        'item-info': {
            '1': 123
        }
    },
}


print(bool([item for item in a.items() if item[1]['item-info'] != {}]))