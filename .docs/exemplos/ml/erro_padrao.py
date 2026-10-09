from math import sqrt
from statistics import NormalDist

# resistores: μ = 100 Ω, σ = 10 Ω, n = 25
ep = 10 / sqrt(25)                                   # erro padrão σ/√n
print(f"erro padrão = {ep}")
print(f"P(x̄ <= 95) = {NormalDist(100, ep).cdf(95):.4f}")

# alturas: μ = 170 cm, σ = 5 cm, n = 40 — exercício 3a pede P(x̄ > 172)
medias = NormalDist(170, 5 / sqrt(40))
print(f"cdf(172)     = {medias.cdf(172):.4f}   <- área à ESQUERDA")
print(f"1 - cdf(172) = {1 - medias.cdf(172):.4f}   <- P(x̄ > 172), a resposta correta")
