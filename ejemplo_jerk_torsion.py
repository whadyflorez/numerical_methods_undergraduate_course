import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros del sistema
J = 10.0     # kg·m^2 (inercia)
c = 5.0      # N·m·s/rad (amortiguamiento)
k = 200.0    # N·m/rad (rigidez torsional)
M0 = 100.0   # N·m (amplitud del momento aplicado)
Omega = 5.0  # rad/s (frecuencia de excitación)


def rhs(t, z):
    theta, u, w = z
    dy=np.array([u,w,10*np.sin(5*t)-0.5*w-20*u])
    return dy

# Condiciones iniciales: en reposo
z0 = [0.0, 0.0, 0.0]

# Intervalo de tiempo
t_span = (0.0, 20.0)  # 20 segundos
t_eval = np.linspace(0, 20, 1000)

# Resolver
sol = solve_ivp(rhs, t_span, z0, t_eval=t_eval)

# Resultados
t = sol.t
theta = sol.y[0]   # desplazamiento angular
u = sol.y[1]   # velocidad angular
w = sol.y[2]   # aceleración angular

jerk=10*np.sin(5*t)-0.5*w-20*u

# Gráficas con formato LaTeX
plt.figure()
plt.plot(t, theta)
plt.xlabel(r"$t$")
plt.ylabel(r"$\theta(t)$")
plt.grid(True)


plt.figure()
plt.plot(t, u)
plt.xlabel(r"$t$")
plt.ylabel(r"$u(t)$")
plt.grid(True)

plt.figure()
plt.plot(t, w)
plt.xlabel(r"$t$")
plt.ylabel(r"$w(t)$")
plt.grid(True)

plt.figure()
plt.plot(t, jerk)
plt.xlabel(r"$t$")
plt.ylabel(r"$jerk(t)$")
plt.grid(False)

plt.show()
