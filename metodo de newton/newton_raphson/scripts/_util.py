"""Utilidades compartidas: rutas, estilo de figuras y solvers de Newton-Raphson."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.normpath(os.path.join(HERE, "..", "figs"))
os.makedirs(FIGS, exist_ok=True)

NAVY = "#1F3864"
GOLD = "#C9A227"
RED = "#B03A2E"
GREEN = "#2E7D5B"
GRAY = "#6B6B6B"

plt.rcParams.update({
    "figure.dpi": 150, "savefig.dpi": 200, "axes.grid": True,
    "grid.alpha": 0.3, "axes.spines.top": False, "axes.spines.right": False,
    "font.size": 11, "axes.titlesize": 12,
})


def savefig(fig, name):
    path = os.path.join(FIGS, name)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print("figura guardada:", path)


def newton_1d(f, df, x0, tol=1e-12, maxit=50):
    """Newton-Raphson 1D. Devuelve (raiz, historial de iterados)."""
    x = float(x0)
    hist = [x]
    for _ in range(maxit):
        dfx = df(x)
        if dfx == 0.0:
            raise ZeroDivisionError("f'(x)=0: Newton no puede continuar")
        dx = -f(x) / dfx
        x = x + dx
        hist.append(x)
        if abs(dx) < tol * max(1.0, abs(x)):
            break
    return x, np.array(hist)


def newton_nd(F, J, x0, tol=1e-12, maxit=50):
    """Newton-Raphson para sistemas. Resuelve J*dx = -F (sin invertir J).
    Devuelve (solucion, historial de iterados)."""
    x = np.array(x0, dtype=float)
    hist = [x.copy()]
    for _ in range(maxit):
        dx = np.linalg.solve(J(x), -F(x))
        x = x + dx
        hist.append(x.copy())
        if np.linalg.norm(dx) < tol * max(1.0, np.linalg.norm(x)):
            break
    return x, np.array(hist)
