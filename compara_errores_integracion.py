import numpy as np
import matplotlib.pyplot as plt

# Función a integrar
f = lambda x: np.sin(x)
a, b = 0, np.pi
exact = 2  # Valor exacto de la integral

# Método del trapecio
def trapezoidal(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = (b - a) / n
    return dx * (np.sum(y) - 0.5*y[0] - 0.5*y[-1])

# Método de Simpson
def simpson(f, a, b, n):
    if n % 2 != 0:
        return np.nan  # Simpson solo se aplica para n par
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = (b - a) / n
    return dx / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))

# Comparación de errores
ns = np.arange(2, 50, 2)
errors_trap = [abs(trapezoidal(f, a, b, n) - exact) for n in ns]
errors_simp = [abs(simpson(f, a, b, n) - exact) for n in ns]

# Gráfico
plt.figure(figsize=(8,5))
plt.plot(ns, errors_trap, 'o-', label='Trapecio')
plt.plot(ns, errors_simp, 's-', label='Simpson')
plt.yscale('log')
plt.xlabel('Número de subintervalos n')
plt.ylabel('Error absoluto')
plt.title('Comparación de errores: Trapecio vs Simpson')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
