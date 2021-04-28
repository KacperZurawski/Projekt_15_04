# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:38:26 2021

@author: Kot
"""
import numpy as np
def AutomaticGeo(a,b,n):
    lp = np.arange(1,n+1)
    x = np.linspace(a,b,n)
    
    nodes = (np.vstack((lp.T,x.T))).T
    
    lp = np.arange(1,n)
    c1 = np.arange(1,n)
    c2 = np.arange(2,n+1)
    
    sections = (np.block([[lp],[c1],[c2]])).T
    EV = [{"ind":1,"type":'D',"val":1},
          {"ind":2,"type":'D',"val":2}]
    return nodes, sections, EV
    