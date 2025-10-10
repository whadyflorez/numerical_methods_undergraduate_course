#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 10:35:23 2025

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt

L=5e-2
n=25
dx=L/(n-1)
dt=5
alpha=1e-6 
tfinal= 60*60
nt=int(tfinal/dt)
x=np.linspace(0,L,n)
t=np.linspace(0,tfinal,nt+1)

Told=100*np.ones(n)
Tnew=np.zeros(n)
H=np.zeros((n,nt+1))

H[:,0]=Told
for j in range(1,nt+1):
    for i in range(1,n-1):
        Tnew[i]=Told[i]+alpha*dt*(Told[i+1]-2*Told[i]+Told[i-1])/dx**2 
    Tnew[0]=20 
    Tnew[n-1]=Tnew[n-2]  
    H[:,j]=Tnew
    Told[:]=Tnew


plt.figure()

for j in range(0,nt+1,int(nt/10)):    
    plt.plot(x,H[:,j],'-*')   
plt.xlabel('x')
plt.ylabel('T')        
    
    
    
plt.figure()  
plt.plot(t,H[24,:],'*-')
plt.plot(t,H[12,:],'g*-')
plt.xlabel('t')
plt.ylabel('T')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





