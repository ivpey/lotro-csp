# ====================
# import packages
# ====================
import jinja2
from flask import Flask, render_template, request, flash, redirect, url_for, session, make_response, send_from_directory, Blueprint
import requests_cache
from datetime import timedelta
import urllib
import copy
from base64 import b64decode
import zlib
import json
from uuid import uuid4

# ====================
# import the custom filters
# ====================
import filters

# ====================
# import the custom class definitions
# ====================
from class_Character_Sheet import Character_Sheet
from class_QueryWiki import QueryWiki
from class_StatTable import Stat_Table

# ====================
# instantiate the app
# ====================
app = Flask(__name__)
app.config['SECRET_KEY'] = 'AMRSONPL'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours = 24)
app.register_blueprint(filters.f_bp)

requests_cache.install_cache('lotro-csp-cache', expire_after=86400, allowable_methods=('GET'))

# this needs to be requested from the Wiki just once for the entire app
stat_sheet = Stat_Table()

# Class Instances Per User
# each user session gets its own class instances which we store here against a unique userID
cipu = {}

def session_handler(session):
    if 'user' not in session:
        session['user'] = str(uuid4().hex)

    try:
        curr_sess = cipu[session['user']]
    except:
        curr_sess = {
            'curr_stats' : Character_Sheet(),
            'old_stats' : Character_Sheet()
        }
        cipu[session['user']] = curr_sess
    
    return curr_sess

# enable caching for static files
# seen at https://stackoverflow.com/questions/77569410/flask-possible-to-cache-images
@app.route('/static/<path:filename>')
def lcsp_cache_static(filename):
    resp = make_response(send_from_directory('static/', filename))
    resp.headers['Cache-Control'] = 'max-age'
    return resp

# main
@app.route("/")
def stats_panel_page():
    s = session_handler(session)

    return render_template(
        'stat-panel.html',
        char_sheet = s['curr_stats'],
        stat_sheet = stat_sheet,
        old_stats = s['old_stats'])

# this route handles both loading from LocalStorage, and from manual import;
# it is intentional to treat them the same way and to pass both through the same form with the input field load_stored;
# if we wanted to differentiate them, the JS at the beginning of the HTML page could do another formData.append(...) for a src,
# while the Import form could have a pre-populated hidden input for src
#
# the route also handles class choice selection
@app.route("/handle_choices", methods = ['POST'])
def handle_choices():
    s = session_handler(session)

    # making sure that when we import, the active config from before the import is used for the comparison,
    # this is practically a clumsy way of enabling comparison between two custom configs
    #
    # also in the HTML we handle deltas on class change - simply do not show them, like the other two cases
    s['old_stats'] = copy.deepcopy(s['curr_stats'])

    import_str = request.form.get('load_stored')
    selected_class = request.form.get('class-selection')
    char_level = request.form.get('char-level')
    clear_config = request.form.get('clear-config')

    if char_level is not None:
        s['curr_stats'].character_level = int(char_level)

    # the request is made from the Clear button
    if clear_config is not None:
        s['curr_stats'].itemSlots = Character_Sheet().itemSlots
        return redirect(url_for('stats_panel_page', hc = 'y'))
    
    # only handling class choice selection
    if (selected_class in s['curr_stats'].class_list):
        s['curr_stats'].class_name = selected_class
        return redirect(url_for('stats_panel_page', hc = 'y'))
    
    if import_str is not None:
        # try to parse the imported string
        try:
            a = json.loads(zlib.decompress(b64decode(import_str)).decode('utf-8'))
        except:
            #s['curr_stats'].itemSlots = Character_Sheet().itemSlots
            flash('Import failed.')
            return redirect(url_for('stats_panel_page', hc = 'y'))

        # making sure we received the expected structure and values
        if (not isinstance(a, dict)):
            flash('Import failed.')
            return redirect(url_for('stats_panel_page', hc = 'y'))
        
        # without this we cannot do anything
        if 'itemSlots' not in a.keys():
            flash('Import failed.')
            return redirect(url_for('stats_panel_page', hc = 'y'))

        for k in a['itemSlots'].keys():
            if (k not in Character_Sheet().itemSlots.keys()): #and k != 'class' and k!= 'lvl'):
                flash('Import failed.')
                return redirect(url_for('stats_panel_page', hc = 'y'))

        # without this, we can use a default value
        if 'lvl' in a.keys():
            s['curr_stats'].character_level = Character_Sheet().character_level if a['lvl'] is None else int(a['lvl'])
            # when importing, deltas are shown as comparing with baseline lvl 150 - i.e. the default for an empty class instance
            s['old_stats'].character_level = Character_Sheet().character_level if a['lvl'] is None else int(a['lvl'])
        else:
            s['curr_stats'].character_level = Character_Sheet().character_level

        # without this, we can use a default value
        if 'class' in a.keys() and a['class'] in s['curr_stats'].class_list: # there is a 'class' key and contains expected value
            s['curr_stats'].class_name = a['class']

        s['curr_stats'].itemSlots = a['itemSlots']
        
        # when we import, the comparison is always done against the baseline character stats;
        # it doesn't make sense to have deltas in this case so we handle it here, i.e.
        # by checking if all items are empty
        if bool([item_old for item_old in s['old_stats'].itemSlots.items() if item_old[1]['item-info'] != {}]) == False:
            s['old_stats'] = copy.deepcopy(s['curr_stats'])

    return redirect(url_for('stats_panel_page', hc = 'y'))

@app.route("/load_items", methods = ['POST'])
def load_items():
    s = session_handler(session)

    item_slot = request.args.get('item')
    item_name = str.strip(request.form.get(item_slot), '[ ]')

    s['old_stats'] = copy.deepcopy(s['curr_stats'])

    # deleting an item
    if (item_slot and item_name == ''):
        flash(s['curr_stats'].validateSlotUpdate(item_slot, {}, None), item_slot)
    else:
        try:
            existingItemName = s['curr_stats'].itemSlots[item_slot]['item-info'].get('name', None)
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
   app.run(host = '0.0.0.0', port = 5000, debug = True)