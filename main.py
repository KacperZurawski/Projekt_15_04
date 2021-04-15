# -*- coding: utf-8 -*-
import numpy as np
import random as r

#globalne
"""
wezly = np.array(0,1,0.5,0.75)

elementy = np.array([[1, 3],
                     [4, 2],
                     [3, 4]])
#warunki brzegowe
twb_L = 'D'
twb_R = 'D'

wwb_L = 0
wwb_R = 1
"""

def init_param(x_start, x_stop, node_num):
    nodes = np.zeros(node_num)
    sections = np.zeros((node_num, 2))
    
    nodes[0] = 0
    for i in range(1,node_num):
        value = round(r.uniform(x_start, x_stop),2)
        nodes[i] = value
    return nodes, sections
    
    
#1a

#1b
print(init_param(0,1,4))
