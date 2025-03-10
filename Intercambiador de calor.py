import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, solve_ivp
import time

# Parámetros del intercambiador de calor
U = 600.0     # W/m²*k
A = 50.0      # m²
m_c = 1.199174  # kg/s => densidad*caudal volumétrico. Agua a 30°C
m_h = 1.7    # kg/s => densidad*caudal volumétrico. Aceite térmico (representativo)
C_p_h = 2.2 * 1000  # J/kg*K (convertido de kJ/kg*K a J/kg*K)
C_p_c = 4.18 * 1000  # J/kg*K (convertido de kJ/kg*K a J/kg*K)
T_h_in = 150.0   # °C
T_c_in = 30.0    # °C

# Función del intercambiador de calor
def heat_exchanger(T, x):
    T_h, T_c = T
    dT_h_dx = -(U * A / (m_h * C_p_h)) * (T_h - T_c)
    dT_c_dx = (U * A / (m_c * C_p_c)) * (T_h - T_c)
    return [dT_h_dx, dT_c_dx]

# Condiciones iniciales
T0 = [T_h_in, T_c_in]
x_lsoda = np.linspace(0, 1, 100)

# Solución con odeint-LSODA (método de referencia)
start_time = time.time()
solution = odeint(heat_exchanger, T0, x_lsoda)
lsoda_time = time.time() - start_time
T_h_lsoda = solution[:, 0]
T_c_lsoda = solution[:, 1]

# Función para RK45 y RK23
def heat_exchanger_rk(x, T):
    T_h, T_c = T
    dT_h_dx = -(U * A / (m_h * C_p_h)) * (T_h - T_c)
    dT_c_dx = (U * A / (m_c * C_p_c)) * (T_h - T_c)
    return [dT_h_dx, dT_c_dx]

# Solución con RK45
start_time = time.time()
sol = solve_ivp(heat_exchanger_rk, [x_lsoda[0], x_lsoda[-1]], T0, method='RK45', t_eval=x_lsoda)
rk45_time = time.time() - start_time
T_h_rk45 = sol.y[0]
T_c_rk45 = sol.y[1]

# Solución con RK23
start_time = time.time()
sol23 = solve_ivp(heat_exchanger_rk, [x_lsoda[0], x_lsoda[-1]], T0, method='RK23', t_eval=x_lsoda)
rk23_time = time.time() - start_time
T_h_rk23 = sol23.y[0]
T_c_rk23 = sol23.y[1]

# Solución con Euler
dx = 0.01  # Paso
x_euler = np.arange(0, 1 + dx, dx)
T_h_euler = np.zeros_like(x_euler)
T_c_euler = np.zeros_like(x_euler)
T_h_euler[0] = T_h_in
T_c_euler[0] = T_c_in

start_time = time.time()
for i in range(1, len(x_euler)):
    dT_h_dx = -(U * A / (m_h * C_p_h)) * (T_h_euler[i - 1] - T_c_euler[i - 1])
    dT_c_dx = (U * A / (m_c * C_p_c)) * (T_h_euler[i - 1] - T_c_euler[i - 1])
    T_h_euler[i] = T_h_euler[i - 1] + dT_h_dx * dx
    T_c_euler[i] = T_c_euler[i - 1] + dT_c_dx * dx
euler_time = time.time() - start_time

# Interpolate LSODA results to match Euler x values
T_h_lsoda_interp = np.interp(x_euler, x_lsoda, T_h_lsoda)
T_c_lsoda_interp = np.interp(x_euler, x_lsoda, T_c_lsoda)

# Interpolate RK45 and RK23 to Euler x values
T_h_rk45_interp = np.interp(x_euler, x_lsoda, T_h_rk45)
T_c_rk45_interp = np.interp(x_euler, x_lsoda, T_c_rk45)

T_h_rk23_interp = np.interp(x_euler, x_lsoda, T_h_rk23)
T_c_rk23_interp = np.interp(x_euler, x_lsoda, T_c_rk23)

# Calcular el error relativo total
error_rk45 = np.abs((T_h_rk45_interp - T_h_lsoda_interp) / T_h_lsoda_interp) + np.abs((T_c_rk45_interp - T_c_lsoda_interp) / T_c_lsoda_interp)
error_rk23 = np.abs((T_h_rk23_interp - T_h_lsoda_interp) / T_h_lsoda_interp) + np.abs((T_c_rk23_interp - T_c_lsoda_interp) / T_c_lsoda_interp)
error_euler = np.abs((T_h_euler - T_h_lsoda_interp) / T_h_lsoda_interp) + np.abs((T_c_euler - T_c_lsoda_interp) / T_c_lsoda_interp)


# Graficar el error relativo total
plt.figure(figsize=(10, 6))

