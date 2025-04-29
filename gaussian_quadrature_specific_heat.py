import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

# Definir la función C_v(T)
def C_v(T):
    a = 25          # J/mol.K
    b = 0.01        # J/mol.K^2
    c = -0.00002    # J/mol.K^3
    return a + b*T + c*T**2

# Función para la integral exacta de C_v(T)
def integral_exacta_Cv(T):
    a = 25          # J/mol.K
    b = 0.01        # J/mol.K^2
    c = -0.00002    # J/mol.K^3
    return a*T + (b/2)*T**2 + (c/3)*T**3

# Número de puntos de Gauss
n_points = 5

# Intervalo de integración [T1, T2]
T1 = 300  # Kelvin
T2 = 1000 # Kelvin

# Cuadratura Gaussiana
xi, wi = leggauss(n_points)
T_nodes = 0.5 * (T2 - T1) * xi + 0.5 * (T2 + T1)
weights = 0.5 * (T2 - T1) * wi
delta_U_gauss = np.sum(weights * C_v(T_nodes))

# Integral exacta
delta_U_exacta = integral_exacta_Cv(T2) - integral_exacta_Cv(T1)

# Error relativo
error_relativo = abs(delta_U_gauss - delta_U_exacta) / abs(delta_U_exacta) * 100

# Mostrar resultados
print(f"Integral Gaussiana ΔU ≈ {delta_U_gauss:.4f} J/mol")
print(f"Integral Exacta   ΔU = {delta_U_exacta:.4f} J/mol")
print(f"Error relativo = {error_relativo:.6f}%")

# Graficar C_v(T) y los nodos
T_plot = np.linspace(T1, T2, 400)
Cv_plot = C_v(T_plot)

plt.figure(figsize=(8,5))
plt.plot(T_plot, Cv_plot, label=r"$C_v(T)$", color='blue')
plt.scatter(T_nodes, C_v(T_nodes), color='red', label='Puntos de Gauss', zorder=5)
plt.title(r"$C_v(T)$ y nodos de Gauss para calcular $\Delta U$")
plt.xlabel("Temperatura (K)")
plt.ylabel(r"$C_v$ (J/mol·K)")
plt.legend()
plt.grid(True)
plt.show()
