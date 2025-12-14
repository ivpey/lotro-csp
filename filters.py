# ====================
# import packages
# ====================
import jinja2
from flask import Blueprint
import urllib
import requests
import zlib
import json
from base64 import b64encode
from bs4 import BeautifulSoup
import re

# this method of loading filters from a separate file seen at
# https://stackoverflow.com/a/24435908

f_bp = Blueprint('filters', __name__)

@jinja2.pass_context
@f_bp.app_template_filter()
def format_url_unquote(context, val, isItemName = False):
    formatted = urllib.parse.unquote_plus(val)
    if (isItemName == True):
        formatted = formatted.replace('_', ' ')
    return formatted

@jinja2.pass_context
@f_bp.app_template_filter()
def item_tooltip(context, itemName, itemEssences):
    try:

        #
        # START
        #
        # Code for grabbing the URLs of essence icons from a page which contains an index of essences.
        # We don't need this to run every single time an essence icon is needed, rather
        # instead of hardcoding it like below (essence_icon_URLs_list) it should be stored in a DB of some sort and updated
        # every once in a while in a background job. 
        #

        # # function definition stolen from https://www.mediawiki.org/wiki/API:Continue
        # def query(request):
        #     request['action'] = 'query'
        #     request['format'] = 'json'
        #     last_continue = {}
        #     while True:
        #         # Clone original request
        #         req = request.copy()
        #         # Modify it with the values returned in the ’continue' section of the last result.
        #         req.update(last_continue)
        #         # Call API
        #         result = requests.get('https://lotro-wiki.com/w/api.php', params=req).json()
        #         if 'error' in result:
        #             raise Exception(result['error'])
        #         if 'warnings' in result:
        #             print(result['warnings'])
        #         if 'query' in result:
        #             yield result['query']
        #         if 'continue' not in result:
        #             break
        #         last_continue = result['continue']

        # all_essence_img_filenames = []

        # for result in query(
        #     {
        #         'titles': 'Essences_(Level_131-140)_Index',
        #         'prop': 'images'
        #     }
        # ):
        #     # 237151 is the pageID which we hardcode because it doesn't change 
        #     all_essence_img_filenames.extend(result['pages']['237151']['images'])

        # # as it returns 3 different rarities, we filter only one of them - i.e. with the prettiest icon
        # all_essence_img_filenames = [essence_icon['title'] for essence_icon in all_essence_img_filenames if 'incomparable' in essence_icon['title']]

        # # we reuse some code fom class_QueryWiki.py to grab the img urls
        # for img in all_essence_img_filenames:
        #     resp_JSON = requests.get(
        #                     url = 'https://lotro-wiki.com/w/api.php',
        #                     params = {
        #                         'action' : 'query',
        #                         'format' : 'json',
        #                         'prop' : 'imageinfo',
        #                         'iiprop' : 'url',
        #                         'titles' : img
        #                     }
        #                 ).json()
        #     for page in resp_JSON['query']['pages']:
        #         print(resp_JSON['query']['pages'][page]['imageinfo'][0]['url'])

        # END
        
        item_page_BS = BeautifulSoup(
            markup = requests.get(url = 'https://lotro-wiki.com/wiki', params = {'action' : 'render', 'title' : 'Item:' + itemName}).text,
            features = 'lxml'
        )

        tooltip_content = item_page_BS.find(class_ = 'tooltip-content itemtooltip')

        for url in tooltip_content.find_all('img'):
            if '/images/' in url['src']:
                url['src'] = url['src'].replace('/images/', 'https://lotro-wiki.com/images/')

        essence_images_list = [essence_img for essence_img in tooltip_content.find_all('img', src = 'https://lotro-wiki.com/images/c/c7/Empty_Essence_Slot-icon.png')]

        essence_icon_URLs_list = {
            'Agility': 'https://lotro-wiki.com/images/9/94/Essence_of_Agility_%28incomparable%29-icon.png',
            'Block Rating': 'https://lotro-wiki.com/images/2/22/Essence_of_Blocking_%28incomparable%29-icon.png',
            'Critical Rating': 'https://lotro-wiki.com/images/e/e8/Essence_of_Critical_Rating_%28incomparable%29-icon.png',
            'Evade Rating': 'https://lotro-wiki.com/images/6/67/Essence_of_Evasion_%28incomparable%29-icon.png',
            'Fate': 'https://lotro-wiki.com/images/5/5a/Essence_of_Fate_%28incomparable%29-icon.png',
            'Finesse Rating': 'https://lotro-wiki.com/images/6/63/Essence_of_Finesse_%28incomparable%29-icon.png',
            'Might': 'https://lotro-wiki.com/images/5/58/Essence_of_Might_%28incomparable%29-icon.png',
            'Parry Rating': 'https://lotro-wiki.com/images/4/48/Essence_of_Parrying_%28incomparable%29-icon.png',
            'Physical Mastery Rating': 'https://lotro-wiki.com/images/7/70/Essence_of_Physical_Mastery_%28incomparable%29-icon.png',
            'Physical Mitigation': 'https://lotro-wiki.com/images/4/49/Essence_of_Physical_Mitigation_%28incomparable%29-icon.png',
            'Resistance Rating': 'https://lotro-wiki.com/images/7/7b/Essence_of_Resistance_%28incomparable%29-icon.png',
            'Tactical Mastery Rating': 'https://lotro-wiki.com/images/e/ed/Essence_of_Tactical_Mastery_%28incomparable%29-icon.png',
            'Tactical Mitigation': 'https://lotro-wiki.com/images/3/32/Essence_of_Tactical_Mitigation_%28incomparable%29-icon.png',
            'Vitality': 'https://lotro-wiki.com/images/a/ad/Essence_of_Vitality_%28incomparable%29-icon.png',
            'Will': 'https://lotro-wiki.com/images/1/17/Essence_of_Will_%28incomparable%29-icon.png',
            'Maximum Morale': 'https://lotro-wiki.com/images/6/67/Essence_of_Morale_%28incomparable%29-icon.png',
            'Outgoing Healing Rating': 'https://lotro-wiki.com/images/f/fa/Essence_of_Healing_%28incomparable%29-icon.png'
        }
        # unused at present - 'https://lotro-wiki.com/images/e/ee/Essence_of_Critical_Defence_%28incomparable%29-icon.png'
        # unused at present - 'https://lotro-wiki.com/images/3/35/Essence_of_Restoration_%28incomparable%29-icon.png'

        # if an item does not have essence slots
        #
        # apparently if a dict key does not exist and the reference to it is still passed to a filter function,
        # the variable which gets inside is jinja2.runtime.Undefined and not None or empty string
        if isinstance(itemEssences, jinja2.runtime.Undefined):
            return str(tooltip_content)

        # essence here is a tuple
        for essence in itemEssences.items():

            # if an item has essence slots but they aren't set
            if len(essence[1].keys()) == 0:
                continue

            # essence[0] gives the key - in our case 1, 2, 3, etc., i.e. a representation of the index;
            # this is how we find the respective entry in essence_images_list
            #
            # essence[1] gives the value - in our case, another dictionary where key = stat name, and value = amount of the stat;
            # this is how we will replace the text of the <span> element in the sequence li > span > a > img
            #
            # we take every time the first element because by design this dictionary has only a single key-value pair

            # first replace the URLs for the image and its parent link element
            essence_images_list[int(essence[0]) - 1]['src'] = essence_icon_URLs_list[list(essence[1].keys())[0]]
            essence_images_list[int(essence[0]) - 1].parent['href'] = essence_icon_URLs_list[list(essence[1].keys())[0]]

            # because we cannot modify only the text portion of a a tag's content, we need to copy the tag
            the_SPAN_tag_2nd_parent_of_IMG = essence_images_list[int(essence[0]) - 1].parent.parent.__copy__()
            # and then replace the entire contents of the whichever parent element
            the_LI_tag = essence_images_list[int(essence[0]) - 1].parent.parent.parent
            the_LI_tag.clear()
            the_LI_tag.append(the_SPAN_tag_2nd_parent_of_IMG)
            the_LI_tag.append(f' +{list(essence[1].values())[0]} {list(essence[1].keys())[0]}')

        # making the item name a link
        item_name_tag = tooltip_content.find('span', class_= re.compile(r'qc-'))
        item_name_string = item_name_tag.string
        the_link = item_page_BS.new_tag(name ='a', href='https://lotro-wiki.com/wiki/Item:' + urllib.parse.quote_plus(itemName).replace('+', '_'), target = '_blank', style = 'color: inherit;')
        the_link.string = item_name_string

        item_name_tag.clear()
        item_name_tag.append(the_link)

        to_return = str(tooltip_content)

    except:
        to_return = 'Tooltip could not be loaded.'
    
    return to_return

@jinja2.pass_context
@f_bp.app_template_filter()
def encode_gear_config(context, gear_config):
    return b64encode(zlib.compress(json.dumps(gear_config).encode('utf-8'))).decode('utf-8')