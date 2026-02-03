import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------
# 1. Definimos la ecuación diferencial
# ----------------------------------------------------
def f(x, y):
    z=x-y
    return z   # ejemplo: dy/dx = x - y

# ----------------------------------------------------
# 2. Región rectangular
# ----------------------------------------------------
x_min, x_max = -3, 3
y_min, y_max = -3, 3


Nx, Ny = 20, 20   # densidad de la grilla

x_vals = np.linspace(x_min, x_max,Nx)
y_vals = np.linspace(y_min, y_max,Ny)

# ----------------------------------------------------
# 3. Tamaño del segmento
# ----------------------------------------------------
L = 0.25  # longitud visual de cada segmento

# ----------------------------------------------------
# 4. Gráfica
# ----------------------------------------------------
plt.figure(figsize=(6, 6))
#plt.figure()

for x in x_vals:
    for y in y_vals:
        m = f(x, y)

        # Vector director (1, m)
        dx = 1.0
        dy = m

        # Normalización
        norm = np.sqrt(dx**2 + dy**2)
        dx /= norm
        dy /= norm

        # Segmento centrado en (x, y)
        x_segment = [x , x + L*dx]
        y_segment = [y , y + L*dy]

#        plt.plot(x_segment, y_segment, color='black')
        plt.arrow(x, y,L*dx,L*dy, color='black',head_width=0.08,
                  head_length=0.12,
                  length_includes_head=True)

# ----------------------------------------------------
# 5. Estética
# ----------------------------------------------------
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Diagrama de pendientes: dy/dx = f(x,y)')
plt.grid(True)
plt.axis('equal')

plt.show()
