# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 12:27:56 2021

@author: Kot
"""

import numpy as np

def ManualGeo():
    
    nodes = np.array([[1,0],
                      [2,1],
                      [3,0.5],
                      [4,0.75]])
    
    sections = np.array([[1,1,3],
                         [2,4,2],
                         [3,3,4]])
    
    EV = [{"ind":1,"type":'D',"val":1},
          {"ind":2,"type":'D',"val":2}]
    
    return nodes, sections, EV