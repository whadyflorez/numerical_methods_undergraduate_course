#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 12:42:00 2025

@author: whadymacbook2016
"""
import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt

n=25
L=10 
H=10
dx=L/4
dy=H/4

A=np.zeros((n,n))
B=np.zeros(n)

L1=[6,7,8,11,12,13,16,17,18]
L2=[20,21,22,23,24]
L3=[15,10,5,0,1,2,3,4,9,14,19]

for i in L1:
    A[i,i-1]=1/dx**2
    A[i,i+1]=1/dx**2
    A[i,i-5]=1/dy**2
    A[i,i+5]=1/dy**2
    A[i,i]=-2/dx**2-2/dy**2 
    B[i]=0
for i in L2:
    A[i,i]=1
    B[i]=1
for i in L3:
    A[i,i]=1
    B[i]=0   
    
    
plt.spy(A)   

u=solve(A,B) 
    
V=np.zeros((5,5)) 
V[0,:]=u[20:25]
V[1,:]=u[15:20]    
V[2,:]=u[10:15] 
V[3,:]=u[5:10]
V[4,:]=u[0:5]   
    
    
    
    
    
    
    
    









