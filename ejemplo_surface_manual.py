#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 21:02:55 2025

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

x=np.array([0,1,2,3])
y=np.array([4,2,0])

X=np.zeros((3,4))
Y=np.zeros((3,4))
Z=np.zeros((3,4))

X[0,:]=x
X[1,:]=x
X[2,:]=x

Y[:,0]=y
Y[:,1]=y
Y[:,2]=y
Y[:,3]=y

for i in range(3):
    for j in range(4):
        Z[i,j]=X[i,j]**2+Y[i,j]**2
        
fig1, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, Z)        
        
fig2, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf=ax.plot_surface(X, Y, Z,cmap=cm.coolwarm)        
fig2.colorbar(surf, shrink=0.5, aspect=5)
        

