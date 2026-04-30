#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:14:37 2026

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt

n=50
alfa=0.1
beta=0.5
epsilon=0.05
Tamb=20.0
Tbase=80.0 
L=0.25
tfinal=120 

dx=L/(n-1)
dt=0.001
Nt=10000

x=np.linspace(0,L,n)
t=np.linspace(0,Nt*dt,Nt+1)

A=np.zeros((n,n))
B=np.zeros(n)
T_presente=np.zeros(n)
T_futura=np.zeros(n)
H=np.zeros((n,Nt+1))

T_presente[:]=Tbase

H[:,0]=T_presente

for j in range(1,Nt+1):
    for i in range(n):
        if i==0:
            A[i,i]=1.0 
            B[i]=Tbase
        if i>0 and i<n-1:
            A[i,i-1]=beta/dx**2
            A[i,i]=-2*beta/dx**2-alfa-1/dt
            A[i,i+1]=beta/dx**2
            B[i]=-T_presente[i]/dt-alfa*Tamb
        if i==n-1:
            A[i,i-1]=-1/dx
            A[i,i]=1/dx+epsilon
            B[i]=epsilon*Tamb
    T_futura=np.linalg.solve(A,B)
    H[:,j]=T_futura
    T_presente=T_futura.copy()


plt.figure()
plt.plot(x,H[:,0])
plt.plot(x,H[:,10])
plt.plot(x,H[:,100])
plt.plot(x,H[:,1000])
plt.plot(x,H[:,5000])
plt.plot(x,H[:,10000])
plt.xlabel('x')
plt.ylabel('T')

plt.figure()
plt.plot(t,H[1,:])
plt.plot(t,H[10,:])
plt.plot(t,H[25,:])
plt.plot(t,H[49,:])
plt.xlabel('t')
plt.ylabel('T')























        
        

