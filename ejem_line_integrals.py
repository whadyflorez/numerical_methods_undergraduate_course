import numpy as np

# Datos del problema
x = np.array([1, 1.0])         # Punto fijo x = (x1, x2)
p = np.array([0.0, 0.0])         # Punto extremo p = (p1, p2)
q = np.array([2.0, 0.0])         # Punto extremo q = (q1, q2)

# Longitud del segmento (norma del vector q - p)
length = np.linalg.norm(q - p)
jacobian = 0.5 * length          # Derivada de z respecto a xi

# Cuadratura de Gauss-Legendre (n puntos)
n_gauss = 6
xi, w = np.polynomial.legendre.leggauss(n_gauss)  # puntos y pesos en [-1, 1]

# Evaluar la integral
integral = 0.0
for i in range(n_gauss):
    N1 = 0.5 * (1 - xi[i])
    N2 = 0.5 * (1 + xi[i])
    z = N1 * p + N2 * q
    r = np.linalg.norm(z - x)
    integral += r * jacobian * w[i]

print(f"Valor de la integral: {integral:.6f}")
