#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:08:53 2026

@author: whadymacbook2016
"""
import numpy as np

def f(x):
    y=x**2-2.0
    return y

def df(x):
#    y=2.0*x
    epsilon=1.0e-3 
    h=epsilon*np.abs(x)
    dy=(f(x+h)-f(x))/h
    return dy

x_old=15.0

iter=10

for i in range(iter):
    x_new=x_old-f(x_old)/df(x_old)
    x_old=x_new
    print('x=',x_new,'error=',np.abs(f(x_new)))
    
    