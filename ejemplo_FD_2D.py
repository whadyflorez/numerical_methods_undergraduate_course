#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 09:06:43 2025

@author: whadymacbook2016
"""
import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt
from matplotlib import cm

n=16    



H=0.2 
V=0.1 
dx=H/3 
dy=V/3 

A=np.zeros((n,n))
B=np.zeros(16) 

x=[0,dx,2*dx,3*dx]
y=[0,dy,2*dy,3*dy]
X=np.zeros((4,4))
Y=np.zeros((4,4))
U=np.zeros((4,4))

X[0,:]=x
X[1,:]=x
X[2,:]=x
X[3,:]=x
Y[:,0]=y
Y[:,1]=y
Y[:,2]=y
Y[:,3]=y


internos=[9,10,5,6]
izquierda=[0,4,8]
derecha=[3,7,11]
abajo=[1,2]
arriba=[12,13,14,15]

for i in internos:
    A[i,i+1]=1/dx**2
    A[i,i-1]=1/dx**2
    A[i,i+4]=1/dy**2
    A[i,i-4]=1/dy**2
    A[i,i]=-2/dx**2-2/dy**2
    B[i]=0
    
for i in izquierda:
    A[i,i]=1 
    B[i]=0

for i in derecha:
    A[i,i]=1 
    B[i]=0

for i in abajo:
    A[i,i]=1 
    B[i]=0   
    
for i in arriba:
    A[i,i]=1 
    B[i]=1    

u=solve(A,B)    

U[0,:]=u[0:4]
U[1,:]=u[4:8]
U[2,:]=u[8:12]
U[3,:]=u[12:16]

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf=ax.plot_surface(X, Y, U,cmap=cm.coolwarm)        
fig.colorbar(surf, shrink=0.5, aspect=5)
    












