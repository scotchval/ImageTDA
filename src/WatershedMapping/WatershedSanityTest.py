'''
Created on Nov 22, 2013

@author: Scott
'''

import src.utils.Utils as utils
import src.WatershedMapping.watershed_mapping as ws_map
import src.WatershedMapping.WatershedMerge as WatershedMerge


def run(filepath,filename, gradient, merge_limit):
    grey_array = utils.greyscale(utils.get_array(filepath+filename))
    
    print("size: " + str(len(grey_array)) + " X " + str(len(grey_array[0])) + " (pixels: " + str(len(grey_array) * len(grey_array[0])) + ")")
    ws = None
    gradstring = ""
    if gradient:
        ws = ws_map.build_index_map(utils.get_gradient(grey_array))
        gradstring = "-gradient-"
    else:
        ws = ws_map.build_index_map(grey_array)
    
    edge_merges = WatershedMerge.merge_watersheds_at_limit(ws, merge_limit)

    utils.write_image(ws.get_watershed_picture(edge_merges,len(grey_array), len(grey_array[0])), filepath +filename[:-4]+ gradstring + str(merge_limit) + filename[-4:])




if __name__ == '__main__':
    
    path = "../../data/"
    name = "farm.PNG"
    
    gradient = True
    merge_limit=50
    
    run(path,name, gradient, merge_limit)