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


A=np.zeros((8,8))
A[:,0]=1
A[:,1]=x
A[:,2]=x**2 
A[:,3]=x**3
A[:,4]=x**4
A[:,5]=x**5
A[:,6]=x**6
A[:,7]=x**7


p=solve(A,y)


nplot=100
xplot=np.linspace(0,7,nplot)
yplot=[]
for i in range(nplot):
    yaprox=p[0]+p[1]*xplot[i]+p[2]*xplot[i]**2+p[3]*xplot[i]**3+\
    p[4]*xplot[i]**4+p[5]*xplot[i]**5+p[6]*xplot[i]**6+p[7]*xplot[i]**7    
    yplot.append(yaprox)
    
plt.figure()
plt.plot(xplot,yplot,'g:')
plt.plot(x,y,'+') 
plt.xlabel('valores x')
plt.ylabel('valores y')   