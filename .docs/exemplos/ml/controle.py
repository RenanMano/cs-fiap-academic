# Exercício 1 (material): triângulo escaleno — lados distintos dois a dois
for a, b, c in [(5, 7, 8), (10, 10, 12)]:
    if a != b and b != c and a != c:
        print(a, b, c, "-> É escaleno!")
    else:
        print(a, b, c, "-> Não é escaleno.")

# Exercício 2 (material): raiz quadrada só para x >= 0
for x in [-16, 81]:
    if x >= 0:
        print(x, "->", x ** (1 / 2))
    else:
        print(x, "-> O número é negativo")

# Repetição (material): cubos de 1 a 5 com for; 1, 11, ..., 91 com while
print([numero ** 3 for numero in range(1, 6)])
numero = 1
saltos = []
while numero < 100:
    saltos.append(numero)
    numero += 10
print(saltos)
