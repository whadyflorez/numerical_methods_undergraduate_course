# Método de Newton-Raphson (1 y varias variables) — Métodos Numéricos, Ing. Mecánica

- `newton_raphson.tex` / `newton_raphson.pdf`: presentación Beamer (47 páginas, 16:9).
- `scripts/`: un script de Python por ejemplo (cada uno genera sus figuras en `figs/` e imprime los números citados en las diapositivas).
  - `01` Newton 1D básico y orden de convergencia · `02` Colebrook · `03` viga en voladizo
  - `04` fallas de Newton · `05` mecanismo de cuatro barras (2x2) · `06` aleta con radiación (3x3)
  - `07` comparación global de la convergencia · `run_all.py` regenera todo.
- Requisitos Python: numpy, scipy, matplotlib.
- Compilar el PDF (dos pasadas): `pdflatex newton_raphson.tex` (necesita beamer, lmodern y babel-spanish).
