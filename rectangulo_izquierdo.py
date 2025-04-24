import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.sin(x)

# def f(x):
#     y=np.sin(x)
#     return y

a, b = 0, np.pi
n = 50
x = np.linspace(a, b, 100)
xi = np.linspace(a, b, n+1)
dx = (b - a) / n

plt.plot(x, f(x), label='f(x)=sin(x)')
for i in range(n):
    plt.bar(xi[i], f(xi[i]), width=dx, align='edge', alpha=0.3, edgecolor='k')
plt.title("Método del rectángulo izquierdo")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()
