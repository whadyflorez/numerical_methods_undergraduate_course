"""02 - Factor de friccion de Colebrook-White con Newton-Raphson (mecanica de fluidos).
Manual (Newton) vs scipy (newton, brentq) vs biseccion."""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton as sp_newton, brentq
from _util import *

# Datos: agua en tuberia de acero comercial
D = 0.050        # m   diametro interior
eps = 0.045e-3   # m   rugosidad absoluta (acero comercial)
Re = 1.0e5       # numero de Reynolds
rr = eps / D     # rugosidad relativa

# Incognita x = 1/sqrt(f). Colebrook:  x + 2 log10( rr/3.7 + 2.51 x / Re ) = 0
F = lambda x: x + 2*np.log10(rr/3.7 + 2.51*x/Re)
dF = lambda x: 1 + (2/np.log(10)) * (2.51/Re) / (rr/3.7 + 2.51*x/Re)

# Semilla: Haaland (formula explicita aproximada)
x_haal = -1.8*np.log10((rr/3.7)**1.11 + 6.9/Re)       # = 1/sqrt(f_Haaland)
f_haal = 1/x_haal**2
print(f"Haaland: f0 = {f_haal:.6f}  (x0 = {x_haal:.4f})")

root, hist = newton_1d(F, dF, x_haal, tol=1e-14)
f_new = 1/root**2
print(f"Newton (x0 de Haaland): f = {f_new:.8f}, iteraciones = {len(hist)-1}")
print("k, x_k, f_k=1/x^2, |F(x_k)|")
for k, xk in enumerate(hist):
    print(f"{k}, {xk:.10f}, {1/xk**2:.8f}, {abs(F(xk)):.3e}")

# Semilla pobre: f0 = 0.5  -> x0 = 1/sqrt(0.5)
x_bad = 1/np.sqrt(0.5)
root_b, hist_b = newton_1d(F, dF, x_bad, tol=1e-14)
print(f"Newton (f0=0.5): f = {1/root_b**2:.8f}, iteraciones = {len(hist_b)-1}")

# scipy
x_sp, info = sp_newton(F, x_haal, fprime=dF, tol=1e-14, full_output=True)
print(f"scipy.optimize.newton: f = {1/x_sp**2:.8f}, iteraciones = {info.iterations}, llamadas f = {info.function_calls}")
x_sec, info2 = sp_newton(F, x_haal, tol=1e-14, full_output=True)   # sin derivada -> secante
print(f"scipy newton sin derivada (secante): f = {1/x_sec**2:.8f}, iteraciones = {info2.iterations}")
x_br, info3 = brentq(F, 3.0, 12.0, xtol=1e-14, full_output=True)
print(f"scipy.optimize.brentq: f = {1/x_br**2:.8f}, iteraciones = {info3.iterations}")

# biseccion manual, mismo criterio
def bisect(fun, a, b, tol=1e-14):
    n = 0
    while (b - a) > tol*max(1, abs(a)):
        m = 0.5*(a+b); n += 1
        if fun(a)*fun(m) <= 0: b = m
        else: a = m
    return 0.5*(a+b), n
x_bi, n_bi = bisect(F, 3.0, 12.0)
print(f"biseccion: f = {1/x_bi**2:.8f}, iteraciones = {n_bi}")

# Intervalo de Newton en f directamente (para contraste, mostrar que la variable importa)
Fq = lambda f_: 1/np.sqrt(f_) + 2*np.log10(rr/3.7 + 2.51/(Re*np.sqrt(f_)))
dFq = lambda f_: (-0.5*f_**-1.5)*(1 + (2/np.log(10))*(2.51/Re)/(rr/3.7 + 2.51/(Re*np.sqrt(f_))))
for f0 in [0.02, 0.05, 0.001]:
    try:
        r_, h_ = newton_1d(Fq, dFq, f0, tol=1e-12, maxit=30)
        print(f"Newton sobre f directo, f0={f0}: f={r_:.8f}, it={len(h_)-1}")
    except Exception as ex:
        print(f"Newton sobre f directo, f0={f0}: falla ({ex})")

# Perdida de carga: caudal tipico
rho, mu = 998.0, 1.0e-3
V = Re*mu/(rho*D)
L = 100.0
dP = f_new * (L/D) * rho * V**2 / 2
print(f"V = {V:.3f} m/s, caida de presion en L=100 m: {dP/1e3:.2f} kPa")

# ---- Figuras ----
fig, ax = plt.subplots(figsize=(6.4, 4.4))
Res = np.logspace(4, 7, 80)
max_it = 0
for rr_, c in zip([0.0, 0.0005, 0.001, 0.005, 0.02], [GRAY, NAVY, GOLD, GREEN, RED]):
    fs = []
    for R in Res:
        Fx = lambda x: x + 2*np.log10(rr_/3.7 + 2.51*x/R)
        dFx = lambda x: 1 + (2/np.log(10))*(2.51/R)/(rr_/3.7 + 2.51*x/R)
        xh = -1.8*np.log10((rr_/3.7)**1.11 + 6.9/R)
        r_, h_ = newton_1d(Fx, dFx, xh, tol=1e-12)
        max_it = max(max_it, len(h_) - 1)
        fs.append(1/r_**2)
    ax.loglog(Res, fs, color=c, label=fr"$\varepsilon/D={rr_}$")
print("Maximo de iteraciones de Newton (semilla Haaland, tol 1e-12) en todo el diagrama de Moody (5 x 80 casos):", max_it)
ax.set_xlabel("Re"); ax.set_ylabel("f (factor de fricción de Darcy)")
ax.legend(fontsize=9)
savefig(fig, "fig02_moody.png")

fig, ax = plt.subplots(figsize=(5.6, 4.2))
ks = np.arange(len(hist))
ax.semilogy(ks, np.abs(hist - hist[-1]) + 1e-17, "o-", color=NAVY, label="semilla Haaland")
ksb = np.arange(len(hist_b))
ax.semilogy(ksb, np.abs(hist_b - hist_b[-1]) + 1e-17, "s-", color=GOLD, label=r"semilla $f_0=0.5$")
ax.set_xlabel("iteración k"); ax.set_ylabel(r"$|x_k - x^*|$")
ax.legend()
savefig(fig, "fig02b_convergencia.png")
