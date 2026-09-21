# Ecuación de Laplace en 2D mediante diferencias finitas
# Cuadrado unitario:
# T = 0 en base, izquierda y derecha
# T = 1 en la frontera superior

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ---------------------------------------------------------
# 1. Dominio y malla
# ---------------------------------------------------------
L = 1.0

# 20 intervalos generan 21 nodos en cada dirección
n_intervalos = 20

dx = L / n_intervalos
dy = L / n_intervalos

Nx = n_intervalos + 1
Ny = n_intervalos + 1

# Número total de nodos
n = Nx * Ny

# ---------------------------------------------------------
# 2. Función para identificar cada nodo en el vector T
# ---------------------------------------------------------
# i: columna (coordenada x)
# j: fila    (coordenada y)
def indice(i, j):
    return j * Nx + i

# ---------------------------------------------------------
# 3. Construcción del sistema A*T = B
# ---------------------------------------------------------
A = np.zeros((n, n))
B = np.zeros(n)

for j in range(Ny):
    for i in range(Nx):

        k = indice(i, j)

        # Frontera superior: T = 1
        if j == Ny - 1:
            A[k, k] = 1.0
            B[k] = 1.0

        # Base, lado izquierdo y lado derecho: T = 0
        elif j == 0 or i == 0 or i == Nx - 1:
            A[k, k] = 1.0
            B[k] = 0.0

        # Nodo interior:
        # d2T/dx2 + d2T/dy2 = 0
        else:
            A[k, indice(i + 1, j)] = 1.0 / dx**2
            A[k, indice(i - 1, j)] = 1.0 / dx**2
            A[k, indice(i, j + 1)] = 1.0 / dy**2
            A[k, indice(i, j - 1)] = 1.0 / dy**2

            A[k, k] = -2.0 / dx**2 - 2.0 / dy**2
            B[k] = 0.0

# ---------------------------------------------------------
# 4. Solución numérica
# ---------------------------------------------------------
T = np.linalg.solve(A, B)

# ---------------------------------------------------------
# 5. Construcción manual de X, Y y Resultados
# ---------------------------------------------------------
X = np.zeros((Ny, Nx))
Y = np.zeros((Ny, Nx))
Resultados = np.zeros((Ny, Nx))

for j in range(Ny):
    for i in range(Nx):

        X[j, i] = i * dx
        Y[j, i] = j * dy
        Resultados[j, i] = T[indice(i, j)]

# ---------------------------------------------------------
# 6. Mostrar la estructura de A
# ---------------------------------------------------------
plt.figure(figsize=(7, 7))
plt.spy(A, markersize=1)
plt.title("Estructura de la matriz A: malla de 21 x 21 nodos")
plt.xlabel("Columnas")
plt.ylabel("Filas")
plt.show()

# ---------------------------------------------------------
# 7. Gráfica de superficie 3D
# ---------------------------------------------------------
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

superficie = ax.plot_surface(
    X,
    Y,
    Resultados,
    cmap="hot",
    edgecolor="black",
    linewidth=0.15
)

ax.set_title("Distribución de temperatura en la placa")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Temperatura")

fig.colorbar(superficie, ax=ax, label="Temperatura")
plt.show()

# ---------------------------------------------------------
# 8. Contornos de temperatura
# ---------------------------------------------------------
plt.figure(figsize=(7, 6))

contornos = plt.contourf(
    X,
    Y,
    Resultados,
    levels=20,
    cmap="hot"
)

plt.contour(
    X,
    Y,
    Resultados,
    levels=20,
    colors="black",
    linewidths=0.4
)

plt.colorbar(contornos, label="Temperatura")
plt.title("Curvas de nivel de temperatura")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.show()