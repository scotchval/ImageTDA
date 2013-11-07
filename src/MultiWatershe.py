'''
Created on Nov 4, 2013

@author: Scott
'''
import Image
import numpy

def sort_pixels(pixels):
    
    pix_list = []
    
    
    for x in range(0,len(pixels)):
        for y in range(0, len(pixels[0])):
            pix_list.append((x,y,pixels[x][y]))
    pix_list.sort(key=lambda tup: tup[2])
    return pix_list

def is_valid_move(dx,dy,location,landscape):
    
    x = dx + location[0]
    y = dy + location[1]
     
    not_zero = x != 0 or y != 0
    
    x_in_bound = x >= 0 and x < len(landscape)
    y_in_bound = y >=0 and y < len(landscape[0])
    
    
    return not_zero and x_in_bound and y_in_bound

def map_watershed(landscape, location, index_map, index, frontier):
        
    
    if index_map.has_key(location) and index not in index_map[location]:
        index_list = index_map[location]
        index_list.add(index)
    elif index_map.has_key(location):
        return
    else:
        value = set()
        value.add(index)
        index_map[location] = value
    
    for i in range(-1,2):
        for j in range(-1,2):
            if is_valid_move(i,j,location,landscape):
                current_height = landscape[location[0]][location[1]]
                next_height = landscape[location[0] + i][location[1] + j]
                
                if current_height<= next_height:
                    frontier.append((location[0] + i, location[1] + j))
    return

def build_full_watershed(grey_array):
    
    index_map = dict()
    
    
    sorted_points = sort_pixels(grey_array)
    
    shed_index = 0
    
    while len(sorted_points) > 0:
        frontier = []
        next_point = sorted_points.pop(0)
        frontier.append(next_point)
        
        while len(frontier) > 0:
            map_watershed(grey_array, next_point, index_map, shed_index, frontier)
        shed_index +=1
    return index_map






def write_array_to_image(array, filename):
    image_matrix = numpy.ndarray(shape=(len(array),len(array[0]),3), dtype='uint8', order='F')
    
    
    for x in range(0,len(array)):
        for y in range(0, len(array[0])):
            image_matrix[x][y][0] = array[x][y]
            image_matrix[x][y][1] = array[x][y]
            image_matrix[x][y][2] = array[x][y]
    
    im = Image.fromarray(image_matrix)
    im.save(filename)

def color_to_grey(array):
    dimensions = array.shape
    grey_image = numpy.ndarray(shape=(dimensions[0], dimensions[1]), dtype='uint8', order='F')
    
    for x in range(0, len(array)):
        for y in range(0,len(array[0])):
            channel_count = len(array[0][0])
            grey = 0
            for c in range(0,channel_count):
                grey += array[x][y][c] / channel_count
            grey_image[x][y] = grey
    return grey_image
    
    

def greyscale(array):
    
    dimensions = array.shape
    
    if len(dimensions) == 2:
        #no need to do anything here
        return array
    if len(dimensions) == 3:
        return color_to_grey(array)
    
    else: 
        # something bad happened
    
    
        return array



def watershed(filename):
    im = Image.open(filename)
    original_array = numpy.array(im)
    index_map = build_full_watershed(greyscale(original_array))
    print(index_map)


if __name__ == '__main__':
    watershed("man.png")