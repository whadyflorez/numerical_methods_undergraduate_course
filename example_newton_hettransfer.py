#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:33:37 2026

@author: whadymacbook2016
"""
import numpy as np

Bi=1.0

def f(x):
    y=x*np.tan(x)-Bi
    return y

def df(x):
#    y=2.0*x
    epsilon=1.0e-6 
    h=epsilon*np.abs(x)
    dy=(f(x+h)-f(x))/h
    return dy

tol=1.0e-6
error=1.0 
maxiter=100
iter=0

x_old=0.5

while error>tol and iter<maxiter:
    x_new=x_old-f(x_old)/df(x_old)
    x_old=x_new
    error=np.abs(f(x_new))
    iter+=1
    print(f"{iter} x={x_new:.3e},Error={error:.3e}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
