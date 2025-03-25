import numpy as np
import matplotlib.pyplot as plt

# Parámetros
c = 1.0
h = 5.0
x_min, x_max = -1, 1
dx = 0.01
r = 0.4
dt = r * dx**2 / c
t_max = 0.1

# Mallas
x = np.arange(x_min, x_max + dx, dx)
nx = len(x)
nt = int(t_max / dt)

# Condición inicial
u = np.ones(nx) * 2
u_history = [u.copy()]
time_steps = [0]

# Avance temporal
for n in range(1, nt + 1):
    u_new = u.copy()

    # Interior
    for i in range(1, nx - 1):
        u_new[i] = u[i] + r * (u[i+1] - 2*u[i] + u[i-1])
    
    # Frontera izquierda (x = -1), usando forward difference
#    dudx_left = (u[1] - u[0]) / dx
    u_new[0] = (u[1] + dx * h * 10) / (1 + dx * h)

    # Frontera derecha (x = 1), usando backward difference
#    dudx_right = (u[-1] - u[-2]) / dx
    u_new[-1] = (u[-2] + dx * h * 10) / (1 + dx * h)

    u = u_new
    if n % (nt // 5) == 0 or n == nt:
        u_history.append(u.copy())
        time_steps.append(n * dt)

# --- GRAFICA u vs x ---
plt.figure(figsize=(10,6))
for i, u_plot in enumerate(u_history):
    plt.plot(x, u_plot, label=f't = {time_steps[i]:.3f}')
plt.title("u vs x (Explícito con Robin)")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.legend()
plt.grid(True)
plt.show()
