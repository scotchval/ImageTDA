'''

Maps out a watershed based on which watershed a point is in and the relative height of that point in the water shed.

Created on Nov 9, 2013

@author: Scott
'''


'''

Returns 3-D tuple
'''
def sort_pixels(pixels):   
    pix_list = []
    for x in range(0,len(pixels)):
        for y in range(0, len(pixels[0])):
            pix_list.append((x,y,pixels[x][y]))
    pix_list.sort(key=lambda tup: tup[2])
    return pix_list


'''
Initializes the watershde_index map
'''
def build_watershed_index_map(pixels):
    
    index_map = dict()
    
    for x in range(0,len(pixels)):
        for y in range(0, len(pixels[0])):
            index_map[(x,y)] = dict()
    return index_map
    
    
'''
 Is the move specified by the change in x (dx) and y (dy) still located in the landscape?
'''
def is_valid_move(dx,dy,location,landscape):
    
    x = dx + location[0]
    y = dy + location[1]
     
    not_zero = dx != 0 or dy != 0
    
    x_in_bound = x >= 0 and x < len(landscape)
    y_in_bound = y >=0 and y < len(landscape[0])
    
    return not_zero and x_in_bound and y_in_bound
    
'''
Map this pixel to the watershed and add any other neighbor pixels to visit.
'''
def map_watershed(current, landscape, index_map, frontier, visited, index, local_min):
    
    if index in index_map[current]:
        return
    
    relative_height = landscape[current[0]][current[1]] - local_min
    
    
    index_map[current][index] = relative_height
    
    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx != dy or dx != -1*dy:  
                next_point = (current[0] + dx, current[1] + dy)
                
                if next_point not in visited:
                
                    if is_valid_move(dx, dy, current, landscape) and landscape[next_point[0]][next_point[1]] >= landscape[current[0]][current[1]]:
                        frontier.append((next_point))
    return
    
'''
Builds the full index_map for the landscape (relative height and watershed index).
'''
def build_index_map(landscape):
    sorted_pixels = sort_pixels(landscape)
    watershed_locations = build_watershed_index_map(landscape)
    
    size = len(sorted_pixels)
    
    
    frontier = []
    
    index = 0
    count = 0;
    
    while len(sorted_pixels) > 0:
        print(str(index) + " c:" + str(count))

        local_min = sorted_pixels.pop(0)
        
        while len(sorted_pixels) > 0 and local_min[0:2] not in watershed_locations:
            local_min = sorted_pixels.pop(0)
        
        if len(sorted_pixels) == 0:
            break
        
        # forget about the last value.
        frontier.append(local_min[:2])
        visited = set()
        while len(frontier) > 0:
            next_point = frontier.pop(0)
            visited.add(next_point)
            count +=1;
            map_watershed(next_point, landscape, watershed_locations, frontier,visited, index, landscape[local_min[0]][local_min[1]])
        index +=1
        
        
    return watershed_locations