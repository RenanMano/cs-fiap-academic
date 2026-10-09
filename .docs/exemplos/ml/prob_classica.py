from fractions import Fraction
from itertools import product
from collections import Counter

def classificar(p):
    if p == 0: return "impossível"
    if p == 1: return "certo"
    if p == Fraction(1, 2): return "provável (máxima incerteza)"
    return "pouco provável" if p < Fraction(1, 2) else "muito provável"

# genética (exercício dos slides): homem Ab x ab, mulher aB x ab
pai, mae = ["Ab", "ab"], ["aB", "ab"]
filhos = []
for gp, gm in product(pai, mae):
    filhos.append("".join(sorted(gp[0] + gm[0])) + "".join(sorted(gp[1] + gm[1])))
homozigoto = [g for g in filhos if g[0] == g[1] and g[2] == g[3]]
p = Fraction(len(homozigoto), len(filhos))
print("espaço amostral:", filhos)
print(f"P(homozigoto) = {p} = {float(p)} -> {classificar(p)}")

# variável aleatória: nº de caras em 3 lançamentos de moeda
omega = ["".join(r) for r in product("kc", repeat=3)]
X = Counter(s.count("k") for s in omega)
print("Ω =", omega)
print("distribuição de X:", {x: str(Fraction(X[x], len(omega))) for x in sorted(X)})
