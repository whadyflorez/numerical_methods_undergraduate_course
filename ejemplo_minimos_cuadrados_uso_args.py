#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 07:38:17 2026

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import random

xdata=np.array([0.0,1.0,2.5,4.0])
ydata=np.array([1.0,1.7,1.5,5.0])
n=len(xdata)

def modelo(x,*args):
    y=args[0]+args[1]*x
    return y

def error(p):
    suma=0
    for i in range(n):
        e_i=(ydata[i]-modelo(xdata[i],*p))**2
        suma+=e_i
#    suma=np.sum((ydata-modelo(xdata,*p))**2 )   #vectorizado
    return suma    

nparams=2
random.seed(42)
params = [random.uniform(-1, 1) for _ in range(nparams)]        


n_m=20
x_m=np.linspace(0,4,n_m)
y_m1=np.zeros(n_m)
y_m2=np.zeros(n_m)

for i in range(n_m):
    y_m1[i]=modelo(x_m[i],*params)

result=minimize(error,params)
p=result.x

for i in range(n_m):
    y_m2[i]=modelo(x_m[i],*p)

plt.figure()
plt.plot(x_m,y_m1,'--',label=r'$p_{arbitrarios}$') 
plt.plot(xdata,ydata,'o',label=r'$p_{ajustados}$')   
plt.plot(x_m,y_m2,'-.') 
plt.legend()

print(f'Error con parametros arbitrarios {error(params):.3E}')

print(f'error con parametros ajustados {error(p):.3E}')    
    







  