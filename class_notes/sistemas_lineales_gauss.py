#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 10:08:36 2026

@author: whadymacbook2016
"""
import numpy as np

A=np.array([[1.0,-2.0,3.0],[2.0,4.0,5.0],[7.0,1.0,-1.0]])
B=np.array([-1.0,2.0,-2.0])

Augm=np.array([[1.0,-2.0,3.0,-1.0],[2.0,4.0,5.0,2.0],[7.0,1.0,-1.0,-2.0]])

d=np.linalg.det(A)

Augm[1,:]-=2.0*Augm[0,:]
Augm[2,:]-=7.0*Augm[0,:]
Augm[2,:]-=(15.0/8.0)*Augm[1,:]

x=np.zeros(3)
x[2]=Augm[2,3]/Augm[2,2]
x[1]=(Augm[1,3]+(-Augm[1,2])*x[2])/Augm[1,1]
x[0]=(Augm[0,3]+(-Augm[0,1]*x[1])+(-Augm[0,2]*x[2]))/Augm[0,0]

Error=np.matmul(A,x)-B
Etot=np.linalg.norm(Error)

print(A.T)
print(np.transpose(A))

x_numpy=np.linalg.solve(A,B)

