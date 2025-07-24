#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 06:10:31 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.linalg import solve,det,lstsq

#x5=30
A=np.array([[1,1,0,0,0],[1,0,-1,0,-1],[0,1,1,-1,0],[0,0,0,1,1]])
rhs=np.array([100,0,0,100])

#d=det(A)
x=lstsq(A,rhs)

solucion=x[0]


AA=np.array([[1,1,0,0],[0,1,1,-1],[1,0,-1,1],[1,0,0,0]])
print(np.linalg.det(AA))


















