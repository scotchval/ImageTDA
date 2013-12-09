'''
Created on Dec 3, 2013

@author: Scott
'''

import struct

'''
Functions used for writing a spares matrix to a file. edge_map specifies the sparse matrix.
Filename specifies the file to write to.

writes the file with watershed 1 (4 bytes) watershed 2 (4 bytes) distance between (4 bytes).

'''
def writeSparseMatrix(filename, edge_map):
    
    f = open(filename, "wb")
    
    for key in edge_map:
        f.write(struct.pack('i', key[0]))
        f.write(struct.pack('i', key[1]))
        f.write(struct.pack('i', edge_map[key]))
    
    f.close()
    
    return 0