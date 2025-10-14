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
tfinal= 30*60
nt=int(tfinal/dt)
x=np.linspace(0,L,n)
t=np.linspace(0,tfinal,nt+1)

Told=100*np.ones(n)
Tnew=np.zeros(n)
H=np.zeros((n,nt+1))

A=np.zeros((n,n))
B=np.zeros(n)


H[:,0]=Told

F1=list(range(1,n-1))
F2=[0]
F3=[n-1] 

for i in F1:
    A[i,i+1]=alpha/dx**2
    A[i,i-1]=alpha/dx**2 
    A[i,i]=-2*alpha/dx**2-1/dt 
for i in F2:
    A[i,i]=1
for i in F3:
    A[i,i-1]=-1/dx 
    A[i,i]=1/dx

for j in range(1,nt+1):
    for i in F1:
        B[i]=-Told[i]/dt
    for i in F2:
        B[i]=20 
    for i in F3:
        B[i]=0
    Tnew=np.linalg.solve(A,B)
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





