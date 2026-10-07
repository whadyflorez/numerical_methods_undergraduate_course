"""07 - Comparacion de la convergencia de Newton en los 4 ejemplos de ingenieria
y estimacion numerica del orden de convergencia p."""
import warnings; warnings.filterwarnings("ignore")
import io, contextlib, importlib
import numpy as np
import matplotlib.pyplot as plt
from _util import *

def quiet_import(name):
    with contextlib.redirect_stdout(io.StringIO()):
        return importlib.import_module(name)

col = quiet_import("02_colebrook")
vig = quiet_import("03_viga_voladizo")
mec = quiet_import("05_cuatro_barras")
ale = quiet_import("06_aleta_radiacion")

series = {}
# 1) Colebrook, semilla pobre f0 = 0.5 (para ver mas iteraciones)
h = col.hist_b; series["Colebrook (1 var)"] = np.abs(h - h[-1])
# 2) Viga, lambda0 = 2.0 -> modo 1 ; error vs raiz de referencia
r, h = newton_1d(vig.g, vig.dg, 2.5, tol=1e-14); series[r"Viga voladizo (1 var), $\lambda_0=2.5$"] = np.abs(h - r)
# 3) Cuatro barras, semilla 20/90 grados
h = mec.hist; series["Cuatro barras (2 var)"] = np.linalg.norm(h - h[-1], axis=1)
# 4) Aleta con radiacion
h = ale.hist; series["Aleta con radiación (3 var)"] = np.linalg.norm(h - h[-1], axis=1)

print("Estimacion del orden p_k = ln(e_{k+1}/e_k) / ln(e_k/e_{k-1}):")
fig, ax = plt.subplots(figsize=(7.4, 4.3))
cols = [NAVY, GOLD, RED, GREEN]
for (name, e), c in zip(series.items(), cols):
    e = np.maximum(e, 1e-17)
    k = np.arange(len(e))
    ax.semilogy(k, e, "o-", color=c, label=name, ms=5)
    ee = e[e > 1e-14]
    ps = [np.log(ee[i+1]/ee[i])/np.log(ee[i]/ee[i-1]) for i in range(1, len(ee)-1)
          if ee[i+1] > 1e-14 and ee[i] != ee[i-1]]
    print(f"{name}: errores = {np.array2string(ee, precision=2)} ; p_k = {np.round(ps, 2)}")
ax.set_xlabel("iteración k"); ax.set_ylabel("error absoluto (norma)")
ax.set_xlim(0, 8); ax.set_ylim(1e-16, 1e1)
ax.legend(fontsize=8)
savefig(fig, "fig07_convergencia_global.png")
