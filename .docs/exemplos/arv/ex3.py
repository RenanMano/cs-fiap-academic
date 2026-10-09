def calcular_posfixa(posfixa):
    pilha = []
    for t in posfixa:
        if t in "+-*/":
            b = pilha.pop()   # 1º pop: operando DIREITO
            a = pilha.pop()   # 2º pop: operando ESQUERDO
            pilha.append({"+": a + b, "-": a - b, "*": a * b, "/": a / b}[t])
        else:
            pilha.append(float(t))
    return pilha[0]

def altura_cadeia(n):
    # 1 + (2 + (3 + ...)): cada "+" tem outro "+" como filho direito
    return n - 1

print(calcular_posfixa("8 4 - 2 -".split()))   # (8 - 4) - 2
print(calcular_posfixa("8 4 2 - -".split()))   # 8 - (4 - 2)
print("altura da cadeia com 1200 números:", altura_cadeia(1200))
