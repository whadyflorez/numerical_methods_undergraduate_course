import numpy as np
import matplotlib.pyplot as plt

# Función a integrar
f = lambda x: np.sin(x)
a, b = 0, np.pi  # Límites de integración
n = 100           # Número de subintervalos
x = np.linspace(a, b, n+1)
y = f(x)
dx = (b - a) / n

# Aproximación por regla del trapecio
area = dx * (np.sum(y) - 0.5*y[0] - 0.5*y[-1])
print(f"Aproximación por trapecio: {area:.8f}")

# Gráfico
x_fine = np.linspace(a, b, 200)
plt.plot(x_fine, f(x_fine), 'k', label='f(x) = sin(x)')
for i in range(n):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, y[i], y[i+1], 0]
    plt.fill(xs, ys, 'skyblue', edgecolor='k', alpha=0.5)
plt.title("Regla del Trapecio")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
