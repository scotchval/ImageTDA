'''
Created on Nov 18, 2013

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

'''
Assumes factor is int
'''
def resize_image(filename, factor):
    
    im_arr = get_array(filename)
    
    resized_arr =  numpy.ndarray(shape=(len(im_arr)*factor, len(im_arr[0])*factor,3), dtype='uint8', order='F')
    for x in range(0,len(im_arr)):
        for y in range(0, len(im_arr[0])):
            y_off = y*factor
            x_off = x*factor
            for offx in range(0,factor):
                for offy in range(0, factor):
                    resized_arr[x_off + offx][y_off + offy][0] = im_arr[x][y][0]
                    resized_arr[x_off + offx][y_off + offy][1] = im_arr[x][y][1]
                    resized_arr[x_off + offx][y_off + offy][2] = im_arr[x][y][2]
    
    write_image(resized_arr,filename[:-4] + "resized.png")
    



if __name__ == '__main__':
    filename = "../../data/man.png"
    resize_image(filename, 10)
    
    