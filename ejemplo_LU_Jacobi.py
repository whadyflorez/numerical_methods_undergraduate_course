#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 10:09:08 2026

@author: whadymacbook2016
"""
from scipy.linalg import lu
import numpy as np

A=np.array([[1.0,2.0,3.0],[-1.5,-2.0,4.0],[0.0,1.0,1.0]])

(P,L,U)=lu(A)

multi=np.matmul(np.matmul(P,L),U)

#ejemplo metodo de Jacobi

x_ini=np.array([1.5,1.7])

for i in range(100):
    x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
    x_ini=x_new
    print(x_new)

# x_ini=x_new
# x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
# print(x_new)

# x_ini=x_new
# x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
# print(x_new)

# x_ini=x_new
# x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
# print(x_new)

# x_ini=x_new
# x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
# print(x_new)

# x_ini=x_new
# x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
# print(x_new)

# x_ini=x_new
# x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
# print(x_new)

# x_ini=x_new
# x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
# print(x_new)

# x_ini=x_new
# x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
# print(x_new)

# x_ini=x_new
# x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
# print(x_new)

# x_ini=x_new
# x_new=np.array([(2.0+2.0*x_ini[1])/5,(2.0-x_ini[0])/3])
# print(x_new)

M=np.array([[5.0,-2.0],[1.0,3.0]])
B=np.array([2.0,2.0])

print('Vector de errorres:',np.matmul(M,x_new)-B)
print('Error global',np.linalg.norm(np.matmul(M,x_new)-B))
