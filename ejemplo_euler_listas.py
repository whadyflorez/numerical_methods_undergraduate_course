#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#ejemplo de metodo de Euler para la ecuacion de enfriamiento de newton
"""
Created on Wed Jul 15 08:53:27 2020

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt

U=0.01
tini=0.0
tfinal=20*60
Tini=35.0
#Tm=20
n=1000
dt=(tfinal-tini)/n #paso

def Tm(t):
    y=2+np.sin(0.25*t)
    return y

def F(t,T):
    valor=-U*(T-Tm(t)) #estudiar jerarquia de los operadores
    return valor



tiempos=[]
T=[]
tiempos.append(tini)
T.append(Tini)

for i in range(0,n):
    T.append(T[i]+dt*F(tiempos[i],T[i]))
    tiempos.append(tiempos[i]+dt)

#Texacta=[100]
#for i in range(0,n):
#    Texacta.append(Tm+80*np.exp(-U*tiempos[i]))    
    
plt.figure()
plt.plot(tiempos,T,'-',label='numerica') 
#plt.plot(tiempos,Texacta,'-',label='exacta')  
plt.xlabel('tiempo') 
plt.ylabel('Temperatura2')
plt.legend()



    

