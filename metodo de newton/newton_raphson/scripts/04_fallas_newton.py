"""04 - Cuando Newton falla: ciclos, divergencia, raices multiples."""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from _util import *

# (a) Ciclo: f(x) = x^3 - 2x + 2, x0 = 0  ->  0, 1, 0, 1, ...
f1 = lambda x: x**3 - 2*x + 2
d1 = lambda x: 3*x**2 - 2
_, h1 = newton_1d(f1, d1, 0.0, tol=1e-14, maxit=8)
print("ciclo:", h1)

# (b) Divergencia: f(x) = arctan(x); converge si |x0| < 1.3917
f2, d2 = np.arctan, lambda x: 1/(1 + x**2)
_, h2 = newton_1d(f2, d2, 1.5, tol=1e-14, maxit=6)
_, h2b = newton_1d(f2, d2, 1.0, tol=1e-14, maxit=8)
print("arctan x0=1.5:", h2)
print("arctan x0=1.0:", h2b)

# (c) Raiz doble: f(x) = (x-1)^2 (x+2): convergencia lineal con factor 1/2
f3 = lambda x: (x - 1)**2*(x + 2)
d3 = lambda x: 2*(x - 1)*(x + 2) + (x - 1)**2
_, h3 = newton_1d(f3, d3, 2.0, tol=1e-15, maxit=30)
# Newton modificado con multiplicidad m=2:  x - m f/f'
x = 2.0; h3m = [x]
for _ in range(8):
    x = x - 2*f3(x)/d3(x) if d3(x) != 0 else x
    h3m.append(x)
    if abs(f3(x)) < 1e-300: break
e3 = np.abs(h3 - 1.0)
print("raiz doble, error:", e3[:10])
print("cociente e_{k+1}/e_k:", (e3[1:10]/e3[:9]))
print("modificado:", np.abs(np.array(h3m) - 1.0))

fig, ax = plt.subplots(1, 3, figsize=(12, 3.6))
xx = np.linspace(-1.8, 1.8, 300)
ax[0].plot(xx, f1(xx), color=NAVY, lw=2); ax[0].axhline(0, color="k", lw=0.8)
for xk in [0.0, 1.0]:
    xt = np.linspace(xk - 0.9, xk + 0.9, 10)
    ax[0].plot(xt, f1(xk) + d1(xk)*(xt - xk), color=GOLD, lw=1.4)
    ax[0].plot(xk, f1(xk), "o", color=RED)
ax[0].set_ylim(-4, 6); ax[0].set_title("(a) Ciclo 0 ↔ 1")
xx = np.linspace(-4, 4, 300)
ax[1].plot(xx, f2(xx), color=NAVY, lw=2); ax[1].axhline(0, color="k", lw=0.8)
ax[1].plot(h2[:4], f2(h2[:4]), "o-", color=RED, ms=5, lw=0.8)
ax[1].set_title(r"(b) Divergencia ($\arctan x$, $x_0=1.5$)")
ax[2].semilogy(np.arange(len(e3)), e3 + 1e-17, "o-", color=NAVY, label="Newton clásico (m=2)")
ax[2].semilogy(np.arange(len(h3m)), np.abs(np.array(h3m) - 1.0) + 1e-17, "s-", color=GOLD, label="Newton modificado")
ax[2].set_xlabel("k"); ax[2].set_ylabel(r"$|x_k-1|$"); ax[2].legend(fontsize=8)
ax[2].set_title("(c) Raíz doble")
fig.tight_layout()
savefig(fig, "fig04_fallas.png")
