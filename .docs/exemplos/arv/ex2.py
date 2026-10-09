def precedencia(op):
    return 2 if op in "*/" else 1 if op in "+-" else 0

def para_posfixa(tokens):
    saida, pilha = [], []
    for t in tokens:
        if t == "(":
            pilha.append(t)
        elif t == ")":
            while pilha[-1] != "(":
                saida.append(pilha.pop())
            pilha.pop()
        elif t in "+-*/":
            while pilha and pilha[-1] != "(" and precedencia(pilha[-1]) >= precedencia(t):
                saida.append(pilha.pop())
            pilha.append(t)
        else:
            saida.append(t)
        print(f"{t:>2} | saída: {' '.join(saida):<14} | pilha: {''.join(pilha)}")
    while pilha:
        saida.append(pilha.pop())
    return saida

print("pós-fixa:", " ".join(para_posfixa(["2", "*", "(", "3", "+", "4", ")", "-", "5"])))
