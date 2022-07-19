# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 11:36:25 2022

@author: USER
"""

def and_get(x1,x2):
    w1,w2,b,theta = (0.3,0.3,0.1,0.5)
    a = x1*w1+x2*w2 +b
    if a<=theta:
        return 0
    else:
        return 1
print(and_get(0,0))
print(and_get(1,0))
print(and_get(0,1))
print(and_get(1,1))