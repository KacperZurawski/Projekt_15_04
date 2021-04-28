# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:13:45 2021

@author: Kot
"""
import matplotlib.pyplot as plt
import numpy as np

def PlotGeo(nodes, sections, ev):
    
    figure = plt.figure(1)
    nodesNum = np.shape(nodes)[0]
    sectionsNum = np.shape(sections)[0]
    
    plt.plot(nodes[:,1], np.zeros((nodesNum,1)),'-b')
    
    for node in np.arange(0, nodesNum):
        
        index = nodes[node,0]
        pos_x = nodes[node,1]
        
        plt.text(pos_x, 0.01, str(round(index,2)), c="b")
        plt.text(pos_x, -0.01, str(round(pos_x,2)))
        
    for section in np.arange(0, sectionsNum):
        
       leftNode = sections[section,1]
       rightNode = sections[section,2]
       
       pos_x = (nodes[leftNode-1,1] + nodes[rightNode-1,1])/2
       
       plt.text(pos_x, 0.01, str(section+1), c = "r")
       
    plt.show()
    return figure