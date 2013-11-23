'''
Created on Nov 18, 2013

@author: Scott
'''

class Watershed(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.points = set()
        
        
    def merge(self, watershed):
        self.points.update(watershed.points)
        
    def is_in_watershed(self, location):
        return location in self.points
    
    def intersection(self, watershed):
        return self.points - watershed
    
    def add_point(self, location):
        self.points.add(location)
        
    def __len__(self):
        return len(self.points)