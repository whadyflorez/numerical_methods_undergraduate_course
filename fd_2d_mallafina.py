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

n=121   



H=0.2 
V=0.1 
dx=H/3 
dy=V/3 

A=np.zeros((n,n))
B=np.zeros(n) 

x=np.linspace(0,H,11)
y=np.linspace(0,V,11)
X=np.zeros((11,11))
Y=np.zeros((11,11))
U=np.zeros((11,11))

X[0,:]=x
X[1,:]=x
X[2,:]=x
X[3,:]=x
X[4,:]=x
X[5,:]=x
X[6,:]=x
X[7,:]=x
X[8,:]=x
X[9,:]=x
X[10,:]=x

for i in range(11):
    Y[:,i]=y


internos1=list(range(12,21))
internos2=list(range(23,32))
internos3=list(range(34,43))
internos4=list(range(45,54))
internos5=list(range(56,65))
internos6=list(range(67,76))
internos7=list(range(78,87))
internos8=list(range(89,98))
internos9=list(range(100,109))
internos=internos1+internos2+internos3+\
internos4+internos5+internos6+internos7+internos8+internos9

izquierda=list(range(11,110,11))
derecha=list(range(21,120,11))
abajo=list(range(0,11))
arriba=list(range(110,121))

for i in internos:
    A[i,i+1]=1/dx**2
    A[i,i-1]=1/dx**2
    A[i,i+11]=1/dy**2
    A[i,i-11]=1/dy**2
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

# U[0,:]=u[0:11] #i=0
# U[1,:]=u[11:22] #i=1
# U[2,:]=u[22:33] #i=2
# U[3,:]=u[33:44]
# U[4,:]=u[44:55]
# U[5,:]=u[55:66]
# U[6,:]=u[66:77]
# U[7,:]=u[77:88]
# U[8,:]=u[88:99]
# U[9,:]=u[99:110]
# U[10,:]=u[110:121]

for i in range(11):
    U[i,:]=u[11*i:11*i+11]
    








fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf=ax.plot_surface(X, Y, U,cmap=cm.coolwarm)        
fig.colorbar(surf, shrink=0.5, aspect=5)
    












