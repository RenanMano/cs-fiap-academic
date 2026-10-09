from itertools import product
from collections import Counter
from statistics import mean, pvariance

populacao = [2, 4, 6, 8]
amostras = list(product(populacao, repeat=2))         # n = 2, com reposição: 4² = 16
medias = [mean(a) for a in amostras]

print("nº de amostras:", len(amostras))
dist = Counter(medias)
for m in sorted(dist):
    print(f"x̄ = {m}: {dist[m]}/16")

print("média das médias amostrais:", mean(medias), "| média populacional:", mean(populacao))
print("variância das médias:", pvariance(medias), "| σ²/n:", pvariance(populacao) / 2)
