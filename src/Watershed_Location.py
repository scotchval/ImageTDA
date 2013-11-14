'''
Created on Nov 9, 2013

@author: Scott Valentine
'''

class Watershed_Location(object):
    
    '''
    Represents the watersheds for a give point
    '''

    def __init__(self, location):
        '''
        Constructor
        '''
        self.location = location
        self.index_map = dict()
        self.intersections = 0
        
        
    '''
    Add the watershed with the relaitve height of the watershed to this point
    '''
    def add_watershed(self, index, relative_height):
        self.index_map[index] = relative_height
        self.intersections +=1
        
    '''
    Is this point in the inidcated watershed
    '''
    def is_in_watershed(self, ws_index):
        return self.index_map.has_key(ws_index)
    
    def visited(self):
        return len(self.index_map) != 0
    
    def intersection_size(self):
        return self.intersections
    
    
    '''
    Merges the watershed of this point with the new watershed
    '''
    def merge_watershed(self, ws_old, ws_new, relative_height_diff):
        old_height = self.index_map[ws_old]
        
        self.index_map.pop(ws_old, None)
        
        new_height = relative_height_diff + old_height
        
        self.index_map[ws_new] = new_height
        
    '''
    String representation.
    '''
    def __repr__(self):
        return str(self.index_map)
        