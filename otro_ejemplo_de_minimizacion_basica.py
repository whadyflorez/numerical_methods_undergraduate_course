"""problema de dos variables en Calculus Volume 3 de OpenStax, 
Ejemplo 4.3 (“Nuts and Bolts”). Una empresa vende tuercas 
\(x\) y pernos \(y\), ambos medidos en miles de unidades al mes; 
la utilidad, en miles de dólares, es:
\[P(x,y)=16-(x-3)^2-(y-2)^2\]"""

import numpy as np
from scipy.optimize import minimize


# SciPy minimiza; por eso usamos el negativo de la utilidad
def objetivo(x):
    f=x[0]**3+x[1]**2+x[2]**2-3*x[0]-4*x[1]-6*x[2]
    return f

# Gradiente de -P(x, y)
def gradiente(x):
    grad=np.array([3*x[0]**2-3,2*x[1]-4,2*x[2]-6])
    return grad

resultado = minimize(
    objetivo,
    x0=[0.1, -1,2],          # estimación inicial: [x, y]
    jac=gradiente,
    method="BFGS"
)

x_opt, y_opt,z_opt = resultado.x
utilidad_max = -resultado.fun

print("Convergió:", resultado.success)
print(f"Tuercas: {x_opt:.4f} miles/mes")
print(f"Pernos: {y_opt:.4f} miles/mes")
print(f"Utilidad máxima: ${utilidad_max:.4f} miles/mes")