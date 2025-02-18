import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return x**2 + y**2

# Definir el rango de valores para x e y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Crear la malla de valores X, Y
X, Y = np.meshgrid(x, y)

# Evaluar la función punto a punto usando ciclos for con zip
Z = np.zeros_like(X)
# for i, (x_row, y_row) in enumerate(zip(X, Y)):
#     for j, (xi, yi) in enumerate(zip(x_row, y_row)):
#         Z[i, j] = f(xi, yi)
        
for i in range(X.shape[0]):  # Itera sobre las filas
    for j in range(X.shape[1]):  # Itera sobre las columnas
        Z[i, j] = f(X[i, j], Y[i, j])  # Evalúa la función y almacena el resultado        

# Crear la figura y el eje 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gráfica de f(x, y) = x^2 + y^2')

# Mostrar la gráfica
plt.show()
