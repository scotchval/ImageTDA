'''
Created on Nov 20, 2013

@author: Scott
'''


import watershed_mapping, utils.Resize as utils


class Edge(object):
    

    def __init__(self, vertA, weightA, vertB, weightB):
        self.vertA = vertA
        self.vertB = vertB
        self.weight = weightA + weightB
        self.open = False

    def open(self):
        self.open = True;
        
    



def build_graph(filename):
    
    landscape = utils.color_to_grey(utils.get_array(filename))
    
    index_map = watershed_mapping.build_index_map(landscape)
    
    height = len(landscape);
    width = len(landscape[0]);




if __name__ == '__main__':
    build_graph("../data/lung-healthy.png")