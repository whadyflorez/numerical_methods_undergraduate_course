#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 13:07:59 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.linalg import lu

A=np.array([[1,2],[5,3]])
B=np.array([2,2])

x=np.linalg.solve(A,B)

E=np.matmul(A,x)-B

p,l,u=lu(A)

print(p)
print(l)
print(u)