'''
Created on Dec 3, 2013

@author: Scott
'''

import WatershedMapping.WatershedMap
import struct

def writeSparseMatrix(watershed_map, filename):
    edge_map = watershed_map.get_edge_weight_map()
    
    file = open(filename, "wb")
    
    a = True
    
    for key in edge_map:
        
        if(a):
            print(str(key[0]) + " " + str(key[1]) + " " + str(edge_map[key]) + " " + '.')
            a= False
        
        
        file.write(struct.pack('i', key[0]))
        file.write(struct.pack('i', key[1]))
        file.write(struct.pack('i', edge_map[key]))
    
    file.close()
    
    return 0


def readTest(filename):
    file = open(filename,'r')
    
    a = struct.unpack('i', file.read(4))
    b = struct.unpack('i', file.read(4))
    d = struct.unpack('i', file.read(4))
    
    print(str(a))
    print(str(b))
    print(str(d))
    

def writeDistanceMatrix(watershed_map):
    
    
    
    return 0