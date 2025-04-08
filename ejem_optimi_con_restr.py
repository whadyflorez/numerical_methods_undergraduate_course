import numpy as np
from scipy.optimize import minimize

# Función objetivo
def obj(x):
    return (x[0] - 1)**2 + (x[1] - 2)**2

# Restricciones de igualdad
def eq1(x):
    return x[0] + x[1] - 3

def eq2(x):
    return x[0] - x[1]

# Restricciones de desigualdad (deben ser >= 0)
def ineq1(x):
    return x[0] - 0.5       # x >= 0.5

def ineq2(x):
    return 3 - x[1]         # y <= 3  → 3 - y ≥ 0

# Agrupamos restricciones
constraints = [
    {'type': 'eq', 'fun': eq1},
    {'type': 'eq', 'fun': eq2},
    {'type': 'ineq', 'fun': ineq1},
    {'type': 'ineq', 'fun': ineq2}
]

# Opcionalmente, también definimos bounds (pero ya están en ineq)
bounds = [(0, 5), (0, 5)]  # x, y entre 0 y 5

# Punto inicial
x0 = [2, 1]

# Solución
res = minimize(obj, x0, method='SLSQP', constraints=constraints, bounds=bounds)

# Resultado
print("Resultado:")
print("x =", res.x[0])
print("y =", res.x[1])
print("Valor mínimo =", res.fun)
print("¿Éxito?", res.success)
print("Mensaje:", res.message)
