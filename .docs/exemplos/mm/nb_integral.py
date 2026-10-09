import numpy as np

# notebook "Aula 3 - integral definida": f(x) = −x²/4 + 2x em [0, 8]
x = np.linspace(0, 8, 1_000_000)
f = lambda x: -(x ** 2) / 4 + 2 * x
y = f(x)
print("trapézios (np.trapezoid):", np.trapezoid(y, x))     # o notebook usa np.trapz

base = 0.001
med = np.arange((0 + base) / 2, 8, base)                   # pontos médios dos intervalos
print("ponto médio, base 0,001:", (base * f(med)).sum())

# notebook "Aula 3 - integral": ∫ sen x de 0 a π
x1 = np.arange(0, np.pi, 0.00001)
print("∫ sen x de 0 a π ≈", np.trapezoid(np.sin(x1), x1))
