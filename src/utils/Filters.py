'''
Created on Dec 2, 2013

@author: Scott
'''
import numpy


def green_blue_filter(color_array):
    filtered = numpy.ndarray(shape=(len(color_array), len(color_array[0])), dtype='uint8', order='F')
    
    for x in range(0, len(color_array)):
        for y in range(0, len(color_array[0])):
            filtered[x][y] = apply_filter(color_array[x][y])
            
    return filtered


def apply_filter(color_tuple):
    r = int(color_tuple[0])
    g = int(color_tuple[1])
    b = int(color_tuple[2])
    
    val = ((g + b)**2 - 4*r**2 + 250000)/(2000)
    return val