'''
Created on Nov 9, 2013

@author: Scott
'''


def sort_peaks(index_map):
    
    
    peakVals = []
    
    for key in sorted(index_map.iterkeys()):
        peakVals.append((key[0], key[1], len(index_map[key])))
        
    
    intersections = sorted(peakVals, key= lambda k: k[2], reverse=True)
    return intersections



def merge(index_map, merge_height):
        
    sorted_points = sort_peaks(index_map)
    
    
    
    current_point = sorted_points.pop(0)
    while len(sorted_points) > 0 and current_point[2] > 1:
        
        watersheds = index_map[current_point[:2]]
        
        keys = watersheds.keys()
        
        for a in keys:
            for b in keys:
                if a in watersheds and b in watersheds and a != b and watersheds[a] -merge_height+ watersheds[b] <= 0:
                    
                    small = a
                    big = b
                    
                    if max(watersheds[a], watersheds[b]) == watersheds[a]:
                        small = b
                        big = a
                        
                    
                    merge_at_point(current_point[:2], index_map, small, big)
                
        current_point = sorted_points.pop(0)
        
    return index_map


'''
Merges the two watesheds that meet at a specified point.
'''
def merge_at_point(point, index_map, watershed_from, watershed_to):
    watershed = index_map[point]
    
    new_height = watershed[watershed_to]
    
    queue = set([])
    queue.add(point)
    
    while len(queue) > 0:
        walk_watershed(queue.pop(), watershed_from, watershed_to, new_height, queue, index_map)
        
    
    
'''
Walks the watershed_from chaging its value to watershed_to
Part of merging
Updates index_map
'''
def walk_watershed(point, watershed_from, watershed_to, new_height, queue, index_map):
    
    
    index_map[point].pop(watershed_from, None)
    index_map[point][watershed_to] = new_height
    
    
    for i in range(-1,2):
        for j in range(-1,2):
            next_point = (point[0] +i, point[1] + j)
            if next_point in index_map and watershed_from in index_map[next_point]:
                queue.add(next_point)
    return
    