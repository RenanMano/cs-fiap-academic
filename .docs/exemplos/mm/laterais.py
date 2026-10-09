def g(x):                                  # exercício 52 das anotações
    if x < 1:  return x
    if x == 1: return 3
    if x <= 2: return 2 - x**2
    return x - 3

h = 1e-9
for a in (1, 2):
    esq, dir_ = round(g(a - h), 6), round(g(a + h), 6)
    print(f"x→{a}⁻: {esq:>4}   x→{a}⁺: {dir_:>4}   g({a}) = {g(a)}   limite:", esq if esq == dir_ else "não existe")

aliquota = lambda renda: 0.0 if renda <= 35_000 else 0.07    # exemplo do imposto
print("imposto:", aliquota(35_000 - 1), "à esquerda |", aliquota(35_000 + 1), "à direita")

modulo_sobre_x = lambda x: abs(x) / x                         # exemplo 8, p. 86
print("|x|/x:", modulo_sobre_x(-1e-9), "à esquerda |", modulo_sobre_x(1e-9), "à direita")
for x in (-0.1, -0.001, 0.001, 0.1):
    print(f"1/x em x = {x:>6}: {1 / x:>8.1f}")
