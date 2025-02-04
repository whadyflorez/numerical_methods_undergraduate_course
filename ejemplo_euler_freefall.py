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
mu=0.01 
v0=0.0
t0=0.0 

def df(v,t):
    dy=-g-mu/m*v
    return dy

def exacta(t):
    y=(g*m/mu)*(np.exp(-mu/m*t)-1)
    return y


tf=200.0 

nsteps=50
dt=tf/nsteps
nt=nsteps+1 

data=np.zeros((nt,2))
data_exacta=np.zeros((nt,2))

data[0,:]=[t0,v0]

for i in range(nsteps):
    vnew=v0+dt*df(v0,t0)
    tnew=t0+dt
    data[i+1,:]=[tnew,vnew]
    t0=tnew
    v0=vnew
    
for i in range(nt):
    data_exacta[i,:]=[data[i,0],exacta(data[i,0])] 
    

plt.figure()
plt.plot(data[:,0],data[:,1],'o')
plt.plot(data_exacta[:,0],data_exacta[:,1],'r-')
plt.xlabel('t')
plt.ylabel('v(t)')


plt.figure()
plt.plot(data_exacta[:,0],data[:,1]-data_exacta[:,1],'-')
plt.xlabel('t')
plt.ylabel('error neto')









    