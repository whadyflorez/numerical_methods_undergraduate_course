#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""t
Created on Wed Aug 27 12:35:05 2025

@author: whadymacbook2016
"""
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

m=0.01
k=0.1

def ode(t,z):
    dy=np.array([z[1],(-k/m)*z[0]])
    return dy

tspan=[0,10]
z0=np.array([0.1,0])
metodo='RK45'
teval=np.linspace(0,10,100)

solucion=solve_ivp(ode,tspan,z0,method=metodo,t_eval=teval)

plt.figure()
plt.plot(solucion.t,solucion.y[0][:])
plt.xlabel('t')
plt.ylabel('X(t)')


plt.figure()
plt.plot(solucion.t,solucion.y[1][:])
plt.xlabel('t')
plt.ylabel('U(t)')


