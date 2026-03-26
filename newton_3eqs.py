#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:09:04 2026

@author: whadymacbook2016
"""
import numpy as np
from numpy.linalg import solve,norm
import matplotlib.pyplot as plt



def F(x):
    y=np.zeros(3)
    y[0]=x[0]**2+x[1]**2+x[2]**2-9
    y[1]=np.exp(x[0])+x[1]-x[2]-1
    y[2]=x[0]+x[1]**3-x[2]
    return y

def J(x):
    j=np.array([[2*x[0],2*x[1],2*x[2]],\
                [np.exp(x[0]),1,-1],\
               [1,3*x[1]**2,-1]])
    
    return j

x_old=np.array([1.1,1.3,0.1])

iter=10

plt.figure()
error=1e6 
tol=1e-6
p=0.1
while error>tol:
    delta=solve(J(x_old),-F(x_old))
    x_new=x_old+delta*p
    x_old=x_new.copy()
    error=norm(F(x_new))
    print(f"x={x_new},Error={error:.3e}")
    





