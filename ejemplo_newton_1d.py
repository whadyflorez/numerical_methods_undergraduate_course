#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 08:36:19 2025

@author: whadymacbook2016
"""
import numpy as np

Bi=3

def f(x):
    y=x*np.tan(x)-Bi
    return y

def df(x):
    yp=x/(np.cos(x))**2+np.tan(x)
    return yp

x_supuesto=1.1 
#print(f(x_supuesto))

#dx=-f(x_supuesto)/df(x_supuesto)

#x_nuevo=x_supuesto+dx

#print(f(x_nuevo))

#x_supuesto=x_nuevo
#dx=-f(x_supuesto)/df(x_supuesto)
#x_nuevo=x_supuesto+dx
#print(f(x_nuevo))

#for i in range(10):
#    dx=-f(x_supuesto)/df(x_supuesto)
#    x_nuevo=x_supuesto+dx
#    print(f(x_nuevo))
#    x_supuesto=x_nuevo

tol=1e-8
error=1
while error>tol:
    dx=-f(x_supuesto)/df(x_supuesto)
    x_nuevo=x_supuesto+dx
    print(f(x_nuevo))
    error=np.abs(f(x_nuevo))
    x_supuesto=x_nuevo
    
print('solucion',x_nuevo)    
