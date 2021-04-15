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
    
    val = (x_range[1]-x_range[0])/(nodes_num-1)
    nodes = np.array([x_range[0]])
    
    for i in range(1,nodes_num):
        nodes = np.block([nodes, i * val + x_range[0]])
    for i in range(1,nodes_num-1):
        nodes[i] = nodes[i] + round(r.uniform(-0.05, 0.05),2)
        
    
    sections = np.zeros((nodes_num-1,2))


    for i in range(0, nodes_num-1, 1):
        sections[i][0] = nodes[i]
        sections[i][1] = nodes[i+1]

    return nodes, sections
#1a
x_range, conditions, types = init_param([0,1,-1,3,'N','D'])
print('x range', x_range)
print('conditions', conditions)
print('types', types)

#1b

nodes, sections = generate_geo(x_range)
print('nodes', nodes)
print('sections', sections)

"""
def GenerujTabliceGeometrii(x_0,x_p,n):

    val = (x_p-x_0)/(n-1)
    tablica1 = np.array([x_0])

    for indeks_tab1 in range(1,n,1):
        tablica1 = np.block([tablica1, indeks_tab1 * val + x_0])

    tablica2 = np.zeros((n-1,2))

    for indeks_tab2 in range(0, n-1, 1):
        tablica2[indeks_tab2][0] = tablica1[indeks_tab2]
        tablica2[indeks_tab2][1] = tablica1[indeks_tab2+1]


    return indeks_tab1,tablica1,tablica2
"""

