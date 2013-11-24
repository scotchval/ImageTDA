'''
Created on Nov 22, 2013

@author: Scott
'''

import utils.Utils as utils
import WatershedMapping.watershed_mapping as ws_map


def run(filename):
    grey_array = utils.greyscale(utils.get_array(filename))
    
    print("size: " + str(len(grey_array)) + " X " + str(len(grey_array[0])) + "( pixels: " + str(len(grey_array) * len(grey_array[0])) + ")")
    
    ws = ws_map.build_index_map(utils.get_gradient(grey_array))
    #print(ws.get_edge_weight_map())

    utils.write_image(ws.get_watershed_picture(len(grey_array), len(grey_array[0])), "../../data/dukegradws.png")




if __name__ == '__main__':
    
    path = "../../data/"
    
    run(path + "duke.png")