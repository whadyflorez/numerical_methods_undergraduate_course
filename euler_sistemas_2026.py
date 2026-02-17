#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 08:10:32 2025

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt

g=9.8 
m=0.1 
mu=0.03 
v0=0.0
t0=0.0 
x0=100.0

def df(y,t):
    dy=np.zeros(2)
    dy=np.array([y[1],-g-mu/m*y[1]])
    return dy

tf=25 

nsteps=200
dt=tf/nsteps
nt=nsteps+1 

data=np.zeros((nt,3))

data[0,:]=[t0,x0,v0]

y0=np.array([x0,v0])

for i in range(nsteps):
    ynew=y0+dt*df(y0,t0)
    tnew=t0+dt
    data[i+1,:]=[tnew,ynew[0],ynew[1]]
    t0=tnew
    y0=ynew
    
plt.figure()
plt.plot(data[:,0],data[:,1])
plt.xlabel('t')
plt.ylabel('x(t)')

plt.figure()
plt.plot(data[:,0],data[:,2])
plt.xlabel('t')
plt.ylabel('v(t)')
