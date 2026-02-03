#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 10:12:39 2026

@author: whadymacbook2016
"""
import numpy as np

m=0.1 
g=9.85 
rhof=1200.0 
R=0.02
v0=0.0

def v(t):
    vt=np.sqrt(m*g/(0.2*rhof*np.pi*R**2))
    y=vt*np.tanh((g*t/vt)+np.arctanh(v0/vt))
    return y

T=np.zeros((10,2))
t=np.array([0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8])
V=v(t)

T[:,0]=t
T[:,1]=V

#for i in range(0,10):
#    print(i)
    
#for i in V:
#     print(i)

tol=0.0001
for i in range(1,10):
    if np.abs(V[i]-V[i-1])>=tol:
        print(V[i])
    else:
        print('Ya se estabilizo')
         
print(f'la velocidad es:{V[1]:.3f}') 
print(f'la velocidad es:{V[1]:10.4e}') 
    
