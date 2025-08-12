#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 11:33:52 2025

@author: whadymacbook2016
"""
import numpy as np

g=1.4
RA=1.8


def f(M):
   y=RA-(1/M)*((2/(g+1))*(1+((g-1)/2)*M**2))**((g+1)/(2*(g-1)))
   return y

def df(M):
    y=M**(-2)*((2/(g+1))*(1+((g-1)/2)*M**2))**((g+1)/(2*(g-1)))-\
    (1/M)*((g+1)/(2*(g-1)))*\
    ((2/(g+1)*(1+(g-1)/2*M**2))**((3-g)/(2*(g-1))))*\
    (2/(g+1))*(g-1)*M
    return y

def df_numerica(x):
    dx=0.01
    y=(f(x+dx)-f(x))/dx
    return y

M0=1.1

iter=20

for i in range(iter):
    M_new=M0-f(M0)/df_numerica(M0)
    print(i,M_new,f(M_new))
    M0=M_new      
    
    



