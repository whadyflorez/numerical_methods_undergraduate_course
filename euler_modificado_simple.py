#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 11:24:15 2025

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    dy=-y
    return dy

#def Texacta(t):
#    return 20+80*np.exp(-0.01*t)


x0=0.0 
y0=1
xfinal=10


n=10
h=(xfinal-x0)/n

xvalues=[]
yvalues=[]
y_ex=[]

xvalues.append(x0)
yvalues.append(y0)

for i in range(n):
    xnuevo=x0+h
    k1=f(x0,y0)
    ynueva_s=y0+h*k1
    k2=f(xnuevo,ynueva_s)
    ynueva=y0+h*0.5*(k1+k2)    
    xvalues.append(xnuevo)
    yvalues.append(ynueva)
    x0=xnuevo
    y0=ynueva
    
#for i in tiempos:
#    Temp_ex.append(Texacta(i))
        

plt.plot(xvalues,yvalues,'-')
#plt.plot(xvalues,y_ex,'r--')
plt.xlabel('x')
plt.ylabel('y')

#plt.figure()
#error=np.array(Temp)-np.array(Temp_ex)
#plt.plot(tiempos,np.abs(error))


