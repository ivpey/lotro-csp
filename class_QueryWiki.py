import requests
import urllib
import re

class QueryWiki:

    def __init__(self):

        self.__wikiItem = {}
        self.__wikiItemErrorMsg = None

        self.__wikiItemIcon = None
        self.__wikiItemIconErrorMsg = None

        self.__allStatsList = ['Might', 'Agility', 'Vitality', 'Will', 'Fate', 'Critical Rating', 'Finesse Rating',
                               'Physical Mastery Rating', 'Tactical Mastery Rating', 'Outgoing Healing Rating',
                               'Resistance Rating', 'Block Rating', 'Parry Rating', 'Evade Rating','Physical Mitigation',
                               'Tactical Mitigation', 'Maximum Morale', 'In-Combat Morale Regeneration',
                               'Non-Combat Morale Regeneration', 'Maximum Power', 'In-Combat Power Regeneration', 'Non-Combat Power Regeneration']


    def __getItemPage(self, itemName):

        resp_JSON = requests.get(
            url = 'https://lotro-wiki.com/w/api.php',
            params = {
                'action' : 'query',
                'format' : 'json',
                'prop' : 'revisions',
                'rvslots' : '*',
                'rvprop' : 'content',
                'titles' : 'Item:' + itemName
            }
        ).json()

        for page in resp_JSON['query']['pages']:
            
            if page == '-1':
                self.__wikiItemErrorMsg = 'Please enter a valid item name.'
                return

            resp = resp_JSON['query']['pages'][page]['revisions'][0]['slots']['main']['*']
            
            # the part we need is here in a "nicely" formatted way like
            # attribute = value \n with bunch of trailing spaces and other characters
            resp = resp[resp.index('<onlyinclude>', 0) : resp.index('</onlyinclude>', 0)]

            # this will be a cleaned-up dictionary version of the above
            res_keys = {}
            for row in resp.split('\n'):
                row_items = row.split('=')
                # list with length 1 happens for the beginning and ending rows without real attributes there;
                # list with length 3 or more happens e.g. for sell value and disenchant where the format is {{Worth|s=83|c=34}} and {{disenchants|embers=75}}
                if len(row_items) == 2:
                    res_keys.update({
                        str.strip(row_items[0], '\t| ').lower() : str.strip(row_items[1])
                    })

            item_stats = {}
            for group in res_keys['attrib'].split('<br>'):
                # if a stat does not exist in our list of stats we want to display
                # or if we have a scaling item with stats such as +X Vitality,
                # then skip and move to the next stat
                try:
                    item_stats[[stat for stat in self.__allStatsList if stat in group][0]] = int(re.search(r'[\d+,?\d+]+', group).group().replace(',', ''))
                except:
                    pass

            res_keys['attrib'] = item_stats

            self.__wikiItem = res_keys

        self.__getItemIcon()


    def __getItemIcon(self):

        if (self.__wikiItemErrorMsg is None):

            try:
                iconID = self.__wikiItem['icon']
            except:
                self.__wikiItemIconErrorMsg = 'No icon is available for selected item.'

        
            if(iconID):

                # in case of regular images referenced by a unique ID
                resp_JSON = requests.get(
                    url = 'https://lotro-wiki.com/w/api.php',
                    params = {
                        'action' : 'query',
                        'format' : 'json',
                        'prop' : 'imageinfo',
                        'iiprop' : 'url',
                        'titles' : 'File:' + iconID + '.png'
                    }
                ).json()

                for page in resp_JSON['query']['pages']:
                    if page == '-1':
                        # this means that most likely the image is a generic one referenced by filename instead of ID,
                        # and as such api.php doesn't have prop=imageInfo about it
                        #
                        # solution via https://stackoverflow.com/a/46441957
                        self.__wikiItemIcon = requests.get('https://lotro-wiki.com/wiki/Special:FilePath/' + iconID + 'icon.png').url
                    else:
                        self.__wikiItemIcon = resp_JSON['query']['pages'][page]['imageinfo'][0]['url']

        else:
            self.__wikiItemIconErrorMsg = 'No item was found.'

    def get(self, itemName):

        self.__getItemPage(itemName)

        # we will consider the essences specific to the Legacy of Morgoth expansion as regular ones
        essence_counter = 0
        for k, v in self.__wikiItem.items():
            if k.startswith('essence'): # specific essences are their own key such as essence-primary or essence-cloak or essence-neck
                essence_counter += int(v.strip() or 0)
            

        return {
            'item': {
                'name': urllib.parse.quote_plus(itemName).replace('+', '_'), # doing this just to make sure we transfer it with properly escaped quotes;
                                                                             # turning it back into normal text is handled by a filter;
                                                                             # we can't use self.__wikiItem['name'] because converting THAT back to human-readable just doesn't work
                'slot': None if 'slot' not in self.__wikiItem else str(self.__wikiItem['slot']).lower(),
                'type': None if 'type' not in self.__wikiItem else str(self.__wikiItem['type']).lower(),
                'isScaled' : self.__wikiItem.get('scaled', False),
                'isWeapon': (bool(self.__wikiItem.get('dmg', False)) and bool(self.__wikiItem.get('dps', False))),
                'attrib': self.__wikiItem.get('attrib', None),
                'essences': essence_counter,
                'error': self.__wikiItemErrorMsg
            },
            'icon': {
                'URL' : self.__wikiItemIcon,
                'error' : self.__wikiItemIconErrorMsg
            }
        }