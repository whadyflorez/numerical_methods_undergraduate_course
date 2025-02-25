#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:00:22 2025

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt

# xdata=np.array([0,1,2,3,4,5,6,7,8,9,10])
# ydata=np.array([2,2.8,3.5,5.1,7.9,12,18.3,25.2,33.8,45.1,60])

xdata=np.array([0,1,2,3,4])
ydata=np.array([2,2.8,3.5,5.1,7.9])

n=xdata.shape[0]

A=np.zeros((n,n))

xmodelo=np.linspace(0,4,25)
m=xmodelo.shape[0]
ymodelo=np.zeros(m)


for i in range(n):
    for j in range(n):
        A[i,j]=xdata[i]**j

a=np.linalg.solve(A,ydata)   

def modelo(x):
    xvector=np.zeros(n)
    for i in range(n):
        xvector[i]=x**i
    y=np.dot(a,xvector)        
    return y 

for i in range(m):
    ymodelo[i]=modelo(xmodelo[i])

print(modelo(3.5)) 

print(np.linalg.cond(A))  
print(np.linalg.det(A)) 




plt.figure()
plt.plot(xdata,ydata,'o',alpha=0.5)
plt.plot(xmodelo,ymodelo,'--')