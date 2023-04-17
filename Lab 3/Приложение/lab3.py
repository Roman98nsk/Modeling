import graphviz 
from collections import deque 
from math import ceil 
import random 
  
class Node: 
    def __init__(self, value): 
        self.value = value 
        self.children = [] 
  
    def add_child(self, child): 
        self.children.append(child) 
  
    def to_graphviz(self): 
        graph = graphviz.Digraph() 
        self._add_nodes(graph) 
        return graph 
  
    def _add_nodes(self, graph): 
        graph.node(str(id(self)), str(self.value)) 
        for child in self.children: 
            graph.edge(str(id(self)), str(id(child))) 
            child._add_nodes(graph) 
  
def build_tree(depth, width): 
    width -= 1 
    if depth <= 0 or width <= 0: 
        raise ValueError("Depth and width must be positive integers") 

    root = Node(0) 
  
    current_depth = 0 
    current_width = [[] for _ in range(depth)] 
    counter = 1 
    parent = root 
    while current_depth < depth: 
        node = Node(counter) 
        parent.add_child(node) 
        counter += 1 
        parent = node 
        current_depth += 1 
    flag = False 
    while not flag: 
        for i in current_width: 
            if len(i) == width: 
                flag = True 
                break 
            r = random.random() 
            idx_a = (1 / (depth)) 
            idx = 0 
            while idx_a < r: 
                idx += 1 
 
                r -= idx_a 
            current_width[idx].append(counter) 
            parent = root 
            for _ in range(idx): 
                parent = parent.children[0] 
            parent.add_child(Node(counter)) 
            print(idx) 
            counter += 1 
    print(current_width) 
    return root 
  
depth = 2
width = 3 
  
root = build_tree(depth, width) 
graph = root.to_graphviz() 
graph.render('tree')