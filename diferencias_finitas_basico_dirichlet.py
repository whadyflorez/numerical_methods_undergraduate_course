#ejemplo diferencias finitas en 2D basico
import numpy as np
import matplotlib.pyplot as plt

L=1.0
dx=L/4
dy=L/4
n=25

A=np.zeros((n,n))
B=np.zeros(n)

l_internos=[6,7,8,11,12,13,16,17,18]
l_base=[0,1,2,3,4]
l_izquierda=[5,10,15]
l_arriba=[20,21,22,23,24]
l_derecha=[9,14,19]

for i in l_internos:
    A[i,i+1]=1.0/dx**2
    A[i,i-1]=1.0/dx**2
    A[i,i+5]=1.0/dy**2
    A[i,i-5]=1.0/dy**2
    A[i,i]=-2.0/dx**2-2.0/dy**2
    B[i]=0.0
for i in l_base:
    A[i,i]=1.0
    B[i]=0.0
for i in l_derecha:
    A[i,i]=1.0 
    B[i]=0.0
for i in l_izquierda:
    A[i,i]=1.0
    B[i]=0.0
for i in l_arriba:
    A[i,i]=1.0
    B[i]=1.0

T=np.linalg.solve(A,B)    

Resultados=np.zeros((5,5))

Resultados[4,:]=T[0:5]
Resultados[3,:]=T[5:10]
Resultados[2,:]=T[10:15]
Resultados[1,:]=T[15:20]
Resultados[0,:]=T[20:25]
    
plt.spy(A)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    