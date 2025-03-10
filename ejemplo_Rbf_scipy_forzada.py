#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:40:00 2025

@author: whadymacbook2016
"""
import numpy as np
from scipy.interpolate import Rbf

x=[0,1,2,3,4]
y=[0,0,0,0,0]
z=[0,0,0,0,0]
d=np.sin(x)

finterp=Rbf(x,y,z,d)

xinterp=[2.5,0,0]
z=finterp(xinterp[0],xinterp[1],xinterp[2])