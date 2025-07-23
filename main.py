# ====================
# import packages
# ====================
from flask import Flask, render_template, request, flash, redirect, url_for, session, make_response, send_from_directory
import requests
import requests_cache
import urllib
import copy
import ast
from uuid import uuid4
from base64 import b64encode, b64decode
import zlib
from datetime import timedelta
import json

# ====================
# import the custom class definitions
# ====================
from class_Character_Sheet import Character_Sheet
from class_StatTable import Stat_Table
from class_QueryWiki import QueryWiki

# ====================
# instantiate the app
# ====================
app = Flask(__name__)
app.config['SECRET_KEY'] = 'AMRSONPL'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours = 24)

requests_cache.install_cache('lotro-csp-cache', expire_after=86400, allowable_methods=('GET'))

# this needs to be requested from the Wiki just once for the entire app
stat_sheet = Stat_Table()

# Class Instances Per User
# each user session gets its own class instances which we store here against a unique userID
cipu = {}

def session_handler(session):
    if 'user' not in session:
        session['user'] = str(uuid4().hex)
        cipu[session['user']] = {
            'curr_stats' : Character_Sheet(),
            'old_stats' : Character_Sheet()
        }
    elif (cipu == {}): # to handle gracefully the case when e.g. the service is restarted while a user is working
        cipu[session['user']] = {
            'curr_stats' : Character_Sheet(),
            'old_stats' : Character_Sheet()
        }

    return cipu[session['user']]

# enable caching for static files
# seen at https://stackoverflow.com/questions/77569410/flask-possible-to-cache-images
@app.route('/static/<path:filename>')
def lcsp_cache_static(filename):
    resp = make_response(send_from_directory('static/', filename))
    resp.headers['Cache-Control'] = 'max-age'
    return resp

@app.template_filter()
def format_url_unquote(val, isItemName = False):
    formatted = urllib.parse.unquote_plus(val)
    if (isItemName == True):
        formatted = formatted.replace('_', ' ')
    return formatted

@app.template_filter()
def item_tooltip(itemName):
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
            '<a href="https://lotro-wiki.com/wiki/Item:' + urllib.parse.quote_plus(itemName).replace('+', '_') + '" style="color: inherit;">' + item_name_HTML + '</a>'
        )
    except:
        to_return = 'Tooltip could not be loaded.'
    
    return to_return

@app.template_filter()
def encode_gear_config(gear_config):
    return b64encode(zlib.compress(json.dumps(gear_config).encode('utf-8'))).decode('utf-8')

@app.route("/")
def stats_panel_page():
    s = session_handler(session)

    return render_template(
        'stat-panel.html',
        char_sheet = s['curr_stats'],
        stat_sheet = stat_sheet,
        old_stats = s['old_stats'])

@app.route("/handle_choices", methods = ['POST'])
def handle_choices():
    s = session_handler(session)

    import_str = request.form.get('load_stored')
    selected_class = request.form.get('class-selection')
    
    if (selected_class in s['curr_stats'].class_list):
        s['curr_stats'].class_name = selected_class
        return redirect(url_for('stats_panel_page', hc = 'y'))

    if import_str is None:
        s['curr_stats'].itemSlots = Character_Sheet().itemSlots
    else:
        try:
            a = json.loads(zlib.decompress(b64decode(import_str)).decode('utf-8'))
        except:
            s['curr_stats'].itemSlots = Character_Sheet().itemSlots
            flash('Import failed.')
            return redirect(url_for('stats_panel_page', hc = 'y'))

        if (isinstance(a, dict)):
            e = False
            for k in a.keys():
                if(k not in Character_Sheet().itemSlots.keys() and k != 'class'):
                    e = True

            if not e:
                if ('class' in a.keys() and a['class'] in s['curr_stats'].class_list): # there is a 'class' key and contains expected value
                    s['curr_stats'].class_name = a['class']
                    a.pop('class')
                    s['curr_stats'].itemSlots = a
                elif ('class' in a.keys()): # there is a 'class' key but contains unexpected value
                    a.pop('class')
                    s['curr_stats'].itemSlots = a
                else:
                    s['curr_stats'].itemSlots = a
            else:
                flash('Import failed.')
        else:
            flash('Import failed.')

    return redirect(url_for('stats_panel_page', hc = 'y'))

@app.route("/load_items", methods = ['POST'])
def load_items():
    s = session_handler(session)

    selected_class = request.form.get('class-selection')
    if (selected_class in s['curr_stats'].class_list):
        s['curr_stats'].class_name = selected_class

    item_slot = request.args.get('item')
    item_name = str.strip(request.form.get(item_slot), '[ ]')

    s['old_stats'] = copy.deepcopy(s['curr_stats'])

    # deleting an item
    if (item_slot and item_name == ''):
        flash(s['curr_stats'].validateSlotUpdate(item_slot, {}, None), item_slot)
    else:
        try:
            existingItemName = s['curr_stats'].itemSlots[item_slot]['item-info']['name']
            newItemName = urllib.parse.quote_plus(item_name).replace('+', '_')
            
            # same item -> we make no request, only handle essences if applicable
            if (newItemName == existingItemName):
                try:
                    essence_count = len(s['curr_stats'].itemSlots[item_slot]['item-info']['essences'])
                    essences = {}
                    for i in range(essence_count):
                        essence_stat_name = request.form.get('essence_'+str(i+1)+'_stat')
                        essence_val = request.form.get('essence_'+str(i+1)+'_value')
                        # handling the case when we submit empty
                        essence_val = 0 if essence_val == '' else essence_val
                        if (int(essence_val) != 0 and essence_stat_name != 0):
                            essences[str(i+1)] = {
                                essence_stat_name : essence_val
                            }
                        else:
                            essences[str(i+1)] = {}
                    flash(s['curr_stats'].validateSlotUpdate(item_slot, None, essences), item_slot)
                except:
                    pass
            # submitted an item with a different name -> request new
            else:
                wikiResp = QueryWiki().get(item_name)
                if (wikiResp['item']['error'] is None):
                    flash(s['curr_stats'].validateSlotUpdate(item_slot, wikiResp, None), item_slot)
                else:
                    flash(wikiResp['item']['error'], item_slot)
        
        # submitted a brand new item
        except:
            wikiResp = QueryWiki().get(item_name)
            if (wikiResp['item']['error'] is None):
                flash(s['curr_stats'].validateSlotUpdate(item_slot, wikiResp, None), item_slot)
            else:
                flash(wikiResp['item']['error'], item_slot)

    return render_template(
        'stat-panel.html',
        char_sheet = s['curr_stats'],
        stat_sheet = stat_sheet,
        old_stats = s['old_stats'])

if __name__ == '__main__':  
   app.run(host = '0.0.0.0', port = 5000)