#aproximacion por minimos cuadrados
import numpy as np
import matplotlib.pyplot as plt

T=np.zeros((6,2))
T[:,0]=[8.0,7.0,6.0,4.0,2.0,1.0]
T[:,1]=[15.0,19.0,25.0,23.0,34.0,40]


n=6

C=np.zeros((n,2)) 
y=T[:,1]

C[:,0]=np.ones(n)
C[:,1]=T[:,0]

CTC=C.T@C
CTy=C.T@y

a=np.linalg.solve(CTC,CTy)

def modelo(x):
    y=a[0]+a[1]*x
    return y

Pred=np.zeros((n,2))
Pred[:,0]=T[:,0]
Pred[:,1]=modelo(T[:,0])


plt.figure()
plt.plot(T[:,0],T[:,1],'o')
plt.plot(T[:,0],Pred[:,1],'--r')

vect_error=(T[:,1]-Pred[:,1])**2
Error_tot=np.sum(vect_error)










