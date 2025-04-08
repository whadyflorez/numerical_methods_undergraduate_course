from scipy.optimize import linprog
import numpy as np

# Costos de transporte: 5 sources x 2 sinks
# c = [c_11, c_12, c_21, c_22, ..., c_52]
c = [4, 6,   # Source 1 to Sink 1 and 2
     5, 3,   # Source 2
     9, 7,   # Source 3
     6, 4,   # Source 4
     8, 5]   # Source 5

# Capacidades de supply en cada fuente
supply = [20, 30, 10, 15, 25]

# Demandas en cada sink
demand = [60, 40]

# Matriz A_ub y b_ub: restricciones de oferta (≤)
A_ub = np.zeros((5, 10))
for i in range(5):
    A_ub[i, 2*i] = 1  # a sink 1
    A_ub[i, 2*i + 1] = 1  # a sink 2
b_ub = supply

# Matriz A_eq y b_eq: restricciones de demanda (==)
A_eq = np.zeros((2, 10))
for j in range(2):
    for i in range(5):
        A_eq[j, 2*i + j] = 1
b_eq = demand

# Bounds: todas las variables ≥ 0
bounds = [(0, None)] * 10

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
print("\nResultado de supply chain:")
print("Costo mínimo:", res.fun)
print("Distribución óptima (x_ij):")
print(res.x.reshape((5, 2)))  # reshaped para ver por fuente-sink
