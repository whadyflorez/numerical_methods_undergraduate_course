#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:14:30 2026

@author: whadymacbook2016
"""
def f(x,*args):
    if len(args)!=0:
        y=args[0]*x**2+args[1]*x+args[2]
    else:
        y=x**2
    return y

z=5
a,b,c,d=1,2,3,5
p=[1,2,3]
print('Llamando la f sin argumentos',f(z))
print('llamando la f con argumentos',f(z,a,b,c))
print('llamando la f con argumentos empaquetados',f(z,*p))

      