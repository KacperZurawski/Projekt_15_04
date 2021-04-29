# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as plt


from ManualGeo import *
from AutomaticGeo import *
from PrintGeo import *
from MemoryAllocation import *
from BaseFun import *

if __name__ == '__main__':
    c = 0
    f = lambda x: 1
    
    x_a = 0
    x_b = 1
    n = 6
    #nodes, sections, ev  = ManualGeo();
    #n = np.shape(nodes)[0]
    nodes, sections, ev = AutomaticGeo(x_a,x_b,n)
    PlotGeo(nodes, sections, ev)
    A,B = MemoryAllocation(n)
    phi,dphi = BaseFun(1)
    
    x = np.linspace(-1,1,101)
    plt.plot(x, phi[0](x),"r")
    plt.plot(x, phi[1](x),"g")
    plt.plot(x, dphi[0](x),"b")
    plt.plot(x, dphi[1](x),"c")
  
   