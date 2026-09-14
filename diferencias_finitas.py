#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:06:32 2026

@author: whadymacbook2016
"""
import numpy as np

def f(x):
    return x[0]**2-2*x[0]*x[1]+x[1]**2 

def df(x):
    z=np.array([2*x[0]-2*x[1],-2*x[0]+2*x[1]])
    return z

def d2fdx2(x):
    return 2.0

def d2fdy2(x):
    return 2.0

xp=np.array([1.0,1.0])
dx=0.01
dy=0.01
xE=np.array([xp[0]+dx,xp[1]])
xW=np.array([xp[0]-dx,xp[1]])
xN=np.array([xp[0],xp[1]+dy])
xS=np.array([xp[0],xp[1]-dy])


dfdx_derecha=(f(xE)-f(xp))/dx
dfdx_izquierda=(f(xp)-f(xW))/dx
dfdx_centrada=(f(xE)-f(xW))/(2*dx)

dfdx_exacta=df(xp)[0]

d2fdx2_numerica=(f(xE)-2*f(xp)+f(xW))/dx**2


print('dfdx derecha',dfdx_derecha)
print('dfdx izquierda',dfdx_izquierda)
print('dfdx centrada',dfdx_centrada)
print('exacta',dfdx_exacta)
print('--------')
print('d2fdx2 exxacto',d2fdx2(xp))
print('d2fdx2 numerica',d2fdx2_numerica)

