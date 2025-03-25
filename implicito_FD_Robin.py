import numpy as np
import matplotlib.pyplot as plt

# Parámetros
c = 1
h = 5.0
x_min, x_max = -1, 1
dx = 0.01
dt = 0.01
r = c * dt / dx**2
t_max = 0.1

# Mallas
x = np.arange(x_min, x_max + dx, dx)
nx = len(x)
nt = int(t_max / dt)

# Condición inicial
u = np.ones(nx) * 2
u_history = [u.copy()]
time_steps = [0]

# Matriz A
A = np.zeros((nx, nx))

# Interior
for i in range(1, nx - 1):
    A[i, i - 1] = -r
    A[i, i]     = 1 + 2*r
    A[i, i + 1] = -r

# Frontera izquierda (Robin)
A[0, 0] = 1 + dx * h
A[0, 1] = -1

# Frontera derecha (Robin)
A[-1, -2] = 1
A[-1, -1] = -(1 + dx * h)

# Avance temporal
for n in range(1, nt + 1):
    b = u.copy()

    # Modificar términos independientes con valor 10 de Robin
    b[0] += dx * h * 10
    b[-1] += -dx * h * 10

    # Resolver sistema lineal
    u = np.linalg.solve(A, b)

    u_history.append(u.copy())
    time_steps.append(n * dt)

# --- GRAFICA u vs x ---
plt.figure(figsize=(10,6))
for i, u_plot in enumerate(u_history):
    if i%5==0:
        plt.plot(x, u_plot, label=f't = {time_steps[i]:.3f}')
plt.title("u vs x (Implícito con Robin)")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.legend()
plt.grid(True)
plt.show()
