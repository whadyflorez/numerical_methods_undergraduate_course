#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 06:03:46 2025

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 1.0, 4, 9, 16, 25])
z = np.polyfit(x, y, 2)

p = np.poly1d(z)
print(p(1.0))

xp = np.linspace(0,5, 100)
yp=p(xp)
plt.plot(x, y, 'o', xp, yp, '--')
