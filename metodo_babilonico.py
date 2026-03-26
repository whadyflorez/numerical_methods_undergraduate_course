#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:28:17 2026

@author: whadymacbook2016
"""
import numpy as np

n=5.0 

# x_guess=2.0 
# x_improved=0.5*(x_guess+n/x_guess)
# print('x=',x_improved)

# x_guess=x_improved
# x_improved=0.5*(x_guess+n/x_guess)
# print('x=',x_improved)

# x_guess=x_improved
# x_improved=0.5*(x_guess+n/x_guess)
# print('x=',x_improved)

# iter=10 
# x_guess=2.0
# for i in range(iter):
#     x_improved=0.5*(x_guess+n/x_guess)
#     print('x=',x_improved) 
#     x_guess=x_improved
    
tol=1.0e-6 
x_guess=2.0 
error=np.abs(x_guess**2-n)
iter=0  
while error>=tol and iter<10:
    x_improved=0.5*(x_guess+n/x_guess)
    print('x=',x_improved) 
    x_guess=x_improved   
    error=np.abs(x_improved**2-n)
    iter+=1


