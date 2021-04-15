# -*- coding: utf-8 -*-
import numpy as np
import random as r
import sys 
import matplotlib.pyplot as plt

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
        sections[i][0] = i
        sections[i][1] = i+1

    return nodes, sections


def plot_geo(x_range, nodes):
    plt.plot(x_range[0],0,'*') #x_range[0]
    plt.plot(x_range[1],0,'*') #x_range[1]
    plt.plot(x_range,[0,0])
    plt.plot(nodes,np.zeros(len(nodes)),'*')
    
    plt.xlim([x_range[0]-0.3,x_range[1]+0.3])
    plt.ylim([-0.2,0.2])


#1a
x_range, conditions, types = init_param([0,1,-1,3,'N','D'])
print('x range', x_range)
print('conditions', conditions)
print('types', types)
#1b
nodes, sections = generate_geo(x_range)
print('nodes', nodes)
print('sections', sections)
#1c
plot_geo(x_range, nodes)

