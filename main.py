# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as plt

from PrintGeo import *
from ManualGeo import *
from AutomaticGeo import *
from MemoryAllocation import *
if __name__ == '__main__':
    c = 0
    f = lambda x: 1
    
    x_a = -9
    x_b = 5
    n = 6
    #nodes, sections, ev  = ManualGeo();
    #n = np.shape(nodes)[0]
    nodes, sections, ev = AutomaticGeo(x_a,x_b,n)
    PlotGeo(nodes, sections, ev)
    A,B = MemoryAllocation(n)
 
    
   