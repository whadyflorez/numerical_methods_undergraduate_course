#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 07:14:29 2025

@author: whadymacbook2016
"""
import numpy as np

def h(beta,k,nu,D,Th,Tl):
    g=9.8
    Ra=g*beta*(Th-Tl)*D**3/nu**2
    if Ra>=0.1 and Ra<1000.0:
        c,n=1.02,0.148
    if Ra>=1000.0 and Ra<100000.0:
        c,n=0.85,0.188
    if Ra>=100000.0 and Ra<1.0e8:
        c,n=0.48,0.25
    if Ra>=1.0e8 and Ra<1.0e13:
        c,n=0.125,0.33
    Nu=c*Ra**n
    y=Nu*k/D
    return y

k=26.3e-3
nu=15.89e-6 
Th=80.0+273.15
Tl=25.0+273.15
beta=1.0/Th
D=2.0e-2
valorh=h(beta,k,nu,D,Th,Tl)
print('h=',valorh)


    






















