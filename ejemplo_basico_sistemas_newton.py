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


for _ in range(30):
    Error=F(X0)
    sigma=norm(Error)
    print(sigma)
    M=J(X0)
    B=-F(X0)
    dX=solve(M,B)
    X1=X0+0.25*dX
    X0=X1

