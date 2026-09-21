#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:30:07 2026

@author: whadymacbook2016
"""
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    z=x**2+y**2
    return z

x=np.linspace(-10.0,10.0,100)
y=np.linspace(-5.0,5.0,100)
X, Y = np.meshgrid(x, y)
Z=f(X,Y)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.plot_surface(X, Y, Z, color='C0')

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z,100)
ax.clabel(CS, fontsize=10)
ax.set_title('Simplest default with labels')