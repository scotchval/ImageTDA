'''
Created on Dec 6, 2013

@author: Scott

Fuctions that map an image array to another array.
These either take [m X n X 3] or [m X n] arrays
'''
import numpy, math
'''
Maps each pixel (r,b,g) -> ((g + b)**2 - 4*r**2 + 250000)/(2000)
'''
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


'''
Inverts all of the values of a greyscale array (2D)
'''
def inverse(array):
    for x in range(0, len(array)):
        for y in range(0,len(array[0])):
            array[x][y] = 255 - array[x][y]
    return array

'''
Transforms a color image (m X n X 3) to a greyscale image (m X n)
'''
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

'''
Turns the passed array to a greyscale image. This can take in either color
or greyscale images
'''
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
Maps the given m X n array to the gradient for each point. The gradient is appoximated by
taking the values of the neighbors of the point.
'''
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