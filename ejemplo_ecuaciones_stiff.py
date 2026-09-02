#ejemplo de ecuacions stiff con ley de enfriamiento de Newton

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

C1=0.05
C2=500.0
UA=50.0
t0=5.0
Q0=100.0


def Q(t):
    if t<t0:
        y=0.0
    else:
        y=Q0
    return y    
    

def odes(t,y):
    T1,T2=y[0],y[1]
    z=np.zeros(2)
    z[0]=Q(t)/C1-UA*(T1-T2)/C1
    z[1]=UA*(T1-T2)/C2
    return z

T_ini=np.array([20.0,20.0])
t_domain=[0.0,100.0]
t_eval=np.linspace(0.0,100,100)

sol=solve_ivp(odes,t_domain,T_ini,method='BDF',t_eval=t_eval)

plt.figure()
plt.plot(sol.t,sol.y[0])
plt.xlabel('t')
plt.ylabel('T1')

plt.figure()
plt.plot(sol.t,sol.y[1])
plt.xlabel('t')
plt.ylabel('T2')






