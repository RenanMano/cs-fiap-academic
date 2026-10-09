casos = {
    "ordenada": [1, 2, 3, 4, 5, 6, 7, 8],
    "invertida": [8, 7, 6, 5, 4, 3, 2, 1],
    "quase_ordenada": [1, 2, 3, 5, 4, 6, 7, 8],
}
print(f"{'caso':15} {'bubble':>9} {'selection':>11} {'insertion':>11}")
for nome, dados in casos.items():
    linha = [f"{c}/{t}" for _, c, t in (f(dados) for f in (bubble_sort, selection_sort, insertion_sort))]
    print(f"{nome:15} {linha[0]:>9} {linha[1]:>11} {linha[2]:>11}")