plt.plot(x_euler, error_rk45, label='Error RK45', linewidth=2, linestyle='--', color='blue')
plt.plot(x_euler, error_rk23, label='Error RK23', linewidth=2, linestyle='-', color='red')
plt.plot(x_euler, error_euler, label='Error Euler', linewidth=2, linestyle=':', color='green')

plt.title('Error relativo total de los métodos numéricos respecto a LSODA')
plt.xlabel('Posición a lo largo del intercambiador de calor (m)')
plt.ylabel('Error relativo total')
plt.legend()
plt.grid(True)
plt.show()

# Graficar la comparación entre errores de RK45 y RK23
plt.figure(figsize=(10, 6))

plt.plot(x_euler, error_rk45, label='Error RK45', linewidth=2, linestyle='--', color='blue')
plt.plot(x_euler, error_rk23, label='Error RK23', linewidth=2, linestyle='-', color='red')

plt.title('Comparación del error relativo total entre RK45 y RK23')
plt.xlabel('Posición a lo largo del intercambiador de calor (m)')
plt.ylabel('Error relativo total')
plt.legend()
plt.grid(True)
plt.show()

# Gráficas individuales de cada método

# LSODA
plt.figure(figsize=(8, 5))
plt.plot(x_lsoda, T_h_lsoda, label='Fluido caliente (Aceite térmico)')
plt.plot(x_lsoda, T_c_lsoda, label='Fluido frío (Agua)')
plt.xlabel('Posición a lo largo del intercambiador de calor (m)')
plt.ylabel('Temperatura (°C)')
plt.title('Perfil de temperatura en el intercambiador de calor (odeint-LSODA)')
plt.legend()
plt.grid(True)
plt.show()

#RK45
plt.figure(figsize=(8, 5))
plt.plot(sol.t, sol.y[0], label='Fluido caliente (Aceite térmico)')
plt.plot(sol.t, sol.y[1], label='Fluido frío (Agua)')
plt.xlabel('Posición a lo largo del intercambiador de calor (m)')
plt.ylabel('Temperatura (°C)')
plt.title('Perfil de temperatura en el intercambiador de calor (RK45)')
plt.legend()
plt.grid(True)
plt.show()

#RK23
plt.figure(figsize=(8, 5))
plt.plot(sol23.t, sol23.y[0], label='Fluido caliente (Aceite térmico)')
plt.plot(sol23.t, sol23.y[1], label='Fluido frío (Agua)')
plt.xlabel('Posición a lo largo del intercambiador de calor (m)')
plt.ylabel('Temperatura (°C)')
plt.title('Perfil de temperatura en el intercambiador de calor (RK23)')
plt.legend()
plt.grid(True)
plt.show()

#EULER
plt.figure(figsize=(8, 5))
plt.plot(x_euler, T_h_euler, label='Fluido caliente (Aceite térmico)')
plt.plot(x_euler, T_c_euler, label='Fluido frío (Agua)')
plt.xlabel('Posición a lo largo del intercambiador de calor (m)')
plt.ylabel('Temperatura (°C)')
plt.title('Perfil de temperatura en el intercambiador de calor (Euler)')
plt.legend()
plt.grid(True)
plt.show()

#gráfico comparativo entre resultados

plt.figure(figsize=(8,5))
plt.plot(x_lsoda, T_h_lsoda, label='Fluido caliente (Aceite térmico) LSODA')
plt.plot(x_lsoda, T_c_lsoda, label='Fluido frío (Agua) LSODA')
plt.plot(sol.t, sol.y[0], label='Fluido caliente (Aceite térmico) RK45')
plt.plot(sol.t, sol.y[1], label='Fluido frío (Agua) RK45')
plt.plot(sol23.t, sol23.y[0], label='Fluido caliente (Aceite térmico) RK23')
plt.plot(sol23.t, sol23.y[1], label='Fluido frío (Agua) RK23')
plt.plot(x_euler, T_h_euler, label='Fluido caliente (Aceite térmico) Euler')
plt.plot(x_euler, T_c_euler, label='Fluido frío (Agua) Euler')
plt.xlabel('Posición a lo largo del intercambiador de calor (m)')
plt.ylabel('Temperatura (°C)')
plt.title('Comparación de resultados entre todos los métodos usados')
plt.legend(loc='best')
plt.grid(True)
plt.show()

# Comparación de tiempos computacionales
methods = ['LSODA', 'RK45', 'RK23', 'Euler']
times = [lsoda_time, rk45_time, rk23_time, euler_time]

plt.figure(figsize=(8, 5))
plt.bar(methods, times, color=['blue', 'green', 'orange', 'red'])
plt.xlabel('Método numérico')
plt.ylabel('Tiempo computacional (s)')
plt.title('Comparación de tiempos computacionales')
plt.grid(True)
plt.show()

# Imprimir tiempos computacionales
for method, time_ in zip(methods, times):
    print(f"Tiempo computacional de {method}: {time_:.6f} segundos")
