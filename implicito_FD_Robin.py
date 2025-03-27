import numpy as np
import matplotlib.pyplot as plt

# Parámetros
c = 1
h = 5.0
x_min, x_max = -1, 1
dx = 0.01
dt = 0.01
r = c * dt / dx**2
t_max = 1

# Mallas
x = np.arange(x_min, x_max + dx, dx)
nx = len(x)
nt = int(t_max / dt)

# Condición inicial
u = np.ones(nx)

u_history = [u.copy()]
time_steps = [0]

# Matriz A
A = np.zeros((nx, nx))

# Interior
for i in range(1, nx - 1):
    A[i, i - 1] = r
    A[i, i]     = -1 - 2*r
    A[i, i + 1] = r

# Frontera izquierda (Robin)
A[0,0]=-1-h*dx
A[0,1]=1

# A[0, 0] = -3 - 2*dx * h
# A[0, 1] = 4
# A[0, 2] = -1 

# Frontera derecha (Robin)
A[-1,-1]=1+h*dx
A[-1,-2]=-1
# A[-1, -1] = 3+2*dx*h
# A[-1, -2] = -4
# A[-1, -3] = 1

b=np.zeros(nx)
b[1:nx-1] = -u[1:nx-1]
    # Modificar términos independientes con valor 10 de Robin
b[0] = -dx * h * 10
b[nx-1]= dx * h * 10

# b[0] = -2*dx * h * 10
# b[-1]= 2*dx * h * 10

# Avance temporal
for n in range(1, nt + 1):

    # Resolver sistema lineal
    u = np.linalg.solve(A, b)
    u_history.append(u.copy())
    time_steps.append(n * dt)
    b[1:nx-1]=-u[1:nx-1]
    b[0] = -dx * h * 10
    b[-1]= dx * h * 10

    # b[0] = -2*dx * h * 10
    # b[-1]= 2*dx * h * 10

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
