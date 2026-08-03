#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:29:42 2026

@author: whadymacbook2016
"""
import numpy as np

def f(x):
    y=(x-1)**2
    return y

def df(x):
    y=2*(x-1)
    return y

x=[0.5]

#asi se itera manualmente uno a uno
# x_nueva=x[0]-0.1*df(x[0])
# x.append(x_nueva)

# x_nueva=x[1]-0.1*df(x[1])
# x.append(x_nueva)

# x_nueva=x[2]-0.1*df(x[2])
# x.append(x_nueva)

# x_nueva=x[3]-0.1*df(x[3])
# x.append(x_nueva)

# x_nueva=x[4]-0.1*df(x[4])
# x.append(x_nueva)

#asi se itera automaticamente con un ciclo for

for i in range(1,40):
  x_nueva=x[i-1]-0.1*df(x[i-1])
  x.append(x_nueva)   
