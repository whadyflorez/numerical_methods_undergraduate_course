import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# -------------------------------
# SISTEMA 1
# -------------------------------
def sistema1(vars):
    x, y = vars
    return [y-x*np.cos(x) ,
            x**2 + y**2 - 5]

sol1 = fsolve(sistema1, [-2, 0])  # Valor inicial adecuado

# -------------------------------
# SISTEMA 2
# -------------------------------
def sistema2(vars):
    x, y = vars
    return [np.log(x**2 + y**2) - 1,
            x * y - 1]

sol2 = fsolve(sistema2, [1, 1])  # Valor inicial adecuado

# -------------------------------
# GRAFICACIÓN
# -------------------------------
x = np.linspace(-4, 4, 600)
y = np.linspace(-4, 4, 600)
X, Y = np.meshgrid(x, y)

# Sistema 1
Z1_1 = Y-X*np.cos(X)  
Z1_2 = X**2 + Y**2 - 5

# Sistema 2
Z2_1 = np.log(X**2 + Y**2) - 1
Z2_2 = X * Y - 1

# Crear figura
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# --------- Sistema 1 -------------
axs[0].contour(X, Y, Z1_1, levels=[0], colors='blue', linestyles='--', linewidths=2)
axs[0].contour(X, Y, Z1_2, levels=[0], colors='red', linewidths=2)
axs[0].plot(sol1[0], sol1[1], 'ko', label='Solución numérica')
axs[0].set_title('Sistema 1: x cos(y) = 4 y x² + y² = 5')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].legend()
axs[0].grid(True)

# --------- Sistema 2 -------------
axs[1].contour(X, Y, Z2_1, levels=[0], colors='green', linestyles='--', linewidths=2)
axs[1].contour(X, Y, Z2_2, levels=[0], colors='purple', linewidths=2)
axs[1].plot(sol2[0], sol2[1], 'ko', label='Solución numérica')
axs[1].set_title('Sistema 2: ln(x² + y²) = 1 y x y = 1')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()

# Mostrar soluciones por consola
print(f"Solución sistema 1: x = {sol1[0]:.4f}, y = {sol1[1]:.4f}")
print(f"Solución sistema 2: x = {sol2[0]:.4f}, y = {sol2[1]:.4f}")


sol3 = fsolve(sistema2, [1, 1],full_output=True) 


print(sistema1(sol1))