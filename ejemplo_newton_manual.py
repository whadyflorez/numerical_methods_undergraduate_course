#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 08:47:26 2025

@author: whadymacbook2016
"""
import numpy as np

def F(X):
    y=np.array([X[0]-4*X[1],X[0]**2+X[1]**2-5])
    return y 

def J(X):
    M=np.array([[1,-4],[2*X[0],2*X[1]]])
    return M

x0=np.array([1.1,1.5])
print(x0,np.linalg.norm(F(x0)))

dx=np.linalg.solve(J(x0),-F(x0))

xnuevo=x0+dx
print(xnuevo,np.linalg.norm(F(xnuevo)))

x0=xnuevo
dx=np.linalg.solve(J(x0),-F(x0))
xnuevo=x0+dx
print(xnuevo,np.linalg.norm(F(xnuevo)))

x0=xnuevo
dx=np.linalg.solve(J(x0),-F(x0))
xnuevo=x0+dx
print(xnuevo,np.linalg.norm(F(xnuevo)))

x0=xnuevo
dx=np.linalg.solve(J(x0),-F(x0))
xnuevo=x0+dx
print(xnuevo,np.linalg.norm(F(xnuevo)))
