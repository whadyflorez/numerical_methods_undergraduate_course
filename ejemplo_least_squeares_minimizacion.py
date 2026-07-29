import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# ---------------------------------------------------------
# 1. Datos ficticios
# ---------------------------------------------------------
np.random.seed(12)

x = np.linspace(-4, 5, 16)
a_real, b_real, c_real = 1.2, -2.0, 4.0
ruido = np.random.normal(0, 2.5, len(x))

y = a_real * x**2 + b_real * x + c_real + ruido


# ---------------------------------------------------------
# 2. Modelo cuadrático: y = a*x² + b*x + c
# ---------------------------------------------------------
def modelo(parametros, x):
    a, b, c = parametros
    return a * x**2 + b * x + c


# Función objetivo: suma de cuadrados de los residuos
def suma_cuadrados(parametros, x, y):
    residuos = y - modelo(parametros, x)
    return np.sum(residuos**2)


# Gradiente de la función objetivo
def gradiente_suma_cuadrados(parametros, x, y):
    residuos = y - modelo(parametros, x)

    d_da = -2 * np.sum(residuos * x**2)
    d_db = -2 * np.sum(residuos * x)
    d_dc = -2 * np.sum(residuos)

    return np.array([d_da, d_db, d_dc])


# ---------------------------------------------------------
# 3. Minimización con BFGS (cuasi-Newton)
# ---------------------------------------------------------
parametros_iniciales = [0, 0, 0]

resultado = minimize(
    suma_cuadrados,
    parametros_iniciales,
    args=(x, y),
    jac=gradiente_suma_cuadrados,
    method="BFGS"
)

a, b, c = resultado.x
y_ajustado = modelo(resultado.x, x)

print("¿La minimización fue exitosa?:", resultado.success)
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print(f"c = {c:.4f}")
print(f"Modelo ajustado: y = {a:.4f}x² + ({b:.4f})x + ({c:.4f})")
print(f"Suma de errores al cuadrado: {resultado.fun:.4f}")


# ---------------------------------------------------------
# 4. Gráfica: datos, modelo y residuos
# ---------------------------------------------------------
x_suave = np.linspace(x.min(), x.max(), 300)
y_suave = modelo(resultado.x, x_suave)

plt.figure(figsize=(10, 6))

# Barras verticales: residuos o errores
for xi, yi, y_predicho in zip(x, y, y_ajustado):
    plt.vlines(
        xi, y_predicho, yi,
        color="crimson",
        linestyle="--",
        linewidth=1.5
    )

# Datos y curva ajustada
plt.scatter(x, y, color="navy", s=60, label="Datos experimentales")
plt.plot(
    x_suave, y_suave,
    color="darkorange",
    linewidth=2.5,
    label="Modelo cuadrático ajustado"
)

plt.title("Ajuste cuadrático por mínimos cuadrados")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()