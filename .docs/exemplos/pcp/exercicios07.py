import random

random.seed(5)
print("1)", [round(random.uniform(0, 10), 2) for _ in range(4)])

notas = [7.0, 5.5, 8.0, 7.0, 9.5, 4.0]
media = sum(notas) / len(notas)
print(f"2) média {media:.2f} | iguais {sum(n == media for n in notas)} | acima {sum(n > media for n in notas)} | abaixo {sum(n < media for n in notas)}")

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for mes, d in list(zip(meses, dias))[:3]:
    print(f"3) O mês de {mes} tem {d} dias ao todo.")

print("4) soma:", sum([3, 8, -1, 10]))

nomes = ["Ana", "Bia", "Caio"]                  # 5) lidos até um Enter vazio
print("5)", nomes[::-1])

v = list("python")                              # 6) inversão por trocas
for i in range(len(v) // 2):
    v[i], v[-1 - i] = v[-1 - i], v[i]
print("6)", "".join(v))

m = [[random.randint(0, 9) for _ in range(4)] for _ in range(3)]
print("7)", m)

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
print("8) A + B =", C)
