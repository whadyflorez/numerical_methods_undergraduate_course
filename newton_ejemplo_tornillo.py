#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 11:33:52 2025

@author: whadymacbook2016
"""
import numpy as np

M=40
d=0.012
sigma=640e6
At=84/(1000**2)


def f(x):
   K=0.18+0.0005*x**0.6
   y=M-K*x*d 
   return y

def df(x):
    K=0.18+0.0005*x**0.6
    y=-K*d-(0.0005*0.6*x**0.6*d)
    return y

def df_numerica(x):
    dx=0.01
    y=(f(x+dx)-f(x))/dx
    return y

x0=0.35*sigma*At

iter=10

for i in range(iter):
    x_new=x0-f(x0)/df_numerica(x0)
    print(i,x_new,f(x_new))
    x0=x_new      
    
    



