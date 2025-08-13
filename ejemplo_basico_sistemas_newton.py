#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 12:27:17 2025

@author: whadymacbook2016
"""
import numpy as np
from numpy.linalg import solve,norm

def F(X):
    return np.array([X[0]+X[1]-1,X[0]**2+X[1]**2-1])

def J(X):
    jac=np.array([[1,1],[2*X[0],2*X[1]]])
    return jac

X0=np.array([1,1.5])
Error=F(X0)
sigma=norm(Error)
print(sigma)

M=J(X0)
B=F(X0)
dX=solve(M,-B)
X1=X0+dX
Error=F(X1)
sigma=norm(Error)
print(sigma)


M=J(X1)
B=F(X1)
dX=solve(M,-B)
X2=X1+dX
Error=F(X2)
sigma=norm(Error)
print(sigma)

M=J(X2)
B=F(X2)
dX=solve(M,-B)
X3=X2+dX
Error=F(X3)
sigma=norm(Error)
print(sigma)

M=J(X3)
B=F(X3)
dX=solve(M,-B)
X4=X3+dX
Error=F(X4)
sigma=norm(Error)
print(sigma)
