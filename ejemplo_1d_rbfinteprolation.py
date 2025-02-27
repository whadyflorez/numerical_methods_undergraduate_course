import numpy as np
import matplotlib.pyplot as plt

# Función base radial multicuádrica
def multiquadric_rbf(r, c):
    return np.sqrt(r**2 + c**2)

# Datos conocidos (nodos de interpolación)
x_nodes = np.linspace(-5, 5, 10)
y_nodes = np.sin(x_nodes)

# Parámetro de forma
c = 1.0

# Construcción de la matriz A para interpolación
A = np.zeros((len(x_nodes), len(x_nodes)))
for i in range(len(x_nodes)):
    for j in range(len(x_nodes)):
        A[i, j] = multiquadric_rbf(abs(x_nodes[i] - x_nodes[j]), c)

# Resolviendo el sistema para encontrar los coeficientes
coeffs = np.linalg.solve(A, y_nodes)

# Puntos de evaluación
x_eval = np.linspace(-5, 5, 100)
y_interp = np.zeros_like(x_eval)

# Aplicar interpolación
for i in range(len(x_eval)):
    for j in range(len(x_nodes)):
        y_interp[i] += coeffs[j] * multiquadric_rbf(abs(x_eval[i] - x_nodes[j]), c)

# Graficar resultados
plt.figure(figsize=(8, 5))
plt.plot(x_nodes, y_nodes, 'ro', label='Nodos')
plt.plot(x_eval, y_interp, 'b-', label='Interpolación RBF')
plt.plot(x_eval, np.sin(x_eval), 'g--', label='Función real')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación con RBF Multicuádrica')
plt.show()
