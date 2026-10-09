print(*range(0, 101, 10))                                   # 2) 0 a 100 de 10 em 10

n = 7                                                       # 3) tabuada (trecho)
print([f"{n}x{i}={n * i}" for i in range(0, 4)], "...", f"{n}x25={n * 25}")

valores = [4, 17, -2, 9, 11]                                # 4) e 5) soma e maior
soma, maior = 0, valores[0]
for v in valores:
    soma += v
    if v > maior:
        maior = v
print("soma:", soma, "| maior:", maior)

print("pares até 15:", [p for p in range(2, 16) if p % 2 == 0])   # 6)

entradas = iter(["-3", "0", "10"])                          # 7) validação com while
n = int(next(entradas))
while n <= 0:
    print("valor inválido:", n)
    n = int(next(entradas))
total = 0
for i in range(1, n + 1):
    total += i
print(f"A soma de 1 até {n} é: {total}")

print("divisores de 28:", [d for d in range(1, 29) if 28 % d == 0])   # 8)

def eh_primo(x):                                           # 9) laços aninhados
    if x < 2:
        return False
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True

primos = [x for x in range(2, 2001) if eh_primo(x)]
print("primos de 2 a 2000:", len(primos), "| primeiros:", primos[:10], "| último:", primos[-1])
