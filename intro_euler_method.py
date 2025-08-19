#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 11:24:15 2025

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    #dy=-0.01*(y-20)
    dy=-0.01*(y-(2+0.5*np.sin(0.1*x)))
    return dy

#def Texacta(t):
#    return 20+80*np.exp(-0.01*t)


t0=0.0 
tfinal=1000
T0=20.0 

n=80
h=(tfinal-t0)/n

tiempos=[]
Temp=[]
Temp_ex=[]

tiempos.append(t0)
Temp.append(T0)

for i in range(n):
    tnuevo=t0+h
    Tnueva=T0+h*f(t0,T0)
    tiempos.append(tnuevo)
    Temp.append(Tnueva)
    t0=tnuevo
    T0=Tnueva
    
#for i in tiempos:
#    Temp_ex.append(Texacta(i))
        

plt.plot(tiempos,Temp,'-')
#plt.plot(tiempos,Temp_ex,'r--')
plt.xlabel('tiempo')
plt.ylabel('Temperatura')

#plt.figure()
#error=np.array(Temp)-np.array(Temp_ex)
#plt.plot(tiempos,np.abs(error))

