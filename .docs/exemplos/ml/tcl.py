import random
from statistics import mean, pstdev

random.seed(42)
# população fortemente assimétrica: tempos de espera exponenciais com média 10 min
populacao = [random.expovariate(1 / 10) for _ in range(100_000)]
mu, sigma = mean(populacao), pstdev(populacao)

for n in (2, 30, 100):
    medias = [mean(random.sample(populacao, n)) for _ in range(2_000)]
    print(f"n = {n:>3}: média das médias = {mean(medias):5.2f} | "
          f"desvio das médias = {pstdev(medias):4.2f} | σ/√n = {sigma / n ** 0.5:4.2f}")
