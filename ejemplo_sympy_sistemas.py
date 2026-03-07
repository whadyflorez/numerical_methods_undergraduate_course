#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 07:47:24 2026

@author: whadymacbook2016
"""
from sympy import symbols, linsolve,latex,expand,diff,exp
from sympy import init_printing
from IPython.display import display

init_printing(use_latex=True)


# 1. Definir símbolos
a,b,c,d,x,y,p,q = symbols('a b c d x y p q')

# 2. Definir el sistema (se asume que cada expresión es igual a 0)
# Ejemplo: x + y = 5  y  x - y = 1
sistema = [a*x+b*y-p,c*x+d*y-q]

# 3. Resolver
solucion = linsolve(sistema, (x,y))
print(solucion)  # Salida: {(3, 2)}
display(solucion)
solucion_latex=latex(solucion)
x,y=list(solucion)[0]
display(x)
display(y)

#derivadas
x,y=symbols('x y')
derivada=diff(x**2*exp(-x),x,2)
display(derivada) 

