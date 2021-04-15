# -*- coding: utf-8 -*-
import numpy as np
import random as r
import sys 

def init_param(array):
    
    if(array == 0):
        print('Write array of x_range, conditions, types')
        array = input()
    
    x_range = np.array([array[0], array[1]])
    conditions = np.array([array[2], array[3]])
    types = np.array([array[4], array[5]])
    return x_range, conditions, types


def generate_geo(x_range):
    print('Write number of nodes')
    nodes_num = int(input())
    
    nodes = np.linspace(x_range[0], x_range[1], nodes_num)
    print(nodes)
    
    return nodes
#1a
x_range, conditions, types = init_param([0,1,-1,3,'N','D'])
print('x range', x_range)
print('conditions', conditions)
print('types', types)

#1b

nodes = generate_geo(x_range)


