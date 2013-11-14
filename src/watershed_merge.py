'''
Created on Nov 9, 2013

@author: Scott
'''

import operator

def sort_peaks(index_map):
    
    
    intersections = sorted(index_map, key= lambda (k,v): index_map[(k,v)].intersection_size(), reverse=True)
    
    #print(intersections)
    
    return intersections

def merge(index_map, merge_height):
    
    sorted_points = sort_peaks(index_map)
    return sorted_points