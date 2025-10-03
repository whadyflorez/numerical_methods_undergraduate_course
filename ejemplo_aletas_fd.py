#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 12:47:48 2025

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (necesario para la proyección 3D)


n=35
L=2
H=1
dx=L/6
dy=H/4

A=np.zeros((35,35))
B=np.zeros(35)

L1=[8,9,10,11,12,15,16,17,18,19,22,23,24,25,26]
L2=[0,7,14,21,28]
L3=[29,30,31,32,33,34]
L4=[1,2,3,4,5,6]
L5=[27,20,13]


for i in L1:
    A[i,i+1]=1/dx**2
    A[i,i-1]=1/dx**2
    A[i,i+7]=1/dy**2
    A[i,i-7]=1/dy**2
    A[i,i]=-2/dx**2-2/dy**2-0.1
    B[i]=0
for i in L2:
    A[i,i]=1
    B[i]=10
for i in L3:
    A[i,i-7]=-1/dx
    A[i,i]=1/dx+1
    B[i]=20 
for i in L4:
    A[i,i+7]=1/dy
    A[i,i]=-1/dy-1
    B[i]=-20 
for i in L5:
    A[i,i]=1/dx
    A[i,i-1]=-1/dx
    B[i]=0

plt.spy(A)

T=np.linalg.solve(A,B)

V=np.zeros((5,7))
V[0,:]=T[28:35]
V[1,:]=T[21:28]
V[2,:]=T[14:21]
V[3,:]=T[7:14]
V[4,:]=T[0:7]


# Malla de coordenadas (5x5 porque V es 5x5)
x = np.linspace(0, L, 7)
y = np.linspace(0, H, 5)
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, V,cmap='viridis')

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$u(x,y)$')
ax.set_title('Superficie de $u(x,y)$ en la malla 5x5')

cb = fig.colorbar(surf, shrink=0.7, aspect=12)
cb.set_label(r'$u$')

plt.tight_layout()
plt.show()    
    
    












    













    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



























