#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 06:22:58 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

m=0.009
g=9.8
v0=350
theta=np.pi/4
tfinal=60
gamma=0.00149

def ecs(t,z):
    dz=np.array([z[2],z[3],0-gamma/m*z[2],-g-gamma/m*z[3]])
    return dz

z0=np.array([0,0,v0*np.cos(theta),v0*np.sin(theta)])

tspan=[0,tfinal]
tvals=np.linspace(0,tfinal,50)

solucion=solve_ivp(ecs,tspan,z0,method='RK45',t_eval=tvals)

plt.figure()
plt.plot(solucion.t,solucion.y[0,:])
plt.xlabel('t')
plt.ylabel('x(t)')

plt.figure()
plt.plot(solucion.t,solucion.y[1,:])
plt.xlabel('t')
plt.ylabel('y(t)')

plt.figure()
plt.plot(solucion.t,solucion.y[2,:])
plt.xlabel('t')
plt.ylabel('U(t)')

plt.figure()
plt.plot(solucion.t,solucion.y[3,:])
plt.xlabel('t')
plt.ylabel('V(t)')


plt.figure()
plt.plot(solucion.y[0,:],solucion.y[1,:])
plt.xlabel('x')
plt.ylabel('y')


