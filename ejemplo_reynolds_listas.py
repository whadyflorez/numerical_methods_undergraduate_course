#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 06:11:33 2025

@author: whadymacbook2016
"""
import numpy as np

mu=1.0e-3 #Pa.s
rho=1000.0 #kg/m^3
V=0.025 #m/s
D=2.0e-2 #m

Re=V*rho*D/mu

def funcion_Re(vel,diam,visc,dens):
    f=vel*diam*dens/visc
    return f

def Re_lista(lista):
    f=lista[0]*lista[1]*lista[3]/lista[2]
    return f
    

print('Re=',Re)
print('Re funcion=',funcion_Re(V,D,mu,rho))

lista_variables=[V,D,mu,rho]
print('Re_lista=',Re_lista(lista_variables))

if Re <= 2300.0:
    clasificacion='laminar'
if Re>2300.0 and Re<4000.0:
    clasificacion='transición'
if Re>=4000.0:
    clasificacion='turbulento'
   
def funcion_clasificacion(Re):
    if Re <= 2300.0:
        clasificacion='laminar'
    if Re>2300.0 and Re<4000.0:
        clasificacion='transición'
    if Re>=4000.0:
        clasificacion='turbulento' 
    return clasificacion   

print('El tipo de flujo es ',funcion_clasificacion(Re))    














