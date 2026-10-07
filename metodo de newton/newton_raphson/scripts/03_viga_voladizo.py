"""03 - Frecuencias naturales de una viga en voladizo (vibraciones mecanicas).
Ecuacion caracteristica: 1 + cos(lam) cosh(lam) = 0, con lam = beta*L.
Se usa la forma escalada g(lam) = cos(lam) + 1/cosh(lam) para evitar overflow de cosh."""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from _util import *

g = lambda l: np.cos(l) + 1/np.cosh(l)
dg = lambda l: -np.sin(l) - np.tanh(l)/np.cosh(l)

# Raices de referencia con brentq (intervalos buscados con la grafica)
brackets = [(1.5, 2.5), (4.0, 5.0), (7.0, 8.5), (10.0, 11.5)]
refs = [brentq(g, a, b, xtol=1e-14) for a, b in brackets]
print("raices de referencia (brentq):", [f"{r:.6f}" for r in refs])

# Newton desde varias semillas
print("semilla -> raiz, iteraciones")
for x0 in [1.0, 2.0, 3.0, 4.0, 5.0, 6.5, 8.0]:
    try:
        r, h = newton_1d(g, dg, x0, tol=1e-13, maxit=60)
        print(f"x0={x0}: raiz={r:.6f}, it={len(h)-1}")
    except ZeroDivisionError as ex:
        print(f"x0={x0}: {ex}")

# Datos de la viga (acero)
E, rho = 200e9, 7850.0
L, b, hh = 0.5, 0.02, 0.005
I = b*hh**3/12; A = b*hh
print(f"I = {I:.4e} m^4, A = {A:.3e} m^2")
for n, lam in enumerate(refs[:3], start=1):
    w = lam**2*np.sqrt(E*I/(rho*A*L**4))
    print(f"modo {n}: lam={lam:.4f}, omega={w:.2f} rad/s, f={w/(2*np.pi):.2f} Hz")

# ---- Figura 1: funcion y raices ----
xx = np.linspace(0, 12, 800)
fig, ax = plt.subplots(figsize=(7.2, 3.8))
ax.plot(xx, g(xx), color=NAVY, lw=2)
ax.axhline(0, color="k", lw=0.8)
for i, r in enumerate(refs):
    ax.plot(r, 0, "o", color=RED, ms=7)
    ax.annotate(fr"$\lambda_{i+1}={r:.3f}$", (r, 0), textcoords="offset points",
                xytext=(0, 12 if i % 2 == 0 else -18), ha="center", fontsize=9, color=RED)
ax.set_xlabel(r"$\lambda=\beta L$"); ax.set_ylabel(r"$\cos\lambda+1/\cosh\lambda$")
savefig(fig, "fig03_viga_raices.png")

# ---- Figura 2: cuencas de atraccion ----
x0s = np.linspace(0.05, 12, 1500)
which = np.full(x0s.shape, np.nan)
for i, x0 in enumerate(x0s):
    try:
        r, h = newton_1d(g, dg, x0, tol=1e-12, maxit=80)
        if abs(g(r)) < 1e-9 and r > 0:
            j = np.argmin([abs(r - q) for q in refs + [14.137167]])
            which[i] = r
    except Exception:
        pass
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.plot(x0s, which, ".", ms=2.5, color=NAVY)
for r in refs:
    ax.axhline(r, color=GOLD, lw=0.8, ls="--")
ax.set_xlabel(r"semilla $\lambda_0$"); ax.set_ylabel("raíz a la que converge")
ax.set_ylim(0, 16)
savefig(fig, "fig03b_cuencas.png")
# resumen de cuencas
nearest = {}
for x0, r in zip(x0s, which):
    if not np.isnan(r):
        nearest.setdefault(round(r, 3), []).append(x0)
for r, lst in sorted(nearest.items()):
    print(f"raiz {r}: {len(lst)} semillas de {len(x0s)}  (rango {min(lst):.2f}-{max(lst):.2f})")
