#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 08:08:57 2025

@author: whadymacbook2016
"""
import numpy as np

x=np.array([1.1,2.5])

iter=50

for i in range(iter):
   x[0]=2-(1.0/5.0)*x[1]
   x[1]=-(10.0/6.0)+(2.0/6.0)*x[0]
   print(x)
   
a=np.array([[5,1],[2,-6]])
b=np.array([10,10])
x_exacta=np.linalg.solve(a,b)   

print('segunda opcion')    
for i in range(iter):
   x[0]=5+3.0*x[1]
   x[1]=10.0-5.0*x[0]
   print(x)    
    
    
a=np.array([[2,1],[3,0]])
b=np.array([1,2])
x_exacta=np.linalg.solve(a,b)      
    
a=np.array([[-4,2],[5,2]])
print(np.matmul(a,x_exacta))  
    
    
a=np.array([[2,1],[3,0],[-4,2],[5,2]]) 
b=np.array([1,2,3,4])  
x_soln=np.linalg.solve(np.matmul(np.transpose(a),a),np.matmul(np.transpose(a),b))
 
print(np.matmul(a,x_soln))    
    
    
    
    
    
    
    
    
    