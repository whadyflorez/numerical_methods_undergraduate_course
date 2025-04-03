#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 08:03:01 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.linalg import lu

A=np.array([[1,2,3,1],[2,5,-1,1],[4,2,7,1]])

A[1,:]=A[1,:]+(-2)*A[0,:]
print(A)
A[2,:]+=(-4)*A[0,:]
print(A)
A[2,:]+=6*A[1,:]
print(A)

x=np.zeros(3)

x[2]=A[2,3]/A[2,2]
x[1]=A[1,3]-A[1,2]*x[2]
x[0]=A[0,3]-A[0,1]*x[1]-A[0,2]*x[2]


F=lu(A[0:3,0:3])


z=np.linalg.solve(A[0:3,0:3],A[:,3])
E=np.matmul(A[0:3,0:3],z)-A[:,3]
