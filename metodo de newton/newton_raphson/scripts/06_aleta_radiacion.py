"""06 - Aleta cilindrica con conveccion y radiacion (transferencia de calor): sistema no lineal 3x3.
Nodos 1,2 interiores; nodo 3 en la punta (volumen de control de media celda). T0 fija en la base."""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, root
from _util import *

sigma = 5.670e-8
k, D, L = 50.0, 0.010, 0.15           # W/mK, m, m
h, eps_e = 15.0, 0.8                  # W/m2K, emisividad
Tinf = Tsur = 300.0                   # K
T0 = 600.0                            # K  (base)
n = 3; dx = L/n
P = np.pi*D; Ac = np.pi*D**2/4
kA_dx = k*Ac/dx

def F(T):
    T1, T2, T3 = T
    r1 = kA_dx*(T0 - 2*T1 + T2) - h*P*dx*(T1 - Tinf) - eps_e*sigma*P*dx*(T1**4 - Tsur**4)
    r2 = kA_dx*(T1 - 2*T2 + T3) - h*P*dx*(T2 - Tinf) - eps_e*sigma*P*dx*(T2**4 - Tsur**4)
    r3 = kA_dx*(T2 - T3) - (h*(P*dx/2 + Ac))*(T3 - Tinf) - eps_e*sigma*(P*dx/2 + Ac)*(T3**4 - Tsur**4)
    return np.array([r1, r2, r3])

def J(T):
    T1, T2, T3 = T
    d1 = -2*kA_dx - h*P*dx - 4*eps_e*sigma*P*dx*T1**3
    d2 = -2*kA_dx - h*P*dx - 4*eps_e*sigma*P*dx*T2**3
    d3 = -kA_dx - h*(P*dx/2 + Ac) - 4*eps_e*sigma*(P*dx/2 + Ac)*T3**3
    return np.array([[d1, kA_dx, 0.0],
                     [kA_dx, d2, kA_dx],
                     [0.0, kA_dx, d3]])

def J_fd(T, h_=1.0):
    """Jacobiana por diferencias finitas hacia adelante."""
    T = np.asarray(T, float); f0 = F(T); Jn = np.zeros((3, 3))
    for j in range(3):
        Tp = T.copy(); Tp[j] += h_
        Jn[:, j] = (F(Tp) - f0)/h_
    return Jn

Tg = np.full(3, T0)
sol, hist = newton_nd(F, J, Tg, tol=1e-13)
print("Newton (J analitica): T =", sol, " it =", len(hist)-1)
print("k, T1, T2, T3, ||F||")
for kk, Tk in enumerate(hist):
    print(f"{kk}, {Tk[0]:.5f}, {Tk[1]:.5f}, {Tk[2]:.5f}, {np.linalg.norm(F(Tk)):.3e}")

solf, histf = newton_nd(F, J_fd, Tg, tol=1e-13)
print("Newton (J por dif. finitas): T =", solf, " it =", len(histf)-1)
print("max |J - J_fd| relativo en la solucion:", np.max(np.abs(J(sol) - J_fd(sol)))/np.max(np.abs(J(sol))))

s2, info, ier, msg = fsolve(F, Tg, fprime=J, xtol=1e-13, full_output=True)
print("fsolve (J analitica):", s2, " nfev =", info['nfev'])
s3, info3, ier3, msg3 = fsolve(F, Tg, xtol=1e-13, full_output=True)
print("fsolve (J interna FD):", s3, " nfev =", info3['nfev'])
r = root(F, Tg, method='hybr', jac=J, tol=1e-13)
print("root hybr:", r.x, " nfev =", r.nfev)

# Verificacion de balance de energia: calor que entra a la aleta = calor perdido por los nodos 1..3
def perdidas_nodos(T, eps_val):
    w = np.array([P*dx, P*dx, P*dx/2 + Ac])
    conv = np.sum(w*h*(T - Tinf))
    rad = np.sum(w*eps_val*sigma*(T**4 - Tsur**4))
    return conv, rad
q_cond = kA_dx*(T0 - sol[0])
conv, rad = perdidas_nodos(sol, eps_e)
print(f"Calor que entra a la aleta (conduccion base->nodo 1): {q_cond:.3f} W")
print(f"Perdidas nodos 1-3: conveccion = {conv:.3f} W, radiacion = {rad:.3f} W, suma = {conv+rad:.3f} W")
# Referencia sin radiacion (lineal, 3x3)
eps_save = eps_e
eps_e = 0.0
sol_nr, _ = newton_nd(F, J, Tg, tol=1e-13)
eps_e = eps_save
print("Sin radiacion: T =", sol_nr)

# ---- Figuras ----
x = np.array([0, dx, 2*dx, 3*dx])
fig, ax = plt.subplots(1, 2, figsize=(10.5, 3.9))
ax[0].plot(x*100, np.r_[T0, sol] - 273.15, "o-", color=NAVY, label="con radiación")
ax[0].plot(x*100, np.r_[T0, sol_nr] - 273.15, "s--", color=GOLD, label="solo convección")
ax[0].set_xlabel("x [cm]"); ax[0].set_ylabel("T [°C]"); ax[0].legend()
ax[0].set_title("Perfil de temperatura en la aleta")
res = [np.linalg.norm(F(Tk)) for Tk in hist]
resf = [np.linalg.norm(F(Tk)) for Tk in histf]
ax[1].semilogy(res, "o-", color=NAVY, label="J analítica")
ax[1].semilogy(resf, "s--", color=GOLD, label="J por diferencias finitas")
ax[1].set_xlabel("iteración k"); ax[1].set_ylabel(r"$\|\mathbf{F}(\mathbf{T}_k)\|$ [W]")
ax[1].legend(); ax[1].set_title("Convergencia del residuo")
fig.tight_layout()
savefig(fig, "fig06_aleta.png")
