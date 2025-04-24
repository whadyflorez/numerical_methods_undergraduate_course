import numpy as np
import matplotlib.pyplot as plt

# Función a integrar
f = lambda x: np.sin(x)
a, b = 0, np.pi
n = 4  # Debe ser par
if n % 2 != 0:
    raise ValueError("n debe ser par para aplicar la regla de Simpson.")

x = np.linspace(a, b, n+1)
y = f(x)
dx = (b - a) / n

# Aproximación por Simpson
area = dx / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))
print(f"Aproximación por Simpson: {area:.8f}")

# Gráfico
x_fine = np.linspace(a, b, 1000)
plt.plot(x_fine, f(x_fine), '--k', label='f(x) = sin(x)')
for i in range(0, n, 2):
    xi = x[i:i+3]
    yi = y[i:i+3]
    coeffs = np.polyfit(xi, yi, 2)
    px = np.linspace(xi[0], xi[-1], 100)
    py = np.polyval(coeffs, px)
    plt.fill_between(px, py, alpha=0.4, edgecolor='k', color='orange')
plt.title("Regla de Simpson")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
