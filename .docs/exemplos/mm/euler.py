import math

for n in (1, 2, 10, 100, 10_000, 1_000_000):
    print(f"n = {n:>9,}: (1 + 1/n)^n = {(1 + 1 / n) ** n:.9f}".replace(",", "."))
print(f"e = {math.e:.9f}")

# n enorme: 1 + 1/n perde dígitos no ponto flutuante e o resultado "passa" de e
for n in (10**9, 10**10, 10**12):
    ingenuo = (1 + 1 / n) ** n
    estavel = math.exp(n * math.log1p(1 / n))       # log1p(x) calcula ln(1 + x) sem perder precisão
    print(f"n = 10^{len(str(n)) - 1}: ingênuo = {ingenuo:.9f} {'> e!' if ingenuo > math.e else ''} | estável = {estavel:.9f}")
