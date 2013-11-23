'''
Created on Nov 18, 2013

@author: Scott
'''
import numpy
import utils.Utils as utils




'''
Assumes factor is int
'''
def resize_image(filename, factor):
    
    im_arr = utils.get_array(filename)
    
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
    
    utils.write_image(resized_arr,filename[:-4] + "resized.png")
    



if __name__ == '__main__':
    filename = "../../data/man.png"
    resize_image(filename, 10)
    
    