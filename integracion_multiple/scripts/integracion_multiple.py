"""
Integracion doble y triple: rectangulos (punto medio), trapecios y Gauss-Legendre.
Metodos Numericos - pregrado.

Cada metodo aparece en dos versiones:
  * implementacion manual (para entender el mecanismo), y
  * comparacion con scipy.integrate (dblquad / tplquad) como referencia.
"""
import numpy as np
from math import erf, pi, sqrt
from scipy import integrate


# ------------------------------------------------------------------ reglas 2D manuales
def rectangulo_2d(f, a, b, c, d, nx, ny):
    """Regla del rectangulo (punto medio) compuesta en [a,b]x[c,d]."""
    hx, hy = (b - a) / nx, (d - c) / ny
    xm = a + hx * (np.arange(nx) + 0.5)          # centros de celda en x
    ym = c + hy * (np.arange(ny) + 0.5)          # centros de celda en y
    X, Y = np.meshgrid(xm, ym, indexing="ij")
    return hx * hy * np.sum(f(X, Y))


def trapecio_2d(f, a, b, c, d, nx, ny):
    """Regla del trapecio compuesta en [a,b]x[c,d] (pesos 1-2-4)."""
    hx, hy = (b - a) / nx, (d - c) / ny
    x = np.linspace(a, b, nx + 1)
    y = np.linspace(c, d, ny + 1)
    wx = np.full(nx + 1, 2.0); wx[[0, -1]] = 1.0
    wy = np.full(ny + 1, 2.0); wy[[0, -1]] = 1.0
    W = np.outer(wx, wy)                         # 1 en esquinas, 2 en bordes, 4 en el interior
    X, Y = np.meshgrid(x, y, indexing="ij")
    return hx * hy / 4.0 * np.sum(W * f(X, Y))


def gauss_2d(f, a, b, c, d, nx, ny=None):
    """Gauss-Legendre producto tensorial en [a,b]x[c,d]."""
    ny = nx if ny is None else ny
    tx, wx = np.polynomial.legendre.leggauss(nx)  # nodos y pesos en [-1,1]
    ty, wy = np.polynomial.legendre.leggauss(ny)
    x = (b - a) / 2 * tx + (a + b) / 2           # cambio de variable a [a,b]
    y = (d - c) / 2 * ty + (c + d) / 2
    X, Y = np.meshgrid(x, y, indexing="ij")
    jac = (b - a) * (d - c) / 4                  # jacobiano de la transformacion
    return jac * np.sum(np.outer(wx, wy) * f(X, Y))


def gauss_2d_variable(f, a, b, c_fun, d_fun, n):
    """Gauss-Legendre en dominio no rectangular: a<=x<=b, c(x)<=y<=d(x)."""
    t, w = np.polynomial.legendre.leggauss(n)
    total = 0.0
    for ti, wi in zip(t, w):
        x = (b - a) / 2 * ti + (a + b) / 2
        c, d = c_fun(x), d_fun(x)
        y = (d - c) / 2 * t + (c + d) / 2
        interior = (d - c) / 2 * np.sum(w * f(x, y))   # integral en y para x fijo
        total += wi * interior
    return (b - a) / 2 * total


def gauss_3d(f, lims, n):
    """Gauss-Legendre producto tensorial en un paralelepipedo."""
    t, w = np.polynomial.legendre.leggauss(n)
    pts, jac = [], 1.0
    for (lo, hi) in lims:
        pts.append((hi - lo) / 2 * t + (lo + hi) / 2)
        jac *= (hi - lo) / 2
    X, Y, Z = np.meshgrid(*pts, indexing="ij")
    W = w[:, None, None] * w[None, :, None] * w[None, None, :]
    return jac * np.sum(W * f(X, Y, Z))


def trapecio_3d(f, lims, n):
    pts, h = [], []
    for (lo, hi) in lims:
        pts.append(np.linspace(lo, hi, n + 1)); h.append((hi - lo) / n)
    w1 = np.full(n + 1, 1.0); w1[1:-1] = 2.0
    W = w1[:, None, None] * w1[None, :, None] * w1[None, None, :]
    X, Y, Z = np.meshgrid(*pts, indexing="ij")
    return np.prod(h) / 8 * np.sum(W * f(X, Y, Z))


