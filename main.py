# ====================
# import packages
# ====================
from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import requests_cache
import urllib
import copy
import ast

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

requests_cache.install_cache('demo_cache', expire_after=86400, allowable_methods=('GET'))

curr_stats = Character_Sheet()
old_stats = Character_Sheet()
stat_sheet = Stat_Table()

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
    except:
        to_return = 'Tooltip could not be loaded.'
    
    return to_return

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/stats_panel")
def stats_panel_page():
    return render_template('stat-panel.html', char_sheet = curr_stats, stat_sheet = stat_sheet, old_stats = old_stats)

@app.route("/handle_choices", methods = ['POST'])
def handle_choices():

    import_str = request.form.get('load_stored')
    selected_class = request.form.get('class-selection')
    
    if (selected_class in curr_stats.class_list):
        curr_stats.class_name = selected_class
        return redirect(url_for('stats_panel_page'))

    if import_str is None:
        curr_stats.itemSlots = Character_Sheet().itemSlots
    else:
        try:
            a = ast.literal_eval(import_str)
            if (isinstance(a, dict)):
                if(a.keys() == Character_Sheet().itemSlots.keys()):
                    curr_stats.itemSlots = a
                else:
                    flash('Import failed.')
            else:
                try:
                    a = ast.literal_eval(a)
                    if (isinstance(a, dict)):
                        if(a.keys() == Character_Sheet().itemSlots.keys()):
                            curr_stats.itemSlots = a
                        else:
                            flash('Import failed.')
                    else:
                        flash('Import failed.')
                except:
                    flash('Import failed.')
        except:
            flash('Import failed.')

    return redirect(url_for('stats_panel_page'))

@app.route("/load_items", methods = ['POST'])
def load_items():

    selected_class = request.form.get('class-selection')
    if (selected_class in curr_stats.class_list):
        curr_stats.class_name = selected_class

    item_slot = request.args.get('item')
    item_name = str.strip(request.form.get(item_slot), '[ ]')

    old_stats = copy.deepcopy(curr_stats)

    # deleting an item
    if (item_slot and item_name == ''):
        flash(curr_stats.validateSlotUpdate(item_slot, {}, None), item_slot)
    else:
        try:
            existingItemName = curr_stats.itemSlots[item_slot]['item-info']['name']
            newItemName = urllib.parse.quote_plus(item_name).replace('+', '_')
            
            # same item -> we make no request, only handle essences if applicable
            if (newItemName == existingItemName):
                try:
                    essence_count = len(curr_stats.itemSlots[item_slot]['item-info']['essences'])
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
                    flash(curr_stats.validateSlotUpdate(item_slot, None, essences), item_slot)
                except:
                    pass
            # submitted an item with a different name -> request new
            else:
                wikiResp = QueryWiki().get(item_name)
                if (wikiResp['item']['error'] is None):
                    flash(curr_stats.validateSlotUpdate(item_slot, wikiResp, None), item_slot)
                else:
                    flash(wikiResp['item']['error'], item_slot)
        
        # submitted a brand new item
        except:
            wikiResp = QueryWiki().get(item_name)
            if (wikiResp['item']['error'] is None):
                flash(curr_stats.validateSlotUpdate(item_slot, wikiResp, None), item_slot)
            else:
                flash(wikiResp['item']['error'], item_slot)

    return render_template('stat-panel.html', char_sheet = curr_stats, stat_sheet = stat_sheet, old_stats = old_stats)

if __name__ == '__main__':  
   app.run()