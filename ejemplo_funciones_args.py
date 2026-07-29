import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#Generar conjuntos de datos
np.random.seed(12)

x = np.linspace(-4, 5, 16)
a_real, b_real, c_real = 1.2, -2.0, 4.0
ruido = np.random.normal(0, 2.5, len(x))

y = a_real * x**2 + b_real * x + c_real+ruido

plt.plot(x,y,'o',color='red')

#definicion de funciones
def gato(x):
    y=x**2
    return y
print(gato(1.2))
print(gato(3.0))
u=np.array([0.0,1.0,5.0])
print(gato(u))

#funciones de varias variables
def fvv(x,y):
    z=x**2+y**2
    return z
print('f(x,y)=',fvv(1.0,3.0))

#funciones de variable vectorial
def f_vector(x):
    y=x[0]**2+x[1]**2
    return y
print('funcion vectorial(x)=',f_vector(np.array([1,3])))


#funciones con parametros

def modelo(parametros, x):
    a, b, c = parametros
    return a * x**2 + b * x + c

parametros=[0.5,1.0,-1.2]
print('funcion con parametros ',modelo(parametros,2.5))
print('funcion con parametros ',modelo(parametros,4.0))
parametros=[1.0,0.0,3.2]
print('funcion con parametros ',modelo(parametros,4.0))
print('funcion con parametros ',modelo(parametros,x))

#funcion de 1 variable con parametros fijos definida apartir de otra funcion

def f(x):
    y=modelo(parametros,x)
    return y
print('funcion con parametros fijos ',f(2.7))

def funcion_args(x,*args):
    y=args[0]*x+args[1]*np.sin(x)
    return y

params=[0.5,1.2]
print(funcion_args(np.pi/3,params[0],params[1]))


#como llamar una funcion compuesta
def pajaro(x):
    y=np.sin(x)+2.0
    return y

def carro(x):
    y=np.tanh(x)
    return y

print('funcion compuesta',pajaro(carro(1.1)))

