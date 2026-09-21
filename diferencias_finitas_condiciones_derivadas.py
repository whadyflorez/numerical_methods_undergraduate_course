##ejemplo diferencias finitas en 2D basico
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

L=1.0
dx=L/4
dy=L/4
n=25

A=np.zeros((n,n))
B=np.zeros(n)

l_internos=[6,7,8,11,12,13,16,17,18]
l_base=[0,1,2,3,4]
l_izquierda=[5,10,15]
l_arriba=[20,21,22,23,24]
l_derecha=[9,14,19]

for i in l_internos:
    A[i,i+1]=1.0/dx**2
    A[i,i-1]=1.0/dx**2
    A[i,i+5]=1.0/dy**2
    A[i,i-5]=1.0/dy**2
    A[i,i]=-2.0/dx**2-2.0/dy**2
    B[i]=0.0
for i in l_base:
    A[i,i]=1.0
    B[i]=0.0
for i in l_derecha:
    A[i,i]=1.0/dx
    A[i,i-1]=-1.0/dx
    B[i]=-100.0
for i in l_izquierda:
    A[i,i]=1.0
    B[i]=0.0
for i in l_arriba:
    A[i,i]=1.0/dy
    A[i,i-5]=-1.0/dy
    B[i]=-100.0

T=np.linalg.solve(A,B)    

 

# Matriz de temperaturas:
# cada fila corresponde a un nivel de y:
# y = 0, 0.25, 0.50, 0.75, 1.00
Resultados = np.zeros((5, 5))

Resultados[0, :] = T[0:5]     # y = 0.00
Resultados[1, :] = T[5:10]    # y = 0.25
Resultados[2, :] = T[10:15]   # y = 0.50
Resultados[3, :] = T[15:20]   # y = 0.75
Resultados[4, :] = T[20:25]   # y = 1.00

# Nodos de la discretización
x_nodos = np.array([0.00, 0.25, 0.50, 0.75, 1.00])
y_nodos = np.array([0.00, 0.25, 0.50, 0.75, 1.00])

# Matrices X e Y construidas manualmente.
# Cada fila de X contiene las coordenadas x de una fila de nodos.
X = np.array([
    [0.00, 0.25, 0.50, 0.75, 1.00],
    [0.00, 0.25, 0.50, 0.75, 1.00],
    [0.00, 0.25, 0.50, 0.75, 1.00],
    [0.00, 0.25, 0.50, 0.75, 1.00],
    [0.00, 0.25, 0.50, 0.75, 1.00]
])

# Cada fila de Y identifica la altura y de esos nodos.
Y = np.array([
    [0.00, 0.00, 0.00, 0.00, 0.00],
    [0.25, 0.25, 0.25, 0.25, 0.25],
    [0.50, 0.50, 0.50, 0.50, 0.50],
    [0.75, 0.75, 0.75, 0.75, 0.75],
    [1.00, 1.00, 1.00, 1.00, 1.00]
])

print("Matriz X:")
print(X)

print("\nMatriz Y:")
print(Y)

print("\nMatriz de temperaturas:")
print(Resultados)

# Estructura de la matriz del sistema
plt.figure()
plt.spy(A)
plt.title("Estructura de la matriz A")
plt.show()

# Superficie de temperatura
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

superficie = ax.plot_surface(
    X, Y, Resultados,
    cmap="hot",
    edgecolor="black",
    linewidth=0.5
)

plt.contour(
    X,
    Y,
    Resultados,
    levels=20,
    colors="black",
    linewidths=0.4)

ax.set_title("Distribución de temperatura")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Temperatura")

fig.colorbar(superficie, ax=ax, label="Temperatura")
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    