x = [2, 4, 3, 4, 5, 2, 4]
n = len(x)

media = sum(x) / n
desvios = [xi - media for xi in x]
s2 = sum(d ** 2 for d in desvios) / (n - 1)      # variância amostral: divide por n - 1
s = s2 ** 0.5

rol = sorted(x)
mediana = rol[(n + 1) // 2 - 1] if n % 2 else (rol[n // 2 - 1] + rol[n // 2]) / 2

print("rol:", rol)
print(f"média = {sum(x)}/{n} = {media:.4f}")
print(f"soma dos desvios = {sum(desvios):.10f}")     # sempre zero: por isso se eleva ao quadrado
print(f"s² = {s2:.4f}   s = {s:.4f}   CV = {s / media * 100:.2f}%")
print("mediana (n ímpar, posição (n+1)/2 = 4):", mediana)
