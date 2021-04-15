# -*- coding: utf-8 -*-
import numpy as np
import random as r


def init_param(x_start, x_stop, node_num):
    section_num = node_num - 1
    nodes = np.zeros(node_num)
    sections = np.zeros((section_num, 2))
    
    nodes[0] = 0
    for i in range(1,node_num):
        value = round(r.uniform(x_start, x_stop),2)
        nodes[i] = value
        
    for i in range(0,section_num):
        values = r.sample(range(0,node_num), 2)
        sections[i] = values
    return nodes, sections
    
    
#1a

#1b
nodes, sections = init_param(0,1,4)
print(nodes)
print(sections)
