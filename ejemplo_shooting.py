#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:19:16 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.integrate import odeint,solve_ivp
import matplotlib.pyplot as plt

def F(x,theta):
    df=np.zeros(2)
    df[0]=theta[1]
    df[1]=0.1*(theta[0]-20)
    return df

qi=-400
L=0.2
theta_i=np.array([100,qi])

x=np.linspace(0,L,50)

solucion=solve_ivp(F, [0,L], theta_i, method='RK23',t_eval=x)



plt.figure()
plt.plot(x,solucion.y[0,:])