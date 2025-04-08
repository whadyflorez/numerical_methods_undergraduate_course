import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Función de Rosenbrock
def f(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

# Punto inicial
x0 = np.array([-1.5, 1.5])

# Lista para guardar las iteraciones
path = []

# Función que guarda el camino de la optimización
def callback(xk):
    path.append(np.copy(xk))

# Ejecutamos la optimización
res = minimize(f, x0, method='BFGS', callback=callback, options={'disp': True})

# Agregamos también el punto inicial
path.insert(0, x0)

# Convertimos la trayectoria en un array
path = np.array(path)

# Generamos la malla para el gráfico de contorno
x = np.linspace(-2, 2, 400)
y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(x, y)
Z = f([X, Y])

# Graficamos
plt.figure(figsize=(10, 6))
contours = plt.contour(X, Y, Z, levels=np.logspace(-1, 3.5, 20), linewidths=1)
plt.clabel(contours, inline=True, fontsize=8)
plt.plot(path[:, 0], path[:, 1], 'ro--', label='Trayectoria')
plt.plot(path[0, 0], path[0, 1], 'go', label='Inicio')
plt.plot(path[-1, 0], path[-1, 1], 'bo', label='Mínimo')
plt.title("Optimización de la función de Rosenbrock")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
