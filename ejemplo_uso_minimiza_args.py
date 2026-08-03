#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:21:31 2026

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#ejemplo funcion con variable vectorial y parametros vectorizados
def f_obj(x,*args):
    a,b,c=args[0][0],args[0][1],args[0][2]
    y=a*(x[0]-1)**2+b*x[1]**2-c*x[0]*x[1]
    return y

#ejemplo uso de funciones vectorizadas con args
params=[1.2,2.0,-1.0]
x=np.array([1.0,2.0,3.0])
print(f_obj(x,params))

#definir una funcion de x con parametros externos
def f_min(x):
    return f_obj(x,params)

print(f_min(x))

#minimizacion
initial_guess = [0.1, 0.5, -0.1]

resultado = minimize(
    f_min,
    initial_guess,
    method="BFGS"
)

print('Resultados minimizacion ',resultado.x)

resultado2 = minimize(
    f_obj,
    initial_guess,
    args=[1.2,2.0,-1.0],
    method="BFGS"
)  

print('resultados minimizacion ',resultado2.x)  

    
    