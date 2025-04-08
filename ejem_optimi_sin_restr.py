import numpy as np
from scipy.optimize import minimize

# Función a minimizar (ejemplo tipo Rosenbrock)
def f(x):
    return 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2

x0 = np.array([0, 0])  # punto inicial

res = minimize(f, x0, method='BFGS')  # BFGS es un método no lineal sin restricciones
print("Resultado sin restricciones:")
print(res)
