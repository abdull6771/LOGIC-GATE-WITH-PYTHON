# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:11:02 2022

@author: USER
"""

def nand_gate(x1,x2):
    w1,w2,b,theta = (-0.5,-0.5,-0.2,-0.8)
    a = x1*w1+x2*w2+b
    if a <= theta:
        return 0
    else:
        return 1
print(nand_gate(0, 1))
print(nand_gate(0, 0))
print(nand_gate(1, 1))
print(nand_gate(1, 0))