'''
Created on Nov 22, 2013

@author: Scott
'''

import utils.Utils as utils
import WatershedMapping.watershed_mapping as ws_map


def run(filename):
    grey_array = utils.color_to_grey(utils.get_array(filename))
    ws = ws_map.build_index_map(grey_array)
    #print(ws.get_edge_weight_map())



if __name__ == '__main__':
    run("../../data/lung-healthy.png")