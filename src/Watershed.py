'''
Created on Oct 31, 2013

@author: Scott
'''
import numpy
import Image

WATERFALL_THRESHOLD = 10

global landscape
global watershed_indices
global relative_heights


def sort_pixels(pixels):
    
    pix_list = []
    
    
    for x in range(0,len(pixels)):
        for y in range(0, len(pixels[0])):
            pix_list.append((x,y,pixels[x][y]))
    pix_list.sort(key=lambda tup: tup[2])
    return pix_list
    
    
    
def is_valid_location(x,y,array):
    res = x >=0 and y >=0
    res = res and x < len(array) and y < len(array[0])
    return res
    
    

def map_cachement_basin(current_locale, frontier, count, initial_height):
    
    global landscape
    global watershed_indices
    global relative_heights
    
    # if it is greater than 0, we have already visited this location
    if watershed_indices[current_locale[0]][current_locale[1]] >= 0:
        return
    
    watershed_indices[current_locale[0]][current_locale[1]] = count;
    
    current_height = landscape[current_locale[0]][current_locale[1]]
    
    print(str(current_height) + " " + str( initial_height))
    
    relative_heights[current_locale[0]][current_locale[1]] = current_height - initial_height
        
    for i in range(-1,2):
        for j in range(-1,2):
            if(i!= 0 or j !=0) and is_valid_location(current_locale[0] + i, current_locale[1] + j, landscape):
                
                x = current_locale[0] + i
                y = current_locale[1] + j
                
                next_height = landscape[x][y]
                
                if next_height >= current_height:                    
                    frontier.append((x,y))
                    
                #elif current_height - initial_height < WATERFALL_THRESHOLD:     
                    
                         
    return

def initial_watershed(pix):
    res = numpy.ndarray(shape=(len(pix),len(pix[0]),1), dtype='uint8', order='F')
    return res;    
    

def construct_watersheds(filename):
    global watershed_indices
    global landscape
    global relative_heights
    
    
    
    pix=numpy.array(Image.open(filename))
    
    landscape= greyscale(pix)
    
    
    sorted_pix = sort_pixels(landscape)
    
    watershed_indices = numpy.ndarray(shape=(len(pix),len(pix[0]),1), dtype='int', order='F')
    relative_heights = numpy.ndarray(shape=(len(pix),len(pix[0]),1), dtype='int', order='F')
    
    for x in range(0, len(watershed_indices)):
        for y in range(0, len(watershed_indices[0])):
            watershed_indices[x][y] = -1
    
    
    count = 0
    while(len(sorted_pix) > 0):
        start_point = sorted_pix.pop()
          
          
        if watershed_indices[start_point[0]][start_point[1]] < 0:
            
            queue =[]
            queue.append(start_point)
            
            initial_height = start_point[2]
        
            while(len(queue) != 0):
                map_cachement_basin(queue.pop(0), queue, count, initial_height)
            count +=1
        
    print(str(count))
    

        
    
    
    watershed_array = get_watershed_image()
    for x in range(0, len(relative_heights)):
        sti = ""
        
        for y in range(0, len(relative_heights[0])):
            sti += str(relative_heights[x][y][0])
        print(sti)
    
    return watershed_array


def is_border(x,y,image):
    global watershed_indices
    
    res = False
    
    
    for i in range(-1,2):
        for j in range(-1,2):
            
            if (i !=0 or j !=0) and is_valid_location(x+i,y+j,watershed_indices):

                if watershed_indices[x][y] != watershed_indices[x+i][y+j]:       
                    return True

    return res

    
    

def get_watershed_image():
    global watershed_indices
    image = numpy.ndarray(shape=(len(watershed_indices),len(watershed_indices[0]),1), dtype='uint8', order='F')
    for x in range(0, len(image)):
        for y in range(0, len(image[0])):
            image[x][y] = 255

    for x in range(0, len(image)):
        for y in range(0, len(image[0])):
            if is_border(x,y,image):
                image[x][y] = 0



    return image

def write_array_to_image(array, filename):
    image_matrix = numpy.ndarray(shape=(len(array),len(array[0]),3), dtype='uint8', order='F')
    
    
    for x in range(0,len(array)):
        for y in range(0, len(array[0])):
            image_matrix[x][y][0] = array[x][y]
            image_matrix[x][y][1] = array[x][y]
            image_matrix[x][y][2] = array[x][y]
    
    im = Image.fromarray(image_matrix)
    im.save(filename)
    

def greyscale(array):
    grey = numpy.ndarray(shape=(len(array),len(array[0]),1), dtype='int', order='F')
    
    for x in range(0,len(array)):
        for y in range(0,len(array[0])):
            
            
            
                num_channels = len(array[0][0])
            
                grey_val = 0
            
                for channel in range(0,min(3,len(array[0][0]))):
                    grey_val += array[x][y][channel]/num_channels
                grey[x][y][0] = grey_val
    return grey

if __name__ == '__main__':
    name = "ellen"

    arr = construct_watersheds(name + ".png")
    
    
    write_array_to_image(arr, name + "-watershed.png")
        