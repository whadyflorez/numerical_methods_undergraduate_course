#ejemplo de interpolacion en tabla de propiedades del amoniaco

import numpy as np
from scipy.linalg import solve

data=np.array([[400.0,0.5136],[420.0,0.4888],\
             [460.0,0.4460],[480.0,0.4273],\
                 [500.0,0.4101],[540.0,0.3795]])

ndata=np.shape(data)[0]    
    
#formar el sistema de ecuaciones
A=np.zeros((ndata,ndata))
B=data[:,1].copy()

for i in range(ndata):
    for j in range(ndata):
        A[i,j]=data[i,0]**j
        
p=solve(A,B)        

def m(x):
   suma=0.0
   for i in range(ndata):
       suma+=p[i]*x**i
   return suma  

print(m(490.0))    