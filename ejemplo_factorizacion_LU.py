#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:05:18 2026

@author: whadymacbook2016

"""
import numpy as np
from scipy.linalg import lu,solve


A=np.array([[1.0,2.0,3.0],[-1.0,2.0,5.0],[0.0,-2.0,4.0]])
B=np.array([1.0,1.0,1.0])

aug=np.array([[1.0,2.0,3.0,1.0],[-1.0,2.0,5.0,1.0],[0.0,-2.0,4.0,1.0]])

aug[1,:]+=aug[0,:]

aug[2,:]+=aug[1,:]*(1.0/2.0)


x=np.zeros(3)

x[2]=aug[2,3]/aug[2,2]
x[1]=(aug[1,3]-aug[1,2]*x[2])/aug[1,1]
x[0]=aug[0,3]-aug[0,1]*x[1]-aug[0,2]*x[2]

error=np.matmul(A,x)-B


L,U=lu(A,permute_l=True)
print(np.matmul(L,U))


P,L,U=lu(A)


x=solve(A,B)

















