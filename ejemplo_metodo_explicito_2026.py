#ejemplo diferencias finitas dependientes del tiempo metodo explicito

import numpy as np
import matplotlib.pyplot as plt

L=2.5 
n=30
dx=L/(n-1)
dt=0.0001
tfinal=1.0 
n_pasos=int(tfinal/dt)
u_i=20.0
c=0.2 

u_presente=np.zeros(n)
u_futuro=np.zeros(n)
H=np.zeros((n,n_pasos+1))


# #primer paso
# u_presente[1:n-1]=u_i
# H[:,0]=u_presente

# for j in range(1,n-1):
#     u_futuro[j]=(dt/c)*(u_presente[j+1]-2*u_presente[j]\
#                         +u_presente[j-1])/dx**2+u_presente[j]
# u_futuro[0]=0.0        
# u_futuro[n-1]=0.0 
# H[:,1]=u_futuro 

# #segundo paso
# u_presente=u_futuro.copy()  
# for j in range(1,n-1):
#     u_futuro[j]=(dt/c)*(u_presente[j+1]-2*u_presente[j]\
#                         +u_presente[j-1])/dx**2+u_presente[j]
# u_futuro[0]=0.0        
# u_futuro[n-1]=0.0      
# H[:,2]=u_futuro 

u_presente[1:n-1]=u_i
H[:,0]=u_presente
    
for k in range(1,n_pasos+1):     
    for j in range(1,n-1):
        u_futuro[j]=(dt/c)*(u_presente[j+1]-2*u_presente[j]\
                            +u_presente[j-1])/dx**2+u_presente[j]
    u_futuro[0]=0.0        
    u_futuro[n-1]=0.0 
    H[:,k]=u_futuro  
    u_presente=u_futuro.copy()
 
    
x=np.linspace(0,L,n) 
tiempo=np.linspace(0,tfinal,n_pasos+1)

plt.figure()
plt.plot(x,H[:,0])
plt.plot(x,H[:,1000])
plt.plot(x,H[:,2000])
plt.xlabel('x')
plt.ylabel('u')

plt.figure()
plt.plot(tiempo,H[0,:])
plt.plot(tiempo,H[15,:])    
plt.plot(tiempo,H[20,:]) 
plt.xlabel('t')
plt.ylabel('u')   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



