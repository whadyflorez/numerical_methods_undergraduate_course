import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
c = 1.0
x_min, x_max = -1, 1
t_max = 0.1
dx = 0.01
dt = 0.001
r = c * dt / dx**2

# Mallas
x = np.arange(x_min, x_max + dx, dx)
nx = len(x)
nt = int(t_max / dt)

# Condición inicial
u = np.ones(nx) 
u[0] = 0     # frontera izquierda
u[-1] = 0    # frontera derecha

# Matriz A para el método implícito
A = np.zeros((nx, nx))

# Llenar matriz A (incluye las condiciones de frontera como filas del sistema)
for i in range(1, nx - 1):
    A[i, i - 1] = -r
    A[i, i]     = 1 + 2*r
    A[i, i + 1] = -r

# Condiciones de frontera como ecuaciones explícitas en A
A[0, 0] = 1
A[-1, -1] = 1

# Guardar historia para graficar
u_history = [u.copy()]
time_steps = [0]

# Solución implícita paso a paso
for n in range(1, nt + 1):
    b = u.copy()
    b[0] = 0    # frontera izquierda
    b[-1] = 0   # frontera derecha

    # Resolver el sistema A u_new = b
    u = np.linalg.solve(A, b)

    u_history.append(u.copy())
    time_steps.append(n * dt)

# --- GRAFICA u vs x ---
plt.figure(figsize=(10,6))
for i, u_plot in enumerate(u_history):
    if i%20==0:
        plt.plot(x, u_plot, label=f't = {time_steps[i]:.3f}')
plt.title("Distribución de u vs x (método implícito)")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.legend()
plt.grid(True)
plt.show()

# --- GRAFICA u vs t en x = 0 ---
x0_index = nx // 2
u_vs_t = [u_hist[x0_index] for u_hist in u_history]

plt.figure(figsize=(8,5))
plt.plot(time_steps, u_vs_t, marker='o')
plt.title("Evolución temporal de u en x = 0 (implícito)")
plt.xlabel("Tiempo t")
plt.ylabel("u(x=0,t)")
plt.grid(True)
plt.show()
