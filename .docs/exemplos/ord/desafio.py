from contagem import bubble_sort, selection_sort, insertion_sort

casos = {
    "ordenada": [1, 2, 3, 4, 5, 6, 7, 8],
    "invertida": [8, 7, 6, 5, 4, 3, 2, 1],
    "quase_ordenada": [1, 2, 3, 5, 4, 6, 7, 8],
}
print(f"{'caso':15} {'bubble':>9} {'selection':>11} {'insertion':>11}   (comparações/trocas)")
for nome, dados in casos.items():
    linha = []
    for f in (bubble_sort, selection_sort, insertion_sort):
        _, c, t = f(dados)
        linha.append(f"{c}/{t}")
    print(f"{nome:15} {linha[0]:>9} {linha[1]:>11} {linha[2]:>11}")
