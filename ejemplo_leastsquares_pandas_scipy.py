import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

# Leer datos desde un archivo CSV (asumiendo que tiene columnas 'x' y 'y')
df = pd.read_csv("data.csv")
x_data = df['x'].values
y_data = df['y'].values

# Definir la función modelo (por ejemplo, una parábola: y = a*x^2 + b*x + c)
def modelo(x, a, b, c):
 #   z=a*x**2 + b*x + c
    z=a*np.exp(-b*x)+c
    return z

# Ajustar la curva usando scipy.optimize.curve_fit
parametros_optimos, _ = curve_fit(modelo, x_data, y_data)

# Generar valores ajustados para graficar
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = modelo(x_fit, *parametros_optimos)

# Graficar los datos y la curva ajustada
plt.scatter(x_data, y_data, label="Datos experimentales", color="red")
plt.plot(x_fit, y_fit, label="Ajuste por mínimos cuadrados", color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Ajuste de mínimos cuadrados con SciPy")
plt.show()
