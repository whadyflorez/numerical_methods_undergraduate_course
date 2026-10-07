"""Regenera todas las figuras y resultados. Uso: python run_all.py"""
import subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
scripts = sorted(f for f in os.listdir(HERE) if f[:2].isdigit() and f.endswith(".py"))
ok = True
for s in scripts:
    r = subprocess.run([sys.executable, os.path.join(HERE, s)], capture_output=True, text=True, cwd=HERE)
    print(f"[{'OK ' if r.returncode == 0 else 'FAIL'}] {s}")
    if r.returncode != 0:
        ok = False; print(r.stderr[-800:])
sys.exit(0 if ok else 1)
