# Questão 4 da parte teórica: estimativa de operações no pior caso (ordem de grandeza)
import math

def custos(n, buscas):
    log_n = math.ceil(math.log2(n + 1))                  # passos da busca binária no pior caso
    a = buscas * n                                       # (A) só buscas lineares
    b_rapida = n * log_n + buscas * log_n                # (B) ordenação O(n log n) + binárias
    b_quadratica = n * (n - 1) // 2 + buscas * log_n     # (B) com Bubble/Selection: n(n-1)/2
    return log_n, a, b_rapida, b_quadratica

for n, buscas in ((1_000_000, 50_000), (800_000, 40_000), (600_000, 70_000)):
    log_n, a, b1, b2 = custos(n, buscas)
    print(f"n={n:,} e {buscas:,} buscas (log2 n ≈ {log_n})".replace(",", "."))
    print(f"  (A) lineares:                     {a:.2e}")
    print(f"  (B) O(n log n) + binárias:        {b1:.2e}  -> cerca de {a / b1:.0f} vezes menos que (A)")
    print(f"  (B) ordenação O(n²) + binárias:   {b2:.2e}")
