#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:52:48 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

g=9.8 
m=0.1 
mu=0.01 

v0=0.0
t0=0.0 

def df(v,t):
    dy=-g-mu/m*v
    return dy

y0=v0

t=np.linspace(0,60,100)

solucion=odeint(df,y0,t)


plt.plot(t,solucion,'o')
plt.xlabel('t')
plt.ylabel('v(t)')