# =========================================================
# ECUACIÓN DE LAPLACE 2D EN UNA GEOMETRÍA EN L
# DIFERENCIAS FINITAS CON CONECTIVIDAD N, S, P, E, W
# =========================================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ---------------------------------------------------------
# 1. Numeración de nodos según la figura
# ---------------------------------------------------------
# Cada lista representa una fila de nodos de la geometría.
# El índice de la fila corresponde a y.
# La posición dentro de cada fila corresponde a x.

filas_de_nodos = [
    [0, 1, 2, 3, 4, 5, 6],        # y = 0
    [7, 8, 9, 10, 11, 12, 13],    # y = 1
    [14, 15, 16, 17, 18, 19, 20], # y = 2
    [21, 22, 23, 24],             # y = 3
    [25, 26, 27, 28]              # y = 4
]

# Diccionarios para pasar de número de nodo a coordenada,
# y de coordenada a número de nodo.
nodo_a_coord = {}
coord_a_nodo = {}

for j, fila in enumerate(filas_de_nodos):
    for i, nodo in enumerate(fila):
        nodo_a_coord[nodo] = (i, j)
        coord_a_nodo[(i, j)] = nodo

n = len(nodo_a_coord)

# Tamaño de cada celda
dx = 1.0
dy = 1.0

# ---------------------------------------------------------
# 2. Condiciones de frontera
# ---------------------------------------------------------
# T = 1 en la frontera interior de la L.
nodos_T1 = {17, 18, 19, 20, 24}

# T = 0 en las fronteras exteriores.
nodos_T0 = {
    0, 1, 2, 3, 4, 5, 6,       # frontera inferior
    7, 13,                      # extremos de la fila y = 1
    14,                         # lado izquierdo, y = 2
    21,                         # lado izquierdo, y = 3
    25, 26, 27, 28              # frontera superior
}

nodos_frontera = nodos_T0.union(nodos_T1)
nodos_internos = sorted(set(nodo_a_coord.keys()) - nodos_frontera)

print("Nodos internos:", nodos_internos)

# ---------------------------------------------------------
# 3. Función de conectividad tipo Patankar
# ---------------------------------------------------------
#            N
#            |
#       W -- P -- E
#            |
#            S

def obtener_vecinos(P):
    x, y = nodo_a_coord[P]

    vecinos = {
        "N": coord_a_nodo.get((x, y + 1)),
        "S": coord_a_nodo.get((x, y - 1)),
        "E": coord_a_nodo.get((x + 1, y)),
        "W": coord_a_nodo.get((x - 1, y))
    }

    return vecinos

conectividad = {}

for P in nodos_internos:
    conectividad[P] = obtener_vecinos(P)

# ---------------------------------------------------------
# 4. Ejemplo didáctico: nodo P = 15
# ---------------------------------------------------------
P = 15
vecinos_15 = conectividad[P]

print("\nConectividad para el nodo P = 15:")
print("N =", vecinos_15["N"])
print("S =", vecinos_15["S"])
print("E =", vecinos_15["E"])
print("W =", vecinos_15["W"])

# Para el nodo 15:
#
# N = 22
# S = 8
# E = 16
# W = 14
#
# 4*T15 - T22 - T8 - T16 - T14 = 0

# ---------------------------------------------------------
# 5. Ensamblaje del sistema A*T = B
# ---------------------------------------------------------
A = np.zeros((n, n))
B = np.zeros(n)

for P in range(n):

    # Condición de frontera T = 0
    if P in nodos_T0:
        A[P, P] = 1.0
        B[P] = 0.0

    # Condición de frontera T = 1
    elif P in nodos_T1:
        A[P, P] = 1.0
        B[P] = 1.0

    # Nodo interior: ecuación de Laplace
    else:
        vecinos = conectividad[P]

        # Coeficientes de difusión
        aE = 1.0 / dx**2
        aW = 1.0 / dx**2
        aN = 1.0 / dy**2
        aS = 1.0 / dy**2

        # Coeficiente central
        ap = aE + aW + aN + aS

        # Ecuación:
        # ap*T_P - aE*T_E - aW*T_W - aN*T_N - aS*T_S = 0

        A[P, P] = ap
        A[P, vecinos["E"]] = -aE
        A[P, vecinos["W"]] = -aW
        A[P, vecinos["N"]] = -aN
        A[P, vecinos["S"]] = -aS

        B[P] = 0.0

