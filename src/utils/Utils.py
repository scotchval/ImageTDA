'''
Created on Nov 22, 2013

@author: Scott
'''

import numpy, Image, math

def get_array(filename):
    im = Image.open(filename)
    original_array = numpy.array(im)
    
    return original_array

def inverse(array):
    for x in range(0, len(array)):
        for y in range(0,len(array[0])):
            array[x][y] = 255 - array[x][y]
    return array


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
    
def get_gradient(array):
    
    gradient = numpy.ndarray(shape=(len(array), len(array[0])), dtype='uint', order='F')
    
    for x in range(0, len(array)):
        for y in range(0, len(array[0])):
            gradient[x][y] = gradient_at_point(x,y, array) 
    return gradient        
    
def in_bounds(x, y, array):
    
    x_in = x >=0 and x < len(array)
    y_in = y >=0 and y < len(array[0])
    
    
    return x_in and y_in    

def gradient_at_point(x, y, array):
    
    dx1 = x -1 
    if not in_bounds(dx1, y, array):
        dx1 = x
    
    
    dx2 = x +1
    if not in_bounds(dx2, y, array):
        dx2 = x
    
    gradient_x = (int(array[dx1][y]) - int(array[dx2][y]))**2
    
    dy1 = y -1 
    if not in_bounds(x, dy1, array):
        dy1 = y
    
    
    dy2 = y +1
    if not in_bounds(x, dy2, array):
        dy2 = y
    
    gradient_y = math.sqrt((int(array[x][dy1]))**2+ (int(array[x][dy2]))**2)
    
    
    
    return gradient_x + gradient_y
    