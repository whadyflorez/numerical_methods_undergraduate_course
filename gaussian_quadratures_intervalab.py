import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

# Definir la función a integrar
def f(x):
    return np.exp(-x**2)

# Número de puntos de Gauss
n_points = 5

# Intervalo [a,b]
a = 0
b = 2

# Obtener nodos (puntos) y pesos de Gauss-Legendre en [-1,1]
xi, wi = leggauss(n_points)

# Cambio de variable: transformar nodos a [a,b]
x_nodes = 0.5 * (b - a) * xi + 0.5 * (b + a)
weights = 0.5 * (b - a) * wi

# Calcular la integral como suma ponderada
integral = np.sum(weights * f(x_nodes))

# Mostrar resultado
print(f"Integral aproximada en [{a}, {b}] con {n_points} puntos de Gauss: {integral:.6f}")

# Graficar la función y los puntos de Gauss transformados
x_plot = np.linspace(a, b, 400)
y_plot = f(x_plot)

plt.figure(figsize=(8,5))
plt.plot(x_plot, y_plot, label=r"$f(x) = e^{-x^2}$", color='blue')
plt.scatter(x_nodes, f(x_nodes), color='red', label='Puntos de Gauss transformados', zorder=5)
plt.title(f"Integración Gaussiana en [{a}, {b}] con {n_points} puntos")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
