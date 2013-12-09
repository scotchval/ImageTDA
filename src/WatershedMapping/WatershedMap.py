'''
Created on Nov 21, 2013

@author: sdv4
'''

import numpy

class WatershedMap(object):
    '''
    Maps the locations of all watersheds in an image. Provides a quick (relative)
    way to map out watersheds and access the calculate data.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.location_to_sheds = dict()
        self.shed_to_location = dict()
       
       
    '''
    Adds a point to the location_2_sheds and shed_2_location with corresponding data.
    '''
    def add_point(self, point, watershed, relative_height):
        if point in self.location_to_sheds: 
            self.location_to_sheds[point].update({watershed: relative_height})
        else:
            self.location_to_sheds[point] = {watershed: relative_height}
            
        if watershed in self.shed_to_location:
            self.shed_to_location[watershed].append(point)
        else:
            self.shed_to_location[watershed] = [point]

            
    def watershed_count(self):
        return len(self.shed_to_location)
            
            
    '''
    Builds a map of adjacent watersheds and the "distance" (calculated by the metric) between them
    '''
    def get_edge_weight_map(self, metric):
        
        # map of edges (pair of watersheds) to the weight of the edge
        edge_map = dict()
        
        for location in self.location_to_sheds:
            # this is the condition for an edge.
            if len(self.location_to_sheds[location]) > 1:
                pairs = get_all_possible_pairs(self.location_to_sheds[location].keys())                
                for pair in pairs:
                    
                    edge_weight = metric(self.location_to_sheds[location][pair[0]], self.location_to_sheds[location][pair[1]])
                    
                    if pair not in edge_map:
                        pair = pair[::-1]
                    if pair in edge_map:
                        
                        if edge_map[pair] > edge_weight:
                            edge_map[pair] = edge_weight
                        
                    else:
                        edge_map[pair] = edge_weight
        print("edges: " + str(len(edge_map)))
        return edge_map
    
    def are_identical_watersheds(self, subshed, supershed):

        if subshed not in self.location_to_sheds or supershed not in self.location_to_sheds:
            return False
        
        if len(self.location_to_sheds[subshed]) == 0 or len(self.location_to_sheds[supershed]) ==0:
            return False

        keys1 = self.location_to_sheds[subshed].keys()
        keys2 = self.location_to_sheds[supershed].keys()
        
        for shed in keys1:
            if shed not in keys2:
                return False
        return True
        

        
    def get_watershed_set(self, point):
        
        watersheds = set()
        
        for ws in self.location_to_sheds[point]:
            watersheds.update(ws[0])
        return watersheds
        
    
    '''
    Builds an image of all the watershed by marking watershed intersection with black
    and everything else with white.
    '''
    def get_watershed_picture(self, edge_tree, dimX, dimY):
        pic = numpy.ndarray(shape=(dimX, dimY,3), dtype='uint8', order='F')
        
        self.edge_merges(edge_tree, dimX, dimY)
        
        
        for x in range(0,dimX):
            for y in range(0,dimY):
                if len(self.location_to_sheds[(x,y)]) > 1:
                    pic[x][y][0] = 0
                    pic[x][y][1] = 0
                    pic[x][y][2] = 0
                else:
                    pic[x][y][0] = 255
                    pic[x][y][1] = 255
                    pic[x][y][2] = 255
        return pic
        

    
    def edge_merges(self, edge_tree,dimX, dimY):
        for x in range(0, dimX):
            for y in range(0, dimY):
                watersheds = self.location_to_sheds[(x,y)]
                to_be_removed = []
                to_be_added = []
                for ws in watersheds:
                    if ws in edge_tree:
                        orig_val = watersheds[ws]
                        to_be_removed.append(ws)
                        
                        to_be_added.append((edge_tree[ws].get_root().value, orig_val))
                for shed in to_be_removed:
                    watersheds.pop(shed)
                for shed in to_be_added:
                    watersheds[shed[0]] = shed[1]
                
                
    
'''
Gives all the possible pairs of elements of a list.
'''
def get_all_possible_pairs(vals):
    
    pairs = []
    
    for i in range(0, len(vals)):
        for j in range(i+1, len(vals)):
            pairs.append((vals[i],vals[j]))
    return pairs
    
    
    