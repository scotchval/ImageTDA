'''
Created on Nov 22, 2013

@author: Scott
'''

import numpy, Image

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


def write_image(array, filename):
    
    im = Image.fromarray(array)
    im.save(filename)