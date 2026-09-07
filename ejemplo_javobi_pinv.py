#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:20:57 2026

@author: whadymacbook2016
"""
import numpy as np
from scipy.linalg import inv,pinv
from scipy.sparse.linalg import bicg

x_ini=np.array([1.0,1.5,-1.2])

x_nuevo=np.zeros(3)



iter=20

for i in range(iter):
    x_nuevo[0]=(2.0+x_ini[1]-x_ini[2])/3.0
    x_nuevo[1]=(4.0-2.0*x_ini[0]-2.0*x_ini[2])/5.0
    x_nuevo[2]=(6.0-x_ini[0])/6.0   
    x_ini=x_nuevo.copy()
    print('x=',x_nuevo)
    
#verificacion
A=np.array([[3.0,-1.0,1.0],[2.0,5.0,2.0],[1.0,0.0,6.0]]) 
B=np.array([2.0,4.0,6.0])
E=np.matmul(A,x_nuevo)-B  
print('RMSE=',np.linalg.norm(E)**2) 

#inversa de matrices
A_inv=  inv(A)
print('sol=',A_inv@B)  
    
#usanod los metodos iterativos del scipy
x_ini=np.array([1.0,1.5,-1.2])

x_bicg=bicg(A,B,x_ini)
print('solucion con bicg ',x_bicg[0])


#pseudoinversas
A=np.array([[2.0,-1.0],[4.0,6.0],[2.0,3.0],[5.0,-1]])
B=np.array([2.0,4.0,6.0,7.0])
A_pinv=pinv(A)
Sol_pinv=A_pinv@B












