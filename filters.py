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
def item_tooltip(context, itemName):
    try:
        resp = requests.get(
            url = 'https://lotro-wiki.com/wiki',
            params = {
                'action' : 'render',
                'title' : 'Item:' + itemName
            }
        ).text

        tooltip_HTML_start_at = resp.index('<div class="tooltip-content itemtooltip"', 0)
        tooltip_HTML_end_at = resp.index('</ul></div>', tooltip_HTML_start_at) + len('</ul></div>')

        # fixing the image paths
        to_return = resp[tooltip_HTML_start_at : tooltip_HTML_end_at]
        to_return = to_return.replace('/images/', 'https://lotro-wiki.com/images/')

        # making the item name a link
        tooltip_item_name_start = to_return.index('<span class="qc', 0)
        tooltip_item_name_end = to_return.index('</span>', tooltip_item_name_start) + len('</span>')
        item_name_HTML = to_return[tooltip_item_name_start : tooltip_item_name_end]
        to_return = to_return.replace(
            item_name_HTML,
            '<a href="https://lotro-wiki.com/wiki/Item:' + urllib.parse.quote_plus(itemName).replace('+', '_') + '" target="_blank" style="color: inherit;">' + item_name_HTML + '</a>'
        )
    except:
        to_return = 'Tooltip could not be loaded.'
    
    return to_return

@jinja2.pass_context
@f_bp.app_template_filter()
def encode_gear_config(context, gear_config):
    return b64encode(zlib.compress(json.dumps(gear_config).encode('utf-8'))).decode('utf-8')