#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:31:57 2026

@author: whadymacbook2016
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

g=9.8
def F(t,z):
    x=z[0]
    v=z[1]
    vectorF=np.array([v,-g])
    return vectorF

dominio=[0,5]

y0=np.array([20,0])

tiempos=np.linspace(0,dominio[1],50)

sol=solve_ivp(F,dominio,y0,method='RK23',t_eval=tiempos)


valores_t=sol.t 
valores_x=sol.y[0]
valores_v=sol.y[1]

plt.figure()
plt.plot(valores_t,valores_x)
plt.xlabel('t')
plt.ylabel('x(t)')

plt.figure()
plt.plot(valores_t,valores_v)
plt.xlabel('t')
plt.ylabel('v(t)')




