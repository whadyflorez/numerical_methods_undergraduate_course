#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 08:25:25 2025
ejemplo geometria anular FD
@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

rin=1e-2 
rout=0.1
Tm=20.0
h=10.0
k=200.0
t=2e-3 
Tb=80.0 
n=50
dr=(rout-rin)/(n-1)
r=np.linspace(rin,rout,n)
dTdr=np.zeros(n)

A=np.zeros((n,n))
B=np.zeros(n)

for i in range(n):
    if i==0:
        A[i,i]=1 
        B[i]=Tb
    if i>0 and i<n-1:
        A[i,i+1]=1/dr**2+1/(2*r[i]*dr)
        A[i,i-1]=1/dr**2-1/(2*r[i]*dr)
        A[i,i]=-2/dr**2-2*h/(k*t)
        B[i]=-2*h/(k*t)*Tm
    if i==n-1:
        A[i,i]=-k/dr-h
        A[i,i-1]=k/dr
        B[i]=-h*Tm
        
T=np.linalg.solve(A,B)   

for i in range(n):
    if i==0:
#        dTdr[i]=(T[i+1]-T[i])/dr
        dTdr[i]=(-3*T[i]+4*T[i+1]-T[i+2])/(2*dr)
    if i>0 and i<n-1:
        dTdr[i]=(T[i+1]-T[i-1])/(2*dr)
    if i==n-1:
        dTdr[i]=(T[i]-T[i-1])/dr


rinterpol=0.025   
f=interp1d(r,T)
Tinterpol=f(rinterpol)
  
        
plt.figure()
plt.plot(r,T,'o--')

plt.figure()
plt.plot(r,dTdr,'*--')
























