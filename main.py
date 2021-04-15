# -*- coding: utf-8 -*-
import numpy as np
import random as r


def init_param():
    print('Write start x')
    x_start = float(input())
    print('Write end  x')
    x_end = float(input())
    
    print('Write left condition')
    left_cond = int(input())
    print('Write right condition')
    right_cond = int(input())
    
    print('Write left type')
    left_type = input()
    print('Write right type')
    right_type = input()
    
    x_range = np.array([x_start, x_end])
    conditions = np.array([left_cond, right_cond])
    types = np.array([left_type, right_type])
    return x_range, conditions, types
    
#1a

#1b
x_range, conditions, types = init_param()

