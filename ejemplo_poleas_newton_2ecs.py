import numpy as np

# ---- Parámetros del problema (ajústalos si quieres) ----
mu = 0.30        # coeficiente de fricción correa-polea
beta = 2.5       # ángulo de arrollamiento [rad]
R = 0.10         # radio polea [m]
M = 50.0         # torque a transmitir [N·m]

E = np.exp(mu * beta)  # relación de tensiones T1/T2 en estática por fricción

def residuals(x):
    """ x = [T1, T2] """
    T1, T2 = x
    f1 = T1 / T2 - E
    f2 = (T1 - T2) * R - M
    return np.array([f1, f2], dtype=float)

def jacobian(x):
    """ Jacobiano analítico de f """
    T1, T2 = x
    J = np.array([[1.0 / T2, -T1 / (T2**2)],
                  [R,         -R            ]], dtype=float)
    return J

def newton(x0, tol=1e-12, maxit=50, verbose=True):
    x = np.array(x0, dtype=float)
    for k in range(maxit):
        f = residuals(x)
        nrm = np.linalg.norm(f)
        if verbose:
            print(f"[It {k:2d}] x={x}, ||f||={nrm:.3e}")
        if nrm < tol:
            return x, True
        J = jacobian(x)
        step = np.linalg.solve(J, -f)
        # Búsqueda de línea simple para mantener T1,T2>0 y mejorar ||f||
        alpha = 1.0
        for _ in range(20):
            x_trial = x + alpha * step
            if np.linalg.norm(residuals(x_trial)) < nrm:
                x = x_trial
                break
            alpha *= 0.5
        else:
            # Si no mejora, acepta paso mínimo pero imponiendo positividad
            x = np.maximum(x + alpha * step, 1e-12)
    return x, False

# ---- Adivinanzas iniciales físicas: T1 > T2 > 0 ----
# Puedes estimarlas desde la segunda ecuación: (T1 - T2) = M/R.
# Por ejemplo, reparte esa diferencia alrededor de un promedio razonable:
dT = M / R        # diferencia necesaria entre tensiones
T2_guess = 200.0  # elige un valor positivo razonable
T1_guess = T2_guess + dT

sol, ok = newton([T1_guess, T2_guess], tol=1e-12, maxit=30, verbose=True)

print("\nConverged:", ok)
T1, T2 = sol
print(f"T1 = {T1:.6f} N")
print(f"T2 = {T2:.6f} N")
print(f"T1/T2 = {T1/T2:.6f} (esperado: e^(mu*beta) = {E:.6f})")
print(f"(T1 - T2)*R = {(T1 - T2)*R:.6f} N·m (esperado: M = {M:.6f} N·m)")
