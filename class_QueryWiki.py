import requests
import urllib

class QueryWiki:

    def __init__(self):

        self.__wikiItem = None
        self.__wikiItemErrorMsg = None

        self.__wikiItemIcon = None
        self.__wikiItemIconErrorMsg = None


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
            else:
                self.__wikiItem = resp_JSON['query']['pages'][page]['revisions'][0]['slots']['main']['*']

        self.__getItemIcon()


    def __getItemIcon(self):

        if (self.__wikiItemErrorMsg is None):

            try:
                iconID = self.__wikiItem.split('icon')[1].split('\n|')[0]
            except:
                self.__wikiItemIconErrorMsg = 'No icon is available for selected item.'

        
            if(iconID):

                iconID = str.strip(iconID, ' =\t')

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

        return {
            'item': {
                'name' : urllib.parse.quote_plus(itemName).replace('+', '_'),
                'slot' : None if ((self.__wikiItem is None) or self.__wikiItem.find('slot') == -1) else str.strip(self.__wikiItem.split('slot')[1].split('\n|')[0].lower(), ' =\t'),
                'type' : None if ((self.__wikiItem is None) or self.__wikiItem.find('type') == -1) else str.strip(self.__wikiItem.split('type')[1].split('\n|')[0].lower(), ' =\t'),
                'scaled' : None if ((self.__wikiItem is None) or self.__wikiItem.find('scaled') == -1) else str.strip(self.__wikiItem.split('scaled')[1].split('\n|')[0].lower(), ' =\t'),
                'attrib' : None if (self.__wikiItem is None) else [str.strip(x, ' =\t') for x in self.__wikiItem.split('attrib')[1].split('\n|')[0].split('<br>')],
                                                                                                          # we are checking length because certain items from Legacy of Morgoth with specific essences
                                                                                                          # (e.g. cloak or neck), get returned from the API with empty (but existing!) attribute "essences"
                                                                                                          # while having the respective attribute "essences-[SLOT]"
                'essences' : 0 if ((self.__wikiItem is None) or self.__wikiItem.find('essences') == -1 or len(str.strip(self.__wikiItem.split('essences')[1].split('\n|')[0].lower(), ' =\t')) == 0) else str.strip(self.__wikiItem.split('essences')[1].split('\n|')[0].lower(), ' =\t'),
                'error' : self.__wikiItemErrorMsg
            },
            'icon' : {
                'URL' : self.__wikiItemIcon,
                'error' : self.__wikiItemIconErrorMsg
            }
        }