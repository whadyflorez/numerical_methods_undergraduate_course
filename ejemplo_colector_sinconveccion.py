#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 08:49:34 2025

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt

Tm=25.0 
L=2.0 
n=50
k=1.2 
q=500.0  
h=10.0

dx=L/(n-1)

A=np.zeros((n,n))
b=np.zeros(n)

x=np.linspace(0,L,n)

for i in range(n):
   if i>0 and i<n-1:
       A[i,i-1]=1.0/dx**2 
       A[i,i+1]=1.0/dx**2 
       A[i,i]=-2.0/dx**2 
       b[i]=-q/k
   if i==0:
       A[i,i]=-k/dx+h 
       A[i,i+1]=k/dx
       b[i]=h*Tm       
   if i==n-1:
       A[i,i]=-k/dx+h 
       A[i,i-1]=k/dx
       b[i]=h*Tm       

T=np.linalg.solve(A,b)
   
       
   
    

plt.spy(A)  

plt.figure()
plt.plot(x,T,'o--')     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    