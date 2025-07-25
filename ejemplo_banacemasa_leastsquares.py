#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 06:10:31 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.linalg import solve,det,lstsq,lu


A=np.array([[1,1,0,0,0],[1,0,-1,0,-1],[0,1,1,-1,0],[0,0,0,1,1]])
rhs=np.array([100,0,0,100])


x=lstsq(A,rhs)
solucion=x[0]
print(np.matmul(A,solucion))
print(np.linalg.matrix_rank(A))
P,L,U=lu(A)


#redefinir el problema x1=60,x3=10
A=np.array([[1,1,0,0,0],[0,1,1,-1,0],[0,0,0,1,1],[1,0,0,0,0],[0,0,1,0,0]])
rhs=np.array([100,0,100,60,10])
xx=solve(A,rhs)
print(det(A))






















