import numpy as np
from math import exp
from scipy.optimize import fsolve

# --- Parámetros del problema ---
mu   = 0.30      # coef. fricción correa-polea
beta = 2.5       # ángulo de arrollamiento [rad]
R    = 0.10      # radio de la polea [m]
M    = 50.0      # torque a transmitir [N·m]

E = exp(mu * beta)  # relación teórica T1/T2

def residuals(x):
    """ x = [T1, T2] """
    T1, T2 = x
    f1 = T1 / T2 - E              # T1/T2 = e^(mu*beta)
    f2 = (T1 - T2) * R - M        # (T1 - T2)*R = M
    return np.array([f1, f2])

# --- Adivinanzas iniciales (físicas): T1 > T2 > 0 ---
                 
T2_guess = 200.0            # elige un valor positivo razonable
T1_guess = T2_guess + 50
x0 = np.array([T1_guess, T2_guess], dtype=float)

# --- Resolver con fsolve ---
sol, info, ier, msg = fsolve(residuals, x0, full_output=True)

T1, T2 = sol
print("Convergencia (ier=1 es OK):", ier)
print("Mensaje:", msg)
print(f"T1 = {T1:.6e} N")
print(f"T2 = {T2:.6f} N")
print(f"T1/T2 = {T1/T2:.6f} (esperado e^(mu*beta) = {E:.6f})")
print(f"(T1 - T2)*R = {(T1 - T2)*R:.6f} N·m (esperado M = {M:.6f} N·m)")

