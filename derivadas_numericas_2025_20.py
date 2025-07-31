#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 07:22:28 2025

@author: whadymacbook2016
"""
import numpy as np

def f(x):
    return np.sin(x)+x

def df(x):
    h=0.001*np.abs(x)
    derecha=(f(x+h)-f(x))/h
    izquierda=(f(x)-f(x-h))/h
    centrada=(f(x+h)-f(x-h))/(2*h)
    return derecha, izquierda,centrada

def df_exacta(x):
    return np.cos(x)+1

x=1.0

print(df(x),df_exacta(x))


