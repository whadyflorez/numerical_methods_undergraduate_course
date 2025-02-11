#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:01:08 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.integrate import odeint,solve_ivp
import matplotlib.pyplot as plt

k=0.1
m=0.6 


v0=0.0
x0=-0.2 


def df(t,y):
    dy=np.zeros(2)
    dy[0]=y[1]
    dy[1]=-k/m*y[0]
    return dy

y0=[x0,v0]

t=np.linspace(0,60,100)

solucion=solve_ivp(df, [0,60], y0, method='RK23', \
t_eval=t)

plt.figure()
plt.plot(t,solucion.y[0,:],'o-')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.figure()
plt.plot(t,solucion.y[1,:],'o-')
plt.xlabel('t')
plt.ylabel('v(t)')
