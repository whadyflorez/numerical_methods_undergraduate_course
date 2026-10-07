"""01 - Newton-Raphson 1D: interpretacion geometrica y convergencia cuadratica."""
import numpy as np
import matplotlib.pyplot as plt
from _util import *

# ---- Ejemplo de calentamiento: raiz de x^2 - 2 ----
f = lambda x: x**2 - 2
df = lambda x: 2*x
root, hist = newton_1d(f, df, 1.0, tol=1e-15)
exact = np.sqrt(2)
print("k, x_k, error")
for k, xk in enumerate(hist):
    print(f"{k}, {xk:.15f}, {abs(xk-exact):.3e}")

# ---- Figura: construccion geometrica (tangentes) ----
g = lambda x: x**3 - 2*x - 5   # ejemplo clasico
dg = lambda x: 3*x**2 - 2
r, h = newton_1d(g, dg, 3.0, tol=1e-14)
print("raiz x^3-2x-5:", r, "iteraciones:", len(h)-1)
xx = np.linspace(1.8, 3.2, 300)
fig, ax = plt.subplots(figsize=(7.2, 4.2))
ax.plot(xx, g(xx), color=NAVY, lw=2.2, label=r"$f(x)=x^3-2x-5$")
ax.axhline(0, color="k", lw=0.8)
for k in range(3):
    xk = h[k]
    xn = h[k+1]
    xt = np.linspace(xn - 0.15, xk + 0.1, 20)
    ax.plot(xt, g(xk) + dg(xk)*(xt - xk), color=GOLD, lw=1.6,
            label="tangente" if k == 0 else None)
    ax.plot([xk, xk], [0, g(xk)], color=GRAY, lw=0.9, ls="--")
    ax.plot(xk, g(xk), "o", color=RED, ms=6)
    ax.annotate(fr"$x_{k}$", (xk, 0), textcoords="offset points", xytext=(0, -16),
                ha="center", color=RED)
ax.plot(r, 0, "s", color=GREEN, ms=8, label="raíz")
ax.set_xlabel("x"); ax.set_ylabel("f(x)"); ax.set_ylim(-8, 18)
ax.legend(loc="upper left")
savefig(fig, "fig01_tangentes.png")

# ---- Figura: orden de convergencia (error_{k+1} vs error_k) ----
e = np.abs(hist - exact)
e = e[e > 1e-14]
fig, ax = plt.subplots(figsize=(6.2, 4.2))
ax.loglog(e[:-1], e[1:], "o-", color=NAVY, label="Newton")
xs = np.logspace(-8, -0.3, 50)
ax.loglog(xs, xs**2*0.35, "--", color=GOLD, label=r"pendiente 2 ($e_{k+1}\propto e_k^2$)")
ax.loglog(xs, xs*0.5, ":", color=GRAY, label="pendiente 1 (lineal)")
ax.set_xlabel(r"$|e_k|$"); ax.set_ylabel(r"$|e_{k+1}|$"); ax.legend()
savefig(fig, "fig01b_orden_convergencia.png")
