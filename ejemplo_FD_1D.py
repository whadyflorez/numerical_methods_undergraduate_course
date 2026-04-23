# ejemplo diferencias finitas

import numpy as np
import matplotlib.pyplot as plt


n=6

A=np.zeros((n,n))
B=np.zeros(n)

h=1.0/(n-1)

q=100.0

for i in range(n):
    for j in range(n):
        if i==0:
            A[i,i],B[i]=1.0,0.0
        if i>0 and i<n-1:
            A[i,i+1]=1.0/h**2
            A[i,i]=-2.0/h**2 
            A[i,i-1]=1.0/h**2
            B[i]=-q
        if i==n-1:
#            A[i,i],B[i]=1.0,0.0
            A[i,i]=1.0/h
            A[i,i-1]=-1.0/h
            B[i]=0
            
plt.spy(A)

T=np.linalg.solve(A,B)
 
x=np.linspace(0,1,n)  

plt.figure()
plt.plot(x,T,'-o')
plt.xlabel('x')
plt.ylabel('T')        
            
            
            
            
            
            
            
            
            
            
            
            
            



