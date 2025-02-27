import numpy as np
import matplotlib.pyplot as plt

# Función base radial multicuádrica
def multiquadric_rbf(r, c):
    return np.sqrt(r**2 + c**2)

# Funciones de aumento explícitas
def augmentation_functions(x):
#    return np.vstack((np.ones_like(x), np.sin(x), np.cos(x))).T  # Términos constantes, lineales y cuadráticos
    return np.vstack((np.ones_like(x), x, x**2)).T  # Términos constantes, lineales y cuadráticos

# Datos conocidos (nodos de interpolación)
x_nodes = np.linspace(-5, 5, 10)
y_nodes = np.sin(x_nodes)

# Parámetro de forma
c = 1.0

# Construcción de la matriz A para interpolación con términos de aumento
n = len(x_nodes)
A = np.zeros((n + 3, n + 3))
for i in range(n):
    for j in range(n):
        A[i, j] = multiquadric_rbf(abs(x_nodes[i] - x_nodes[j]), c)

# Agregar términos de aumento
P = augmentation_functions(x_nodes)
A[:n, n:] = P
A[n:, :n] = P.T

# Construcción del vector de resultados
b = np.zeros(n + 3)
b[:n] = y_nodes

# Resolviendo el sistema para encontrar los coeficientes
coeffs = np.linalg.solve(A, b)

# Puntos de evaluación
x_eval = np.linspace(-5, 5, 100)
y_interp = np.zeros_like(x_eval)

# Aplicar interpolación
for i in range(len(x_eval)):
    for j in range(n):
        y_interp[i] += coeffs[j] * multiquadric_rbf(abs(x_eval[i] - x_nodes[j]), c)
#    y_interp[i] += coeffs[n] + coeffs[n+1] * np.sin(x_eval[i]) + coeffs[n+2] * np.cos(x_eval[i])  # Aplicar términos de aumento
    y_interp[i] += coeffs[n] + coeffs[n+1] * x_eval[i] + coeffs[n+2] * x_eval[i]**2  # Aplicar términos de aumento

# Graficar resultados
plt.figure(figsize=(8, 5))
plt.plot(x_nodes, y_nodes, 'ro', label='Nodos')
plt.plot(x_eval, y_interp, 'b-', label='Interpolación RBF con aumento')
plt.plot(x_eval, np.sin(x_eval), 'g--', label='Función real')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación con RBF Multicuádrica y Términos de Aumento {1, x, x²}')
plt.show()
