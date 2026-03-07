
# ## Gradiente Conjugado — Material para clase

# ### El algoritmo (pseudo-código limpio)
# ```
# DADO: A (SPD), b, tolerancia
# x ← 0
# r ← b − A·x       ← residuo inicial
# p ← r              ← primera dirección de búsqueda

# MIENTRAS ‖r‖ > tol:
#     α ← (rᵀr) / (pᵀAp)    ← paso óptimo
#     x ← x + α·p            ← actualizar solución
#     r ← r − α·Ap           ← actualizar residuo
#     β ← (r_nuevo·r_nuevo) / (r·r)
#     p ← r_nuevo + β·p      ← nueva dirección conjugada

# RETORNAR x

import numpy as np
import time

# ─────────────────────────────────────────────────────
#  MÉTODO ITERATIVO: Gradiente Conjugado
#  Resuelve A·x = b  donde A es simétrica definida positiva (SPD)
# ─────────────────────────────────────────────────────

def gradiente_conjugado(A, b, tol=1e-6, max_iter=10):
    """
    A        : matriz SPD  (ndarray n×n)
    b        : lado derecho (ndarray n)
    tol      : tolerancia para ‖r‖
    Retorna  : (x, número_iters, lista_residuos)
    """
    n = len(b)

    # --- Inicialización ---
    x     = np.zeros(n)     # x₀ = vector cero
    r     = b - A @ x      # r₀ = b − A·x₀
    p     = r.copy()        # p₀ = r₀  (primera dirección de búsqueda)
    r_dot = r @ r           # rₖᵀ rₖ  (producto interno actual)

    residuos = [np.sqrt(r_dot)]

    for k in range(max_iter):

        Ap    = A @ p                  # producto matriz-vector (lo más costoso)
        alpha = r_dot / (p @ Ap)      # αₖ = paso óptimo

        x = x + alpha * p             # xₖ₊₁ = xₖ + αₖ pₖ
        r = r - alpha * Ap            # rₖ₊₁ = rₖ − αₖ A pₖ

        r_dot_nuevo = r @ r
        residuos.append(np.sqrt(r_dot_nuevo))

        if np.sqrt(r_dot_nuevo) < tol:
            return x, k+1, residuos   # convergió

        beta = r_dot_nuevo / r_dot    # βₖ
        p    = r + beta * p           # pₖ₊₁ = rₖ₊₁ + βₖ pₖ  (nueva dirección conjugada)
        r_dot = r_dot_nuevo

    return x, max_iter, residuos      # devolver aunque no converja


# ─────────────────────────────────────────────────────
#  EJEMPLO 1: sistema 2×2 verificable a mano
#  Solución exacta conocida: x = [1/11, 7/11]
# ─────────────────────────────────────────────────────

A_small = np.array([[4, 1],
                    [1, 3]], dtype=float)
b_small = np.array([1, 2], dtype=float)

x, iters, res = gradiente_conjugado(A_small, b_small, tol=1e-12)
print(f"Solución   : {x}")       # [0.09090909, 0.63636364]
print(f"Iteraciones: {iters}")   # 2  (exacto para sistema 2×2)
print()


# ─────────────────────────────────────────────────────
#  EJEMPLO 2: sistema 500×500 — comparación de tiempos
#  A = BᵀB + nI  →  SPD garantizada y bien condicionada
# ─────────────────────────────────────────────────────

np.random.seed(42)
n = 500
B      = np.random.randn(n, n)
A      = B.T @ B + n * np.eye(n)   # SPD garantizada
x_real = np.random.randn(n)
b      = A @ x_real                # conocemos la solución exacta

# --- Método iterativo ---
t0 = time.perf_counter()
x_gc, iters, residuos = gradiente_conjugado(A, b)
t_gc = time.perf_counter() - t0

# --- Método directo (numpy usa LAPACK/LU internamente) ---
t0 = time.perf_counter()
x_np = np.linalg.solve(A, b)
t_np = time.perf_counter() - t0

print("=== Gradiente Conjugado ===")
print(f"  Iteraciones : {iters}")
print(f"  Tiempo      : {t_gc:.4f} s")
print(f"  Error ‖x-x*‖: {np.linalg.norm(x_gc - x_real):.2e}")

print("\n=== numpy.linalg.solve (LU) ===")
print(f"  Tiempo      : {t_np:.4f} s")
print(f"  Error ‖x-x*‖: {np.linalg.norm(x_np - x_real):.2e}")


# ─────────────────────────────────────────────────────
#  ESCALADO: ¿cómo crece el tiempo con n?
# ─────────────────────────────────────────────────────

print(f"\n{'n':>6} | {'GC (s)':>9} | {'LU (s)':>9} | ratio LU/GC")
print("-"*45)
for n in [100, 500, 1000, 10000]:
    B = np.random.randn(n, n)
    A = B.T @ B + n * np.eye(n)
    b = A @ np.random.randn(n)

    t0 = time.perf_counter(); gradiente_conjugado(A, b); t_gc = time.perf_counter() - t0
    t0 = time.perf_counter(); np.linalg.solve(A, b);    t_np = time.perf_counter() - t0

    print(f"  {n:4d}  | {t_gc:9.4f} | {t_np:9.4f} | {t_np/t_gc:6.1f}x")

# impresion de los residuos

x_sol,iter,res=gradiente_conjugado(A, b, tol=1e-6, max_iter=10)

