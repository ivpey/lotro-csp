import re
from class_StatTable import Stat_Table

class Character_Sheet:

    def __init__(self, class_name = 'Warden'):

        self.itemSlots = {
            'head': {
                'slot-type' : 'armor',
                'item-info' : {}
            },
            'shoulder': {
                'slot-type' : 'armor',
                'item-info' : {}
            },
            'back' : {
                'slot-type' : 'armor',
                'item-info' : {}
            },
            'chest': {
                'slot-type' : 'armor',
                'item-info' : {}
            },
            'gloves': {
                'slot-type' : 'armor',
                'item-info' : {}
            },
            'legs': {
                'slot-type' : 'armor',
                'item-info' : {}
            },
            'feet': {
                'slot-type' : 'armor',
                'item-info' : {}
            },
            'ear-left': {
                'slot-type': 'jewelry',
                'item-info': {}
            },
            'ear-right': {
                'slot-type': 'jewelry',
                'item-info': {}
            },
            'neck': {
                'slot-type': 'jewelry',
                'item-info': {}
            },
            'wrist-left': {
                'slot-type': 'jewelry',
                'item-info': {}
            },
            'wrist-right': {
                'slot-type': 'jewelry',
                'item-info': {}
            },
            'finger-left': {
                'slot-type': 'jewelry',
                'item-info': {}
            },
            'finger-right': {
                'slot-type': 'jewelry',
                'item-info': {}
            },
            'pocket': {
                'slot-type': 'jewelry',
                'item-info': {}
            }
        }

        self.class_name = class_name

        self.class_list = ['Beorning', 'Brawler', 'Burglar', 'Captain',
                           'Champion', 'Guardian', 'Hunter', 'Lore-master',
                           'Mariner', 'Minstrel', 'Rune-keeper', 'Warden'
                          ]
        
        # this list comes from Stat_Table().listAllStats() but the app is very slow if we pass the class here
        self.__allStatsList = ['Might', 'Agility', 'Vitality', 'Will', 'Fate', 'Critical Rating', 'Finesse Rating',
                               'Physical Mastery Rating', 'Tactical Mastery Rating', 'Outgoing Healing Rating',
                               'Resistance Rating', 'Block Rating', 'Parry Rating', 'Evade Rating','Physical Mitigation',
                               'Tactical Mitigation', 'Maximum Morale', 'In-Combat Morale Regeneration',
                               'Non-Combat Morale Regeneration', 'Maximum Power', 'In-Combat Power Regeneration', 'Non-Combat Power Regeneration']

    def validateSlotUpdate(self, slot, slotData = None, essences = None):
        
        # pre-load the message for success
        notification_msg = f'Updated {slot.upper()} slot.'

        if (slot in [x for x in self.itemSlots]):

            if (slotData is not None and slotData != {}):

                if ((slotData['item']['slot'] is not None) & (slotData['item']['type'] is not None)):
                    
                    if (
                        slot == slotData['item']['slot']                            # armor typically has both SLOT and TYPE
                        or
                        ((slotData['item']['slot'] == 'cloak') & (slot == 'back'))  # certain cloaks have SLOT=CLOAK instead of SLOT=BACK
                        or
                        slotData['item']['slot'] == slot.split('-')[0]              # jewelry typically only has TYPE, but found some rings which have both SLOT and TYPE
                    ):

                        if (slotData['item']['scaled'] is not None):
                            notification_msg = f'Exact stat values cannot be determined for scaled item in slot {slot.upper()}. It will not contribute to stat calculations.'

                        self.__updateSlot(slot, slotData, essences)

                    else:

                        notification_msg = f'Trying to enter {slotData['item']['slot'].upper()} item into {slot.upper()} slot.'

                elif ((slotData['item']['slot'] is None) & (slotData['item']['type'] is not None)):

                    # armor without SLOT
                    if (
                        re.search('[a-zA-Z]+', slotData['item']['type']).group() in ['light', 'medium', 'heavy']
                        and
                        slot in ['head', 'shoulder', 'back', 'chest', 'gloves', 'legs', 'feet']
                    ):
                        
                        if (slotData['item']['scaled'] is not None):
                            notification_msg = f'Exact stat values cannot be determined for scaled item in slot {slot.upper()}. It will not contribute to stat calculations.'

                        self.__updateSlot(slot, slotData, essences)
                        notification_msg = f'The item slot could not be verified in the Wiki. Updated {slot.upper()} slot.'

                    # jewelry
                    else:

                        if (slotData['item']['type'] == slot.split('-')[0]):

                            if (slotData['item']['scaled'] is not None):
                                notification_msg = f'Exact stat values cannot be determined for scaled item in slot {slot.upper()}. It will not contribute to stat calculations.'

                            self.__updateSlot(slot, slotData, essences)

                        else:

                            notification_msg = f'Trying to enter {slotData['item']['type'].upper()} item into {slot.upper()} slot.'

                elif ((slotData['item']['slot'] is not None) & (slotData['item']['type'] is None)):

                    if (
                        slot == slotData['item']['slot']                # pocket item
                        or
                        slotData['item']['slot'] == slot.split('-')[0]  # found some earring which has SLOT but not TYPE
                    ):

                        if (slotData['item']['scaled'] is not None):
                            notification_msg = f'Exact stat values cannot be determined for scaled item in slot {slot.upper()}. It will not contribute to stat calculations.'

                        self.__updateSlot(slot, slotData, essences)

                    else:

                        notification_msg = f'Trying to enter {slotData['item']['slot'].upper()} item into {slot.upper()} slot.'

                else:

                    notification_msg = 'Unknown error.'

            else:

                self.__updateSlot(slot, slotData, essences)

            return notification_msg
        
    def __updateSlot(self, slot, slotData, essences):
        
        # deleting an item
        if (slotData == {}):
            self.itemSlots[slot]['item-info'] = slotData
        
        # updating essences
        elif (slotData is None):
            self.itemSlots[slot]['item-info']['essences'] = essences
        
        # updating the item itself
        else:
            
            self.itemSlots[slot]['item-info'] = {} # reset it
            self.itemSlots[slot]['item-info']['name'] = slotData['item']['name']
            self.itemSlots[slot]['item-info']['icon-url'] = slotData['icon']['URL']

            for attrib in slotData['item']['attrib']:

                try:
                    stat_name = [word for word in self.__allStatsList if word in attrib][0]
                    stat_value = int(re.search(r'[\d+,?\d+]+', attrib).group().replace(',', ''))
                    self.itemSlots[slot]['item-info'][stat_name] = stat_value
                except:
                    pass

            # if from the Wiki we load an item with essences,
            # create the proper structure
            if (slotData['item']['essences'] != 0):
                self.itemSlots[slot]['item-info']['essences'] = {str(i+1):dict() for i in range(int(slotData['item']['essences']))}
            else:
                if('essences' in self.itemSlots[slot]['item-info']):
                    del self.itemSlots[slot]['item-info']['essences']

    def getSlot(self, slot):
        
        # making sure that we can only get an existing attribute
        for attr in self.itemSlots.items():
            if (attr[0] == slot):
                return self.itemSlots[slot]['item-info']

    def getTotalStat(self, stat, statDerivTable = None):
        res = 0

        # first we sum all the occurrences of the given stat in all items
        for slot in self.itemSlots.items():

            if (stat in slot[1]['item-info']):

                res = res + slot[1]['item-info'][stat]

            # handling essences
            if ('essences' in slot[1]['item-info']):
                
                for essence in slot[1]['item-info']['essences']:
                    
                    if (stat in slot[1]['item-info']['essences'][essence]):

                        res = res + int(slot[1]['item-info']['essences'][essence][stat])

        # if we supplied a reference table, then we use it as map
        if (isinstance(statDerivTable, Stat_Table)):

            ms = statDerivTable.listMainStats()

            # main stats are not derived through anything else
            if (stat not in ms):

                t = statDerivTable.getFullTable()

                # but any derived stat may depend on any of the main stats
                for s in ms:

                    total_main_stat = self.getTotalStat(s)
                    multiplier = t.loc[(t['Main stat'] == s) & (t['Derived stat'] == stat), self.class_name].values

                    # multiplier is a series
                    if (len(multiplier) != 0):
                        res = res + total_main_stat*multiplier[0]

                return res

            else:

                return res
            
        else:

            return res