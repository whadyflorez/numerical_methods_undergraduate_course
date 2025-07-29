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


A=np.zeros((8,2))
A[:,0]=x
A[:,1]=1.0

p=lstsq(A,y)
param=p[0]

nplot=50
xplot=np.linspace(0,6,nplot)
yplot=[]
for i in range(nplot):
    yaprox=param[0]*xplot[i]+param[1]
    yplot.append(yaprox)
    
plt.figure()
plt.plot(xplot,yplot,'--')
plt.plot(x,y,'o')    
    
    