#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 13:12:27 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.linalg import solve,det,lstsq,lu
import matplotlib.pyplot as plt

x=np.array([0,1,2,2.5,4,7,3.2,6])
y=np.array([0.5,0.7,3.5,7,4.5,10,20,9])


A=np.zeros((8,3))
A[:,0]=x**2
A[:,1]=x
A[:,2]=1.0

p=lstsq(A,y)
param=p[0]

nplot=100
xplot=np.linspace(0,7,nplot)
yplot=[]
for i in range(nplot):
    yaprox=param[0]*xplot[i]**2+param[1]*xplot[i]+param[2]
    yplot.append(yaprox)
    
plt.figure()
plt.plot(xplot,yplot,'g:')
plt.plot(x,y,'+') 
plt.xlabel('valores x')
plt.ylabel('valores y')   
    
    