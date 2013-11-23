'''
Created on Nov 9, 2013

@author: Scott
'''

import numpy, Image, watershed_mapping, watershed_merge

def get_array(filename):
    im = Image.open(filename)
    original_array = numpy.array(im)
    
    return original_array


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
        #indicate something bad happened here
        return array


'''
Writes the given array to the file (as an image) -- PNG
'''    
def write_image(array, filename):
    image_array = numpy.ndarray(shape=(len(array),len(array[0]),3), dtype='uint8', order='F')

    for x in range(0, len(image_array)):
        for y in range(0, len(image_array[0])):
            image_array[x][y][0] = array[x][y]
            image_array[x][y][1] = array[x][y]
            image_array[x][y][2] = array[x][y]
    
    im = Image.fromarray(image_array)
    im.save(filename)
        

def build_watershed_array(index_map, x_max, y_max):
    
    ws_arr = numpy.ndarray(shape=(x_max,y_max,1), dtype='int', order='F')
    
    for x in range(0, x_max):
        for y in range(0, y_max):
            ws_arr[x][y] = len(index_map[(x,y)])
            
    return ws_arr

def outline_array(array):
    image_array = numpy.ndarray(shape=(len(array),len(array[0]),1), dtype='uint8', order='F')

    for x in range(0, len(array)):
        for y in range(0, len(array[0])):
            
            if array[x][y] > 1:
                image_array[x][y] = 0
            else:
                image_array[x][y] = 255
            
    return image_array
    


def run_merge_analysis(filename):
    
    merge_step = 200
    
    pix_arr = (greyscale(get_array(filename)))
    
    x_max = len(pix_arr)
    y_max = len(pix_arr[0])
    
    index_map = watershed_mapping.build_index_map(pix_arr)
    
    
    
    merge_limit = merge_step
    
    
    #while(merge_limit <= 255):
    index_map = watershed_merge.merge(index_map, merge_limit)
    write_image(outline_array(build_watershed_array(index_map, x_max, y_max)), filename[:-3] + str(merge_limit) + ".png")

   
        #merge_limit += merge_step
    return