# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:53:13 2021

@author: Kot
"""

def BaseFun(n):
    if n == 0:
        f = lambda x: 0*x + 1
        df = lambda x: 0*x
    elif n == 1:
        f = (lambda x: -1/2 * x + 1/2, lambda x: 0.5*x + 0.5)
        df = (lambda x: -1/2 + 0*x, lambda x: 0.5 + 0*x)
    else:
        raise Exception("Error basefun")
        
    return f,df