# "Modelo de linguagem" de brinquedo: conta qual palavra segue cada palavra
from collections import Counter, defaultdict

corpus = [
    "eu adoro comer bolo de chocolate",
    "eu adoro comer sanduíche",
    "eu adoro comer bolo de cenoura",
    "eu adoro comer em restaurante italiano",
    "eu gosto de comer bolo de chocolate",
]

seguintes = defaultdict(Counter)
for frase in corpus:
    palavras = frase.split()
    for atual, proxima in zip(palavras, palavras[1:]):   # pares (entrada, saída)
        seguintes[atual][proxima] += 1

def gerar(inicio, n=4):
    palavras = inicio.split()
    for _ in range(n):
        opcoes = seguintes.get(palavras[-1])
        if not opcoes:
            break
        palavras.append(opcoes.most_common(1)[0][0])     # escolhe a mais frequente
    return " ".join(palavras)

print("Depois de 'comer':", dict(seguintes["comer"]))
print(gerar("eu adoro comer"))
