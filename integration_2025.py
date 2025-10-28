#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 06:00:03 2025

@author: whadymacbook2016
"""
import scipy.integrate as sp
import numpy as np
from scipy.special import roots_legendre

def f(x):
    y=x**2 
    return y

def cp(T):
    y=25.48+1.520e-2*T-0.7155e-5*T**2+1.312e-9*T**3 
    return y
    

a=0 
b=3 

I=sp.quad(f,a,b)

print(I)

T1=300 
T2=500 

dH=sp.quad(cp,T1,T2)

dH_quad=sp.fixed_quad(cp,T1,T2,n=2)

z=roots_legendre(3)

def f2(y,x):
    z=x**2+y**2 
    return z

def g(x):
    y=x**3 
    return y

def h(x):
    y=x**4
    return y

I2=sp.dblquad(f2,0,5,g,h)