# Mostrar la fila de la matriz correspondiente al nodo 15
print("\nCoeficientes de la fila asociada al nodo 15:")
print("A[15,15] =", A[15, 15], "  coeficiente de T15")
print("A[15,22] =", A[15, 22], "  vecino Norte")
print("A[15,8]  =", A[15, 8], "   vecino Sur")
print("A[15,16] =", A[15, 16], "  vecino Este")
print("A[15,14] =", A[15, 14], "  vecino Oeste")

print("\nEcuación para el nodo 15:")
print("4*T15 - T22 - T8 - T16 - T14 = 0")

# ---------------------------------------------------------
# 6. Resolver el sistema
# ---------------------------------------------------------
T = np.linalg.solve(A, B)

# ---------------------------------------------------------
# 7. Construcción manual de las matrices X, Y y Z
# ---------------------------------------------------------
# X e Y corresponden al rectángulo auxiliar de 7 x 5 nodos.
# Z contiene NaN fuera de la geometría real en L.

X = np.zeros((5, 7))
Y = np.zeros((5, 7))
Z = np.full((5, 7), np.nan)

for j in range(5):
    for i in range(7):
        X[j, i] = i * dx
        Y[j, i] = j * dy

# Solo se asigna una temperatura en los nodos existentes.
for nodo, (x, y) in nodo_a_coord.items():
    Z[y, x] = T[nodo]

# Matriz enmascarada: oculta los NaN al graficar.
Z_mascara = np.ma.masked_invalid(Z)

# ---------------------------------------------------------
# 8. Visualizar la malla y la numeración
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))

for nodo, (x, y) in nodo_a_coord.items():

    if nodo in nodos_T1:
        color = "red"
    elif nodo in nodos_T0:
        color = "blue"
    else:
        color = "black"

    plt.plot(x, y, "o", color=color)
    plt.text(x + 0.06, y + 0.06, str(nodo), fontsize=10)

plt.title("Geometría en L y numeración de nodos")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.axis("equal")
plt.xlim(-0.3, 6.3)
plt.ylim(-0.3, 4.3)
plt.show()

# ---------------------------------------------------------
# 9. Patrón de la matriz A
# ---------------------------------------------------------
plt.figure(figsize=(6, 6))
plt.spy(A, markersize=5)
plt.title("Estructura de la matriz global A")
plt.xlabel("Columna")
plt.ylabel("Fila")
plt.show()

# ---------------------------------------------------------
# 10. Superficie 3D de temperatura
# ---------------------------------------------------------
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

superficie = ax.plot_surface(
    X,
    Y,
    Z_mascara,
    cmap="hot",
    edgecolor="black",
    linewidth=0.5
)

ax.set_title("Distribución de temperatura en la geometría en L")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Temperatura")

fig.colorbar(superficie, ax=ax, label="Temperatura")
plt.show()

# ---------------------------------------------------------
# 11. Contornos de temperatura
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))

niveles = np.linspace(0.0, 1.0, 21)

relleno = plt.contourf(
    X,
    Y,
    Z_mascara,
    levels=niveles,
    cmap="hot",
    corner_mask=False
)

lineas = plt.contour(
    X,
    Y,
    Z_mascara,
    levels=niveles,
    colors="black",
    linewidths=0.6,
    corner_mask=False
)

plt.clabel(lineas, inline=True, fontsize=8)
plt.colorbar(relleno, label="Temperatura")

plt.title("Contornos de temperatura en la geometría en L")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.xlim(0, 6)
plt.ylim(0, 4)
plt.grid()
plt.show()