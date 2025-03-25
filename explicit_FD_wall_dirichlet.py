import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
c = 1.0          # coeficiente de difusión
x_min, x_max = -1, 1
t_max = 0.1
dx = 0.01
r = 0.3         # r=c*dt/dx**2 número de Fourier (debe ser <= 0.5 para estabilidad)
dt = r * dx**2 / c

# Mallas de espacio y tiempo
x = np.arange(x_min, x_max + dx, dx)
nx = len(x)
nt = int(t_max / dt)

# Condición inicial
u = np.ones(nx) 
u[0] = 0     # condición de frontera en x = -1
u[-1] = 0    # condición de frontera en x = 1

# Para guardar resultados en ciertos tiempos
u_history = [u.copy()]
time_steps = [0]

# Avance temporal (esquema explícito FTCS)
for n in range(1, nt+1):
    u_new = u.copy()
    for i in range(1, nx - 1):
        u_new[i] = u[i] + r * (u[i+1] - 2*u[i] + u[i-1])
    
    u = u_new
    u_history.append(u.copy())
    time_steps.append(n * dt)

# --- GRAFICA u vs x en diferentes tiempos ---
plt.figure(figsize=(10,6))
for i, u_plot in enumerate(u_history):
    if i%200==0:
      plt.plot(x, u_plot, label=f't = {time_steps[i]:.3f}')
plt.title("Distribución de u vs x en diferentes tiempos")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.legend()
plt.grid(True)
plt.show()

# --- GRAFICA u vs t en un punto específico x0 ---
x0_index = nx // 2  # punto central (x = 0)
u_vs_t = [u_hist[x0_index] for u_hist in u_history]

plt.figure(figsize=(8,5))
plt.plot(time_steps, u_vs_t)
plt.title("Evolución temporal de u en x = 0")
plt.xlabel("Tiempo t")
plt.ylabel("u(x=0,t)")
plt.grid(True)
plt.show()
