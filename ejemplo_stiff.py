import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Definir el sistema stiff de Robertson
def robertson(t, y):
    y1, y2, y3 = y
    dydt = [
        -0.04 * y1 + 1e4 * y2 * y3,
        0.04 * y1 - 1e4 * y2 * y3 - 3e7 * y2**2,
        3e7 * y2**2
    ]
    return dydt

# Condiciones iniciales
y0 = [1, 0, 0]  # Valores iniciales para y1, y2, y3
t_span = (0, 1e5)  # Intervalo de tiempo
t_eval = np.logspace(-6, 5, 200)  # Evaluamos en una escala logarítmica

# Resolver usando Radau (adecuado para sistemas stiff)
sol = solve_ivp(robertson, t_span, y0, method='LSODA', t_eval=t_eval)

# Graficar la solución
plt.figure(figsize=(8, 6))
plt.loglog(sol.t, sol.y[0], label=r'$y_1$', color='b')
plt.loglog(sol.t, sol.y[1], label=r'$y_2$', color='g')
plt.loglog(sol.t, sol.y[2], label=r'$y_3$', color='r')
plt.xlabel('Tiempo')
plt.ylabel('Concentraciones')
plt.legend()
plt.title('Solución del sistema stiff de Robertson')
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0], label=r'$y_1$', color='b')
plt.plot(sol.t, sol.y[1], label=r'$y_2$', color='g')
plt.plot(sol.t, sol.y[2], label=r'$y_3$', color='r')
plt.xlabel('Tiempo')
plt.ylabel('Concentraciones')
plt.legend()