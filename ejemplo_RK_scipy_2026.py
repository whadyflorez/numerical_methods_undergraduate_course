#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 10:59:12 2026

@author: whadymacbook2016
"""
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def F(t,x):
    dx=np.zeros(3)
    dx[0]=x[1]
    dx[1]=-0.4*x[1]-4*x[0]+np.sin(t)
    dx[2]=x[0]
    #dx=np.array([x[1],-0.4*x[1]-4*x[0]+np.sin(t),x[0]])
    return dx

x0=np.array([0,1,0])

rango=[0,10]

puntos=np.linspace(0,10,100)

x_sol=solve_ivp(F,rango,x0,method='RK45',t_eval=puntos)

tiempos=x_sol.t
x0=x_sol.y[0,:]
x1=x_sol.y[1,:]
x2=x_sol.y[2,:]

plt.figure()
plt.plot(tiempos,x0)
plt.xlabel('t')
plt.ylabel('x0(t)')


plt.figure()
plt.plot(tiempos,x1)
plt.xlabel('t')
plt.ylabel('x1(t)')


plt.figure()
plt.plot(tiempos,x2)
plt.xlabel('t')
plt.ylabel('x2(t)')












