# Como as contagens crescem com n (listas embaralhadas com semente fixa)
import random

def contar(lista):
    n = len(lista)
    bubble_comp = n * (n - 1) // 2                     # sempre, na versão sem parada antecipada
    inv = sum(1 for i in range(n) for j in range(i + 1, n) if lista[i] > lista[j])
    return bubble_comp, inv

gerador = random.Random(2026)
print("    n   comp. Bubble/Selection   inversões (trocas Bubble = desloc. Insertion)")
for n in (50, 100, 200, 400):
    lista = list(range(n))
    gerador.shuffle(lista)
    comp, inv = contar(lista)
    print(f"{n:5} {comp:24} {inv:12}   (≈ n²/4 = {n * n // 4})")
