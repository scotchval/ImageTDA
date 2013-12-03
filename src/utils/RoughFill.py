'''
Created on Dec 2, 2013

@author: Scott
'''
import utils.Utils as util

def valid(i,j,x,y,array):
    
    x_range = x+i >= 0 and x +i < len(array)
    y_range = y+j >= 0 and y + j < len(array[0])
    
    return x_range and y_range

def fill(array):
    tt = 3
    
    for x in range(0, len(array) /tt):
        for y in range(0, len(array)/tt):
            
            count = 0
            black = 0
            
            for i  in range(-1, 2):
                for j in range(-1,2):
                    if(valid(i,j,tt*x,tt*y,array)):
                        count +=1
                        if array[tt*x+i][tt*y+j] ==0:
                            black +=1
            if black*4 >= count:
                for i  in range(-1, 2):
                    for j in range(-1,2):
                        if(valid(i,j,tt*x,tt*y,array)):
                            array[tt*x+i][tt*y+j] = 0
                            '''else:
                for i  in range(-1, 2):
                    for j in range(-1,2):
                        if(valid(i,j,3*x,3*y,array)):
                            array[3*x+i][3*y+j] = 255 '''
    
    return array
    

if __name__ == '__main__':
    
    
    
    filename = "../../data/class_notes-gradient-530.png"
    writeFileName = "../../data/class_notes-gradient-530-FILL.png"
    
    util.write_image(fill(util.greyscale(util.get_array(filename))), writeFileName);