'''
Created on Nov 24, 2013

@author: sdv4
'''

'''
Merges ws1 into ws2 runs in O(|ws1|)

not that a merge turns it into a new watershed that keeps the min
distance of both - this is to keep this consistent with the
persistence diagram

note that this does not take into account changes in edge weights

'''
def merge_watersheds_at_limit(edge_merges, watersheds, limit):
    
    edge_map = watersheds.get_edge_weight_map()
    
    edge_weights = sorted(edge_map.keys(), key = lambda t: edge_map[t])
    
    if len(edge_weights) == 0:
        return
    current = edge_weights.pop(0)
    
    merges = 0
    
    while edge_map[current] <= limit and len(edge_weights) > 0:
        merges +=1
        merge_watershed(edge_merges, current[0], current[1])
        current = edge_weights.pop(0)    
    print("merges: " + str(len(edge_merges)))
    return edge_merges



def merge_watershed( edge_map, ws1, ws2):
        node1 = Node(ws1)
        a = ws1 in edge_map
        b = ws2 in edge_map
        
        if a and not b:
            node = Node(ws2)
            merge_nodes(node, edge_map[ws1])
            edge_map[ws2] =node
        elif b and not a:
            node = Node(ws1)
            merge_nodes(node, edge_map[ws2])
            edge_map[ws1] =  node
        elif not b and not a:
            node1 = Node(ws1)
            node2 = Node(ws2)
            merge_nodes(node1,node2)
            edge_map[ws1] = node1
            edge_map[ws2] = node2
        else:
            merge_nodes(edge_map[ws2],edge_map[ws1])
    


def merge_nodes(node1, node2):
    parent1 = node1.get_root()
    parent2 = node2.get_root()
    parent2.parent = parent1
     
    
class Node(object):
    def __init__(self, val):
        self.parent = self
        self.value = val
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.value == self.value
        return False
        
    
    def get_root(self):
        res = self.parent
        while res != res.parent:
            res = res.parent
            self.parent =res
        return res
        
    