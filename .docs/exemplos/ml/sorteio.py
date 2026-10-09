import numpy as np
from collections import Counter

Amostra = ["Gabriel", "Gustavo", "Lucas", "Camila", "João", "Gabriela"]
vies = [0.1, 0.2, 0.05, 0.15, 0.1, 0.4]

rng = np.random.default_rng(7)                 # gerador com semente: resultado reprodutível
print([str(nome) for nome in rng.choice(Amostra, size=3, replace=False, p=vies)])

# frequência de cada nome como 1º sorteado em 10 mil sorteios viciados
primeiros = Counter(str(rng.choice(Amostra, p=vies)) for _ in range(10_000))
for nome, p in zip(Amostra, vies):
    print(f"{nome:<9} esperado {p:.2f} | observado {primeiros[nome] / 10_000:.2f}")
