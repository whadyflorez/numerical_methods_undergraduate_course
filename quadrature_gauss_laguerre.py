import numpy as np
import matplotlib.pyplot as plt
from scipy.special import roots_laguerre

# Definir la función g(x)
def g(x):
    return 1 / (1 + x**2)

# Número de puntos de Gauss-Laguerre
n_points = 20

# Obtener nodos y pesos de Gauss-Laguerre
nodes, weights = roots_laguerre(n_points)

# Calcular la integral aproximada
integral = np.sum(weights * g(nodes))

print(f"Integral aproximada usando Gauss-Laguerre con {n_points} puntos: {integral:.8f}")

# Para visualizar g(x) en un rango razonable
x_plot = np.linspace(0, 10, 400)
y_plot = g(x_plot)

plt.figure(figsize=(8,5))
plt.plot(x_plot, y_plot, label=r"$g(x) = \frac{1}{1+x^2}$", color='blue')
plt.scatter(nodes, g(nodes), color='red', label='Puntos de Gauss-Laguerre', zorder=5)
plt.title("Integración impropia con Gauss-Laguerre")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.grid(True)
plt.xlim(0, 10)
plt.show()
