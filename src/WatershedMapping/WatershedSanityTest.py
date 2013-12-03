'''
Created on Nov 22, 2013

@author: Scott
'''

import utils.Utils as utils
import utils.Filters as Filters
import WatershedMapping.watershed_mapping as ws_map
import WatershedMapping.WatershedMerge as WatershedMerge


def run(filepath,filename, gradient, step, merge_limit):
    #Filters.green_blue_filter(utils.get_array(filepath+filename))#
    grey_array = utils.greyscale(utils.get_array(filepath+filename))
    
    for x in range(0,len(grey_array)):
        for y in range(0, len(grey_array[0])):
            grey_array[x][y] = 255 - grey_array[x][y]
    
    
    
    print("size: " + str(len(grey_array)) + " X " + str(len(grey_array[0])) + " (pixels: " + str(len(grey_array) * len(grey_array[0])) + ")")
    ws = None
    gradstring = ""
    if gradient:
        ws = ws_map.build_index_map(utils.get_gradient(grey_array))
        gradstring = "-gradient-"
    else:
        ws = ws_map.build_index_map(utils.inverse(grey_array))
        gradstring = "-reverse-"
    
    edge_merges = dict()
    s = 0
    while s < merge_limit:
        edge_merges = WatershedMerge.merge_watersheds_at_limit(edge_merges, ws, s)
        utils.write_image(ws.get_watershed_picture(edge_merges,len(grey_array), len(grey_array[0])), filepath +filename[:-4]+ gradstring + str(s) + filename[-4:])
        s += step



if __name__ == '__main__':
    
    path = "../../data/"
    
    
    did_not_do = "Giant_squid_west_coast.png",
    wwii = ["class_notes.png"]
    
    for name in wwii:
        gradient = False
        merge_limit = 40
        step = 2
        run(path,name, gradient, step, merge_limit)
        
        
        