#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:15:53 2026

@author: whadymacbook2016
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#definir las constantes del problema
g=9.8
k=0.1
Ho=100 
tfinal=60 
#m=2 

def masa(t):
    if t<=20:
        m=2 
    else:
        m=1
    return m

#definir la funcion con el sistema de ecuaciones
def F(t,z):   
    y=np.array([z[1],-g-k/masa(t)*z[1]])
    return y

#condiciones iniciales

z0=np.array([Ho,0]) 

t_val=np.linspace(0,tfinal,100)

sol=solve_ivp(F,[0,tfinal],z0,method='RK45',t_eval=t_val)   
    
tiempos=sol.t
altura=sol.y[0]
velocidad=sol.y[1]



plt.subplot(1,2,1)
plt.plot(tiempos,altura)
# plt.xlabel('t')
# plt.ylabel('H(t)')

plt.subplot(1,2,2)
plt.plot(tiempos,velocidad)
# plt.xlabel('t')
# plt.ylabel('V(t)')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    