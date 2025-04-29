import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

# Definir la función a integrar
def f(x):
    return np.exp(-x**2)

# Número de puntos de Gauss
n_points = 24

# Obtener nodos (puntos) y pesos de Gauss-Legendre
nodes, weights = leggauss(n_points)

# Calcular la integral como suma ponderada
integral = np.sum(weights * f(nodes))

# Mostrar resultado
print(f"Integral aproximada con {n_points} puntos de Gauss: {integral:.6f}")

# Graficar la función y los puntos de Gauss
x_plot = np.linspace(-1, 1, 400)
y_plot = f(x_plot)

plt.figure(figsize=(8,5))
plt.plot(x_plot, y_plot, label=r"$f(x) = e^{-x^2}$", color='blue')
plt.scatter(nodes, f(nodes), color='red', label='Puntos de Gauss', zorder=5)
plt.title(f"Integración Gaussiana con {n_points} puntos")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
