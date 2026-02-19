#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 10:17:12 2026

@author: whadymacbook2016
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

Ch=0.5
Cc=0.1
Upd=0.25

Th0=80
Tc0=20 

def modelo(z,T):
    dT=np.zeros(2)
    dT[0]=-Upd*(T[0]-T[1])/Ch
    dT[1]=Upd*(T[0]-T[1])/Cc
    return dT

T0=np.array([Th0,Tc0])

zspan=[0,2]

zeval=np.linspace(zspan[0],zspan[1],100)

solucion=solve_ivp(modelo,zspan,T0,method='RK45',t_eval=zeval)


z_values=solucion.t
Th_values=solucion.y[0,:]
Tc_values=solucion.y[1,:]

plt.figure()
plt.plot(z_values,Th_values,'r')
plt.xlabel('z')
plt.ylabel('Th')

plt.figure()
plt.plot(z_values,Tc_values,'g')
plt.xlabel('z')
plt.ylabel('Tc')


plt.figure()
plt.plot(z_values,Th_values,'r')
plt.plot(z_values,Tc_values,'g')
plt.xlabel('z')
plt.ylabel('T')


fig, (ax1, ax2,ax3) = plt.subplots(3,1)
fig.suptitle('Ficguras juntas')

ax1.plot(z_values, Th_values, 'r')
ax1.set_ylabel('Th')

ax2.plot(z_values, Tc_values, 'g')
ax2.set_ylabel('Tc')

ax3.plot(z_values,Th_values)
ax3.plot(z_values,Tc_values)

plt.show()














