import math

def integral(f, a, b, n=100_000):
    h = (b - a) / n
    return sum(f(a + (k + 0.5) * h) for k in range(n)) * h

print("∫ x² de −1 a 1     =", round(integral(lambda x: x * x, -1, 1), 6), "(exato 2/3)")
print("∫ x de −2 a 2      =", round(integral(lambda x: x, -2, 2), 6) + 0.0, "(áreas +2 e −2 se cancelam)")
print("∫ sen x de 0 a π   =", round(integral(math.sin, 0, math.pi), 6))
print("∫ sen x de 0 a 3π/2 =", round(integral(math.sin, 0, 3 * math.pi / 2), 6))

# Índice de Gini = 2·∫₀¹ (x − L(x)) dx  (resolução das anotações da aula 4)
gini = lambda L: 2 * integral(lambda x: x - L(x), 0, 1)
print("Gini, L(x) = x²              =", round(gini(lambda x: x * x), 4))
print("Gini, L(x) = 0,7604·x^2,0926 =", round(gini(lambda x: 0.7604 * x ** 2.0926), 5))