# ------------------------------------------------------------------ ejemplo 1
if __name__ == "__main__":
    f = lambda x, y: np.exp(-(x**2 + y**2))
    I_ex = (sqrt(pi) / 2 * erf(1.0)) ** 2
    print(f"Ejemplo 1: I = int_0^1 int_0^1 exp(-(x^2+y^2)) dy dx = {I_ex:.10f}")
    I_sp, err_sp = integrate.dblquad(lambda y, x: f(x, y), 0, 1, 0, 1)
    print(f"  scipy dblquad = {I_sp:.10f} (est. error {err_sp:.1e})")

    print("\n  n   N_eval  rectangulo   err_R       trapecio    err_T      err_R/err_T")
    for n in (2, 4, 8, 16, 32):
        R = rectangulo_2d(f, 0, 1, 0, 1, n, n)
        T = trapecio_2d(f, 0, 1, 0, 1, n, n)
        print(f"{n:3d} {n*n:5d}/{(n+1)**2:<5d} {R:.8f} {R-I_ex:+.2e}  {T:.8f} {T-I_ex:+.2e}  {(R-I_ex)/(T-I_ex):+.3f}")

    print("\n  Gauss n x n:")
    for n in (1, 2, 3, 4, 5, 6):
        G = gauss_2d(f, 0, 1, 0, 1, n)
        print(f"  n={n} N={n*n:3d}  G={G:.12f}  err={G-I_ex:+.2e}")

    # Detalle 2x2 a mano
    t = 1 / sqrt(3)
    nodos = [0.5 - 0.5 * t, 0.5 + 0.5 * t]
    print("\n  Gauss 2x2 detallado (pesos w=1, jacobiano 1/4):")
    s = 0
    for xi in nodos:
        for yj in nodos:
            print(f"   ({xi:.6f},{yj:.6f}) f={f(xi,yj):.6f}")
            s += f(xi, yj)
    print(f"   suma f = {s:.6f}  ->  I = {s/4:.6f}")

    # puntos 2x2 trapecio y rectangulo con n=1 y n=2 para comparar costo de 4 evaluaciones
    print(f"  Rect n=2 (4 eval) = {rectangulo_2d(f,0,1,0,1,2,2):.6f}; Trap n=1 (4 eval)= {trapecio_2d(f,0,1,0,1,1,1):.6f}")

    # ------------------------------------------------------------------ ejemplo 2 polinomio
    p = lambda x, y: x**3 * y**2 + x * y
    print("\nEjemplo 2: int_0^2 int_0^1 (x^3 y^2 + x y) dy dx = 7/3 =", 7 / 3)
    for n in (1, 2, 3):
        print(f"  Gauss {n}x{n}: {gauss_2d(p,0,2,0,1,n):.12f}")
    for n in (2, 4, 8):
        print(f"  Trap n={n}: {trapecio_2d(p,0,2,0,1,n,n):.8f}  Rect n={n}: {rectangulo_2d(p,0,2,0,1,n,n):.8f}")

    # ------------------------------------------------------------------ ejemplo 3 cuarto de circulo
    print("\nEjemplo 3: momento polar de inercia de un cuarto de circulo R=1: J = pi/8 =", pi / 8)
    g = lambda x, y: x**2 + y**2
    for n in (2, 3, 4, 6, 8, 16):
        Jc = gauss_2d_variable(g, 0, 1, lambda x: 0.0 * x, lambda x: np.sqrt(1 - x**2), n)
        print(f"  cartesianas Gauss n={n:2d} (N={n*n:3d}): {Jc:.10f} err={Jc-pi/8:+.2e}")
    # polares: int_0^{pi/2} int_0^1 r^2 * r dr dtheta
    gp = lambda r, th: r**3 + 0 * th
    for n in (1, 2):
        Jp = gauss_2d(gp, 0, 1, 0, pi / 2, n)
        print(f"  polares Gauss {n}x{n}: {Jp:.12f} err={Jp-pi/8:+.2e}")
    Jsp, _ = integrate.dblquad(lambda y, x: x**2 + y**2, 0, 1, 0, lambda x: np.sqrt(1 - x**2))
    print(f"  scipy dblquad = {Jsp:.10f}")

    # ------------------------------------------------------------------ ejemplo 4 triple
    h3 = lambda x, y, z: np.exp(-(x**2 + y**2 + z**2))
    I3 = (sqrt(pi) / 2 * erf(1.0)) ** 3
    print(f"\nEjemplo 4: integral triple en [0,1]^3 = {I3:.10f}")
    for n in (2, 3, 4):
        G3 = gauss_3d(h3, [(0, 1)] * 3, n)
        print(f"  Gauss {n}^3 (N={n**3}): {G3:.10f} err={G3-I3:+.2e}")
    for n in (4, 8, 16):
        T3 = trapecio_3d(h3, [(0, 1)] * 3, n)
        print(f"  Trap n={n} (N={(n+1)**3}): {T3:.10f} err={T3-I3:+.2e}")
    I3sp, _ = integrate.tplquad(lambda z, y, x: h3(x, y, z), 0, 1, 0, 1, 0, 1)
    print(f"  scipy tplquad = {I3sp:.10f}")

    # ------------------------------------------------------------------ maldicion de la dimension
    print("\nPuntos necesarios con 10 puntos por eje:")
    for dmn in (1, 2, 3, 6, 10):
        print(f"  d={dmn}: {10**dmn:.0e}")
