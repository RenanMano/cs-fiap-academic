# Exercício 1 (pseudocódigo traduzido para Python)
x = 5
y = 10
z = 5 / y
x = x + 1
y = z
z = y + x
print("Ex. 1:", x, y, z)

# Exercício 2 — "a++" não existe em Python; equivale a a += 1
a = 2
b = 3
c = 2 + a
b = a
a = c
a = a + 1
a += 1
a += 1          # a++
b = c
c = b
b = a % 2
print("Ex. 2:", a, b, c)

# Exercício 3 — Resultado e resultado são variáveis DIFERENTES
x = y = z = 0
Resultado = x + y + z
x, y, z = 10, 25, 30
resultado = x + y + z
print("Ex. 3:", Resultado)
