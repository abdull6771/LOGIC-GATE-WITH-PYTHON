# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:40:10 2022

@author: USER
"""
def or_gate(x1,x2):
    w1,w2,b,theta = (0.5,0.5,0.2,0.5)
    a = x1*w1+x2*w2+b
    if a <= theta:
        return 0
    else:
        return 1


def and_get(x1,x2):
    w1,w2,b,theta = (0.3,0.3,0.1,0.5)
    a = x1*w1+x2*w2 +b
    if a<=theta:
        return 0
    else:
        return 1


def nand_gate(x1,x2):
    w1,w2,b,theta = (-0.5,-0.5,-0.2,-0.8)
    a = x1*w1+x2*w2+b
    if a <= theta:
        return 0
    else:
        return 1
def xor(x1,x2):
    s1 = nand_gate(x1, x2)
    s2 = or_gate(x1, x2)
    y = and_get(s1, s2)
    return y
print(xor(0, 1))
print(xor(0, 0))
print(xor(1, 1))
print(xor(1, 0))