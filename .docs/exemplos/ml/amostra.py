import random

random.seed(2026)                              # semente fixa: sorteio reprodutível
populacao = [f"Cirurgião {i:02d}" for i in range(1, 51)]
amostra = random.sample(populacao, 15)         # sorteio sem reposição

print("Tamanho da população (N):", len(populacao))
print("Tamanho da amostra (n):  ", len(amostra))
print("Fração amostral:          ", f"{len(amostra) / len(populacao):.0%}")
print("Todos pertencem à população?", set(amostra) <= set(populacao))
