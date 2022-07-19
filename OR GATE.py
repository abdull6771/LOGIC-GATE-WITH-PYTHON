# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 11:51:23 2022

@author: USER
"""

def or_gate(x1,x2):
    w1,w2,b,theta = (0.5,0.5,0.2,0.5)
    a = x1*w1+x2*w2+b
    if a <= theta:
        return 0
    else:
        return 1
print(or_gate(0, 1))
print(or_gate(0, 0))
print(or_gate(1, 1))
print(or_gate(1, 0))
