"""05 - Analisis de posicion de un mecanismo de cuatro barras (cinematica) con Newton 2x2.
Ecuaciones de cierre de lazo: r2 e^{i th2} + r3 e^{i th3} = r1 + r4 e^{i th4}
Incognitas: th3 (acoplador), th4 (balancin) dado th2 (manivela)."""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from _util import *

r1, r2, r3, r4 = 0.30, 0.10, 0.25, 0.20          # m  (bancada, manivela, acoplador, balancin)
print("Grashof: s+l =", min(r1,r2,r3,r4)+max(r1,r2,r3,r4), " p+q =", r1+r2+r3+r4-min(r1,r2,r3,r4)-max(r1,r2,r3,r4))

def make_system(th2):
    def F(u):
        th3, th4 = u
        return np.array([r2*np.cos(th2) + r3*np.cos(th3) - r4*np.cos(th4) - r1,
                         r2*np.sin(th2) + r3*np.sin(th3) - r4*np.sin(th4)])
    def J(u):
        th3, th4 = u
        return np.array([[-r3*np.sin(th3),  r4*np.sin(th4)],
                         [ r3*np.cos(th3), -r4*np.cos(th4)]])
    return F, J

# ---- Una posicion: th2 = 60 deg ----
th2 = np.radians(60)
F, J = make_system(th2)
u0 = np.radians([20.0, 90.0])
u, hist = newton_nd(F, J, u0, tol=1e-13)
print(f"th2=60: th3 = {np.degrees(u[0]):.4f} deg, th4 = {np.degrees(u[1]):.4f} deg, iteraciones={len(hist)-1}")
print("k, th3[deg], th4[deg], ||F||")
for k, uk in enumerate(hist):
    print(f"{k}, {np.degrees(uk[0]):.6f}, {np.degrees(uk[1]):.6f}, {np.linalg.norm(F(uk)):.3e}")
us, info, ier, msg = fsolve(F, u0, fprime=J, xtol=1e-13, full_output=True)
print(f"fsolve: th3={np.degrees(us[0]):.4f}, th4={np.degrees(us[1]):.4f}, nfev={info['nfev']}")

# ---- Otra rama (mecanismo cruzado) con otra semilla ----
u0c = np.radians([-20.0, -90.0])
uc, hc = newton_nd(F, J, u0c, tol=1e-13)
print(f"rama cruzada: th3 = {np.degrees(uc[0]):.4f}, th4 = {np.degrees(uc[1]):.4f}, it={len(hc)-1}")

# ---- Barrido de la manivela con continuacion (semilla = solucion anterior) ----
th2s = np.radians(np.arange(0, 361, 2.0))
sol = []; its = []
u_prev = u.copy()
for t2 in th2s:
    Fk, Jk = make_system(t2)
    u_prev, hk = newton_nd(Fk, Jk, u_prev, tol=1e-12)
    sol.append(u_prev.copy()); its.append(len(hk)-1)
sol = np.array(sol)
print("iteraciones por posicion: min", min(its), "max", max(its), "prom", np.mean(its))
th4_deg = np.degrees(np.unwrap(sol[:, 1]))
print("th4 rango:", th4_deg.min(), th4_deg.max())

# Sin continuacion (semilla fija) -> ramas mezcladas / fallas
fails = 0; wrong = 0
for t2, uref in zip(th2s, sol):
    Fk, Jk = make_system(t2)
    try:
        ui, hi = newton_nd(Fk, Jk, np.radians([20.0, 90.0]), tol=1e-12, maxit=30)
        if np.linalg.norm(Fk(ui)) > 1e-9: fails += 1
        elif np.linalg.norm(((ui - uref + np.pi) % (2*np.pi)) - np.pi) > 1e-6: wrong += 1
    except np.linalg.LinAlgError:
        fails += 1
print(f"semilla fija: {fails} fallas, {wrong} convergen a otra rama, de {len(th2s)} posiciones")

# ---- Singularidad del Jacobiano: det J = r3 r4 sin(th3 - th4)
det = np.array([np.linalg.det(make_system(t)[1](s)) for t, s in zip(th2s, sol)])
print("min |det J| en el barrido:", np.min(np.abs(det)), "en th2 =", np.degrees(th2s[np.argmin(np.abs(det))]))

# ---- Figuras ----
def pts(th2_, th3_, th4_):
    O2 = np.array([0, 0]); O4 = np.array([r1, 0])
    A = O2 + r2*np.array([np.cos(th2_), np.sin(th2_)])
    B = O4 + r4*np.array([np.cos(th4_), np.sin(th4_)])
    return O2, O4, A, B
fig, ax = plt.subplots(figsize=(6.2, 4.2))
O2, O4, A, B = pts(th2, u[0], u[1])
ax.plot([O2[0], A[0]], [O2[1], A[1]], color=RED, lw=3, label=r"manivela $r_2$")
ax.plot([A[0], B[0]], [A[1], B[1]], color=NAVY, lw=3, label=r"acoplador $r_3$")
ax.plot([O4[0], B[0]], [O4[1], B[1]], color=GREEN, lw=3, label=r"balancín $r_4$")
ax.plot([O2[0], O4[0]], [0, 0], color=GRAY, lw=3, ls="--", label=r"bancada $r_1$")
for P, lab in [(O2, "$O_2$"), (O4, "$O_4$"), (A, "A"), (B, "B")]:
    ax.plot(*P, "ko", ms=6); ax.annotate(lab, P, textcoords="offset points", xytext=(6, 6))
ax.annotate(r"$\theta_2$", O2, textcoords="offset points", xytext=(25, 6), color=RED)
ax.set_aspect("equal"); ax.set_xlim(-0.12, 0.45); ax.set_ylim(-0.05, 0.25)
ax.legend(fontsize=8, loc="upper right"); ax.set_xlabel("x [m]"); ax.set_ylabel("y [m]")
savefig(fig, "fig05_mecanismo.png")

fig, ax = plt.subplots(1, 2, figsize=(10.5, 3.8))
ax[0].plot(np.degrees(th2s), th4_deg, color=NAVY, lw=2, label=r"$\theta_4$ (balancín)")
ax[0].plot(np.degrees(th2s), np.degrees(np.unwrap(sol[:, 0])), color=GOLD, lw=2, label=r"$\theta_3$ (acoplador)")
ax[0].set_xlabel(r"$\theta_2$ [°]"); ax[0].set_ylabel("ángulo [°]"); ax[0].legend()
ax[0].set_title("Posición del mecanismo (barrido con continuación)")
ax[1].plot(np.degrees(th2s), its, "o-", ms=3, color=NAVY)
ax[1].set_xlabel(r"$\theta_2$ [°]"); ax[1].set_ylabel("iteraciones de Newton")
ax[1].set_title("Costo por posición (semilla = solución previa)")
ax[1].set_ylim(0, 8)
fig.tight_layout()
savefig(fig, "fig05b_barrido.png")
