#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:17:36 2026

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt


n=30
L=2.5 
dx=L/(n-1)
dt=0.01
tfinal=1.0 
n_pasos=int(tfinal/dt)
u_i=20.0
c=0.2 

u_presente=np.zeros(n)
u_futuro=np.zeros(n)
H=np.zeros((n,n_pasos+1))

u_presente[1:n-1]=u_i
H[:,0]=u_presente

A=np.zeros((n,n))
B=np.zeros(n)

x=np.linspace(0,L,n) 
for k in range(1,n_pasos+1):
    for j in range(n):
        if j==0:
            A[j,j]=1.0 
            B[j]=0.0 
        if j>0 and j<n-1:
            A[j,j+1]=1.0/dx**2 
            A[j,j]=-2.0/dx**2-c/dt
            A[j,j-1]=1.0/dx**2
            B[j]=-c/dt*u_presente[j]+100.0*x[j]**2
        if j==n-1:
#            A[j,j]=1.0 
#            B[j]=0.0
            A[j,j]= 1.0/dx+0.1
            A[j,j-1]=-1.0/dx
            B[j]=2.0
    u_futuro=np.linalg.solve(A,B)        
    H[:,k]=u_futuro 
    u_presente=u_futuro.copy()       
            

tiempo=np.linspace(0,tfinal,n_pasos+1)

plt.figure()
plt.plot(x,H[:,0])
plt.plot(x,H[:,2])
plt.plot(x,H[:,8])
plt.xlabel('x')
plt.ylabel('u')

plt.figure()
plt.plot(tiempo,H[0,:])
plt.plot(tiempo,H[15,:])    
plt.plot(tiempo,H[20,:]) 
plt.xlabel('t')
plt.ylabel('u')   











