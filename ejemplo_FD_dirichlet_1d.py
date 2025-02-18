import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

# Parámetros del problema
L = 1.0  # Longitud del dominio
N = 50  # Número de puntos internos
h = L / (N + 1)  # Tamaño del paso espacial

# Discretización del dominio
x = np.linspace(0, L, N + 2)  # Incluye los puntos de frontera

# Función fuente f(x)
def f(x):
    return np.sin(np.pi * x)

# Construcción de la matriz del sistema lineal
A = np.zeros((N, N))  # Matriz de coeficientes
b = np.zeros(N)        # Vector de términos independientes

# Llenar la matriz y el vector de términos independientes
for i in range(N):
    A[i, i] = -2 / h**2  # Elemento diagonal
    if i > 0:
        A[i, i - 1] = 1 / h**2  # Elemento de la izquierda
    if i < N - 1:
        A[i, i + 1] = 1 / h**2  # Elemento de la derecha
    b[i] = -f(x[i + 1])  # Evaluamos f(x) en los nodos internos

# Condiciones de frontera
alpha = 0  # u(0) = 0
beta = 1   # u(L) = 1

# Modificar b para incluir las condiciones de frontera
b[0] -= alpha / h**2
b[-1] -= beta / h**2

# Resolver el sistema lineal
u_interior = solve(A, b)

# Agregar las condiciones de frontera
u = np.zeros(N + 2)
u[0] = alpha
u[-1] = beta
u[1:N+1] = u_interior

# Graficar la solución
plt.plot(x, u, label="Solución Numérica", marker="o")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.legend()
plt.grid()
plt.show()

