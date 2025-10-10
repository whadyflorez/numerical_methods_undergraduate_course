#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 10:35:23 2025

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt

R=0.05
n=50
dr=R/(n-1)
dt=0.0001
tfinal= 0.005
nt=int(tfinal/dt)
r=np.linspace(0,R,n)
t=np.linspace(0,tfinal,nt+1)

Told=30*np.ones(n)
Tnew=np.zeros(n)
H=np.zeros((n,nt+1))

A=np.zeros((n,n))
B=np.zeros(n)


H[:,0]=Told

F1=[0]
F2=list(range(1,n-1))
F3=[n-1] 

for i in F1:
    A[i,i+1]=1/dr 
    A[i,i]=-1/dr
for i in F2:
    A[i,i+1]=1/dr**2+1/(2*dr*r[i])
    A[i,i-1]=1/dr**2-1/(2*dr*r[i])
    A[i,i]=-2/dr**2-1/dt
for i in F3:
    A[i,i]=1

for j in range(1,nt+1):
    for i in F1:
        B[i]=0
    for i in F2:
        B[i]=-100-Told[i]/dt 
    for i in F3:
        B[i]=30
    Tnew=np.linalg.solve(A,B)
    H[:,j]=Tnew 
    Told[:]=Tnew    
        
        


plt.figure()

for j in range(0,nt+1,int(nt/10)):    
    plt.plot(r,H[:,j],'-*')   
plt.xlabel('r')
plt.ylabel('T')        
    
    
    
plt.figure()  
plt.plot(t,H[24,:],'*-')
plt.plot(t,H[12,:],'g*-')
plt.xlabel('t')
plt.ylabel('T')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





