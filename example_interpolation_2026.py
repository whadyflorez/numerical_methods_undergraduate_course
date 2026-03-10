import numpy as np
import matplotlib.pyplot as plt

n=7
T=np.array([240.0,255.0,270.0,285.0,300.0,310.0,365.0])
k=np.array([0.036,0.038,0.040,0.043,0.048,0.052,0.076])


A=np.zeros((n,n))
B=np.zeros(n)

for i in range(n):
    for j in range(n):
        A[i,j]=T[i]**j
    B[i]=k[i]   
    
a=np.linalg.solve(A,B)    

def P(T):
    s=0.0
    for i in range(n):
        s+=a[i]*T**i
    return s
    
print('T=',340.0,'k=',P(340.0))   

plt.figure()
plt.plot(T,k,'o')
plt.plot(340.0,P(340.0),'or')
plt.plot(380.0,P(380.0),'or')
plt.xlabel('T')
plt.ylabel('k')


 
    
    
    
    
    