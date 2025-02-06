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

nsteps=100
dt=tf/nsteps
nt=nsteps+1 

data=np.zeros((nt,2)) #euler
data_exacta=np.zeros((nt,2)) #exacta
data_rk=np.zeros((nt,2)) #rk 4
data_rk2=np.zeros((nt,2)) #rk2

data[0,:]=[t0,v0]
data_rk[0,:]=[t0,v0]

for i in range(nsteps):
    vnew=v0+dt*df(v0,t0)
    tnew=t0+dt
    data[i+1,:]=[tnew,vnew]
    t0=tnew
    v0=vnew

#metodo rk 4
t0=0
v0=0
for i in range(nsteps):
    k1=df(v0,t0)
    k2=df(v0+0.5*dt*k1,t0+0.5*dt)
    k3=df(v0+0.5*dt*k2,t0+0.5*dt)
    k4=df(v0+dt*k3,t0+dt)
    vnew_rk=v0+(dt/6)*(k1+2*k2+2*k3+k4)
    tnew=t0+dt
    data_rk[i+1,:]=[tnew,vnew_rk]
    t0=tnew
    v0=vnew_rk
    
#metodo rk 2
t0=0
v0=0
for i in range(nsteps):
    k1=df(v0,t0)
    k2=df(v0+dt*k1,t0+dt)
    vnew_rk=v0+(dt/2)*(k1+k2)
    tnew=t0+dt
    data_rk2[i+1,:]=[tnew,vnew_rk]
    t0=tnew
    v0=vnew_rk    
    
for i in range(nt):
    data_exacta[i,:]=[data[i,0],exacta(data[i,0])] 
    

plt.figure()
plt.plot(data[:,0],data[:,1],'o',label='euler')
plt.plot(data_exacta[:,0],data_exacta[:,1],'r-',label='exact')
plt.plot(data_rk[:,0],data_rk[:,1],'+',label='rk4')
plt.plot(data_rk2[:,0],data_rk2[:,1],'*',label='rk2')
plt.xlabel('t')
plt.ylabel('v(t)')
plt.legend(loc='upper right')


plt.figure()

plt.plot(data_exacta[:,0],data[:,1]-data_exacta[:,1],'-',label='euler')
plt.plot(data_exacta[:,0],data_rk[:,1]-data_exacta[:,1],'--',label='rk')
plt.xlabel('t')
plt.ylabel('error neto')
plt.legend(loc='upper right')










    