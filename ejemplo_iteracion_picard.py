#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 08:17:31 2025

@author: whadymacbook2016
"""
import numpy as np

x=1.6
Bi=3.0

#print(np.tan(x),Bi/x)

def f(x):
    y=x*np.tan(x)-Bi
    return y

print(f(1.1),f(1.5))
x_prom=0.5*(1.1+1.5)
print(f(x_prom
        ))
x_prom=(1.1+1.3)/2 
print(f(x_prom))

x_prom=(1.1+1.2)/2
print(f(x_prom))
