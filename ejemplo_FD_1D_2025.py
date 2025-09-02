import numpy as np
import matplotlib.pyplot as plt

n=15
L=1
dx=L/(n-1)
m=10
Tizq=20
Tder=100
x=np.linspace(0,L,n)


A=np.zeros((n,n))
B=np.zeros(n)

for i in range(n):
    if i==0:
      A[i,i]=1  
      B[i]=Tizq
    if i>0 and i<n-1:
      A[i,i+1]=1/dx**2
      A[i,i]=-2/dx**2-m
      A[i,i-1]=1/dx**2
      B[i]=0
    if i==n-1:
      A[i,i]= 1
      B[i]=Tder
      
#plt.spy(A)  

T=np.linalg.solve(A,B)    

plt.plot(x,T,'-+')
plt.xlabel('x')
plt.ylabel('T(x)')  



