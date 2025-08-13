# Intercambiador tubos–coraza: resolver v_w (agua en tubos) y v_o (aceite en coraza)
# con dos ecuaciones no lineales:
#   1) U(v_w,v_o) * A(v_w) * ΔT_lm = Q
#   2) ΔP_tubo(v_w) + ΔP_coraza(v_o) = ΔP_max

import numpy as np
from math import pi
from scipy.optimize import fsolve

# ---------------- Datos del problema ----------------
Q = 150e3          # W
DeltaT_lm = 25.0   # K
DeltaP_max = 100e3 # Pa

# Geometría
D_t = 0.025        # m (diámetro interno tubo)
L_t = 4.0          # m (longitud tubo)
D_h = 0.04         # m (diámetro hidráulico coraza)
L_s = 3.0          # m (long. característica coraza)

# Propiedades (a T media)
rho_w, mu_w, k_w, Pr_w = 995.0, 0.0008, 0.60, 5.5
rho_o, mu_o, k_o, Pr_o = 850.0, 0.03,   0.13, 200.0

# Caudal másico agua para dimensionar número de tubos
m_dot_w = 1.5      # kg/s

# --------------- Correlaciones básicas ---------------
def h_water(vw):
    Re = max(rho_w * vw * D_t / mu_w, 1.0)
    Nu = 0.023 * (Re**0.8) * (Pr_w**0.3)
    return (k_w / D_t) * Nu, Re

def h_oil(vo):
    Re = max(rho_o * vo * D_h / mu_o, 1.0)
    Nu = 0.36 * (Re**0.55) * (Pr_o**(1/3))
    return (k_o / D_h) * Nu, Re

def U_overall(vw, vo):
    hw, _ = h_water(vw); ho, _ = h_oil(vo)
    return 1.0 / (1.0/hw + 1.0/ho)

def area_from_vw(vw):
    vw = max(vw, 1e-9)
    Vdot = m_dot_w / rho_w                 # m^3/s
    A_sec = pi * (D_t**2) / 4.0            # m^2 (sección de UN tubo)
    N_tubes = Vdot / (vw * A_sec)          # cantidad de tubos en paralelo
    A_total = N_tubes * (pi * D_t * L_t)   # m^2 (área externa aprox)
    return A_total

def f_fric(Re):   # Blasius
    return 0.079 * (Re**-0.25)

def dP_tube(vw):
    _, Re = h_water(vw)
    return f_fric(Re) * (L_t / D_t) * (rho_w * vw**2 / 2.0)

def dP_shell(vo):
    _, Re = h_oil(vo)
    return f_fric(Re) * (L_s / D_h) * (rho_o * vo**2 / 2.0)

# --------------- Residuales para fsolve ---------------
def residuals(x):
    vw, vo = x
    vw = max(vw, 1e-9); vo = max(vo, 1e-9)
    U  = U_overall(vw, vo)
    A  = area_from_vw(vw)
    f1 = U * A * DeltaT_lm - Q
    f2 = dP_tube(vw) + dP_shell(vo) - DeltaP_max
    return np.array([f1, f2], dtype=float)

# --------------- Resolver y reportar -------------------
# Adivinanzas iniciales razonables
x0 = np.array([0.005, 0.008])  # [vw (m/s), vo (m/s)]

sol, info, ier, msg = fsolve(residuals, x0, full_output=True)

vw, vo = sol
U  = U_overall(vw, vo)
A  = area_from_vw(vw)
r1, r2 = residuals(sol)

print("Convergencia (ier=1 OK):", ier)
print("Mensaje:", msg)
print("\n--- RESULTADOS ---")
print(f"v_w (agua en tubos)  = {vw:.6f} m/s")
print(f"v_o (aceite coraza)  = {vo:.6f} m/s")
print(f"U (global)           = {U:.2f} W/m^2-K")
print(f"A_total              = {A:.3f} m^2")
print(f"Check energía  f1    = {r1:.3e}  (→0)")
print(f"Check hidráulica f2  = {r2:.3e}  (→0)")
