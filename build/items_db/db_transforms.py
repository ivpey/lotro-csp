def parse_essence_slot(data:str|None) -> dict:
    """
        Args:
            data (str|None): can be a real string, e.g. 'CP' (cloak essence slot + primary essence slot),
                             or a number stored as string (indicating number of slots for basic essences)
                             or it can be empty (no essence slots).
        Returns:
            (dict): empty for no essence slots, or filled with key = type of essence and value = number of slots.
                    In the sqlite database essence types are found in the type column with slot = 'ESSENCE'.
                    Possible values are:
                    ['WAR', 'CLOAK', 'NECK', 'PRIMARY', 'VITAL', 'BASIC']
    """

    if data is None:
        return {}
    try:
        return {'BASIC': int(data)}
    except ValueError:
        essence_dict = {letter:sum([1 for letter_to_count in data if letter_to_count == letter]) for letter in data}
        for essence_type in zip(
            ['W', 'C', 'N', 'P', 'V', 'S'],
            ['WAR', 'CLOAK', 'NECK', 'PRIMARY', 'VITAL', 'BASIC']
        ):
            abbreviated = essence_type[0]
            full = essence_type[1]
            # replacing the short version with a more descriptive one
            if abbreviated in essence_dict.keys():
                essence_dict[full] = essence_dict.pop(abbreviated)
        return essence_dict
    except Exception as e:
        raise e

def parse_slot(item) -> str:
    match item.get('slot'):
        case 'LEFT_EAR' | 'RIGHT_EAR' | 'EAR':
            return 'EAR'
        case 'RIGHT_FINGER' | 'LEFT_FINGER' | 'FINGER':
            return 'FINGER'
        case  'LEFT_WRIST' | 'RIGHT_WRIST' | 'WRIST':
            return 'WRIST'
        case _:
            if item.get('category') == 'ESSENCE':
                return 'ESSENCE'
            else:
                return item.get('slot')

def parse_type(item) -> str:
    if item.get('category') == 'ESSENCE':
        match item.get('type'):
            case "18":
                return 'WAR'
            case "19":
                return 'BACK'
            case "20":
                return 'NECK'
            case "22":
                return 'PRIMARY'
            case "23":
                return 'VITAL'
            case "1":
                return 'BASIC'
    elif item.get('armourType') is not None:
        return item.get('armourType')
    elif item.get('weaponType') is not None:
        return item.get('weaponType')
    elif parse_slot(item) in ['EAR', 'FINGER', 'WRIST', 'POCKET', 'NECK']:
        return 'JEWELRY'
    else:
        return item.get('slot')