#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 08:14:36 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.integrate import odeint,solve_ivp
import matplotlib.pyplot as plt

g=9.8

def F(t,z):
    dy=np.zeros(4)
    dy[0]=z[2]
    dy[1]=z[3]
    dy[2]=0 
    dy[3]=-g
    return dy

vix=100*np.cos(np.pi/4)
viy=100*np.sin(np.pi/4)

z0=np.array([0,0,vix,viy])

t0=0 
tf=30
t=np.linspace(t0,tf,100)

solucion=solve_ivp(F, [t0,tf], z0, method='RK23',t_eval=t)

plt.figure()
plt.plot(t,solucion.y[0,:])
plt.xlabel('t')
plt.ylabel('x')

plt.figure()
plt.plot(t,solucion.y[1,:])
plt.xlabel('t')
plt.ylabel('y')

plt.figure()
plt.plot(t,solucion.y[2,:])
plt.xlabel('t')
plt.ylabel(r'$V_x$')

plt.figure()
plt.plot(t,solucion.y[3,:])
plt.xlabel('t')
plt.ylabel(r'$V_y$')

plt.figure()
plt.plot(solucion.y[0,:],solucion.y[1,:])
plt.xlabel('x')
plt.ylabel('y')



fig, axs = plt.subplots(5)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(t,solucion.y[0,:])
axs[1].plot(t,solucion.y[1,:])
axs[2].plot(t,solucion.y[2,:])
axs[3].plot(t,solucion.y[3,:])
axs[4].plot(solucion.y[0,:],solucion.y[1,:])
    
    
    
   
    
    
    
    
    
    
    
    
    
    