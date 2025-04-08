import numpy as np
import matplotlib.pyplot as plt

# Punto fijo y extremos del segmento
x = np.array([1.0, 1.0])
p = np.array([0.0, 0.0])
q = np.array([2.0, 0.0])

# Puntos para graficar r(xi)
xi_vals = np.linspace(-1, 1, 100)
r_vals = []

for xi in xi_vals:
    N1 = 0.5 * (1 - xi)
    N2 = 0.5 * (1 + xi)
    z = N1 * p + N2 * q
    r = np.linalg.norm(z - x)
    r_vals.append(r)

# Convertir a arreglo de numpy para graficar
r_vals = np.array(r_vals)

# Graficar
plt.figure(figsize=(8, 5))
plt.plot(xi_vals, r_vals, label=r'$r(\xi) = \|\mathbf{z}(\xi) - \mathbf{x}\|$')
plt.xlabel(r'$\xi$ (parámetro en [-1, 1])')
plt.ylabel(r'$r(\xi)$ (distancia al punto fijo)')
plt.title('Comportamiento del integrando $r(\\xi)$ a lo largo del segmento')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
