

import numpy as np

def f(x):
    y=x**2*np.sin(x)
    return y

x=2.0
dx=0.001

def df(g,x,dx):
    dy=(-3*g(x)+4*g(x+dx)-g(x+2*dx))/(2*dx)
    return dy

def d2f(g,x,dx):
    d2y=(2*g(x)-5*g(x+dx)+4*g(x+2*dx)-g(x+3*dx))/dx**2
    return d2y

def dexacta(x):
    dy=2*x*np.sin(x)+x**2*np.cos(x)
    d2y=2*np.sin(x)+2*x*np.cos(x)+2*x*np.cos(x)-x**2*np.sin(x)
    return dy,d2y

print(df(f,x,dx))
print(d2f(f,x,dx))
print(dexacta(x))

def h(x,y):
    z=x**2+y**2 
    return z

def dh(h,x,y,dx,dy):
    dh_x=(h(x+dx,y)-h(x-dx,y))/(2*dx)
    dh_y=(h(x,y+dy)-h(x,y-dy))/(2*dy)
    return dh_x,dh_y

x=1.0
y=3.0 
dx=0.01
dy=0.005

print(dh(h,x,y,dx,dy))
    
    
    