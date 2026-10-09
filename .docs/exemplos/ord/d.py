def bubble_sort(lista):
    lista = lista[:]                      # trabalha em uma cópia
    comparacoes = trocas = 0
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    return lista, comparacoes, trocas


def selection_sort(lista):
    lista = lista[:]
    comparacoes = trocas = 0
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:                    # conta só trocas efetivas
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1
    return lista, comparacoes, trocas


def insertion_sort(lista):
    lista = lista[:]
    comparacoes = movimentos = 0
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if lista[j] > atual:
                lista[j + 1] = lista[j]   # deslocamento
                movimentos += 1
                j -= 1
            else:
                break
        lista[j + 1] = atual
    return lista, comparacoes, movimentos

casos = {
    "ordenada": [1, 2, 3, 4, 5, 6, 7, 8],
    "invertida": [8, 7, 6, 5, 4, 3, 2, 1],
    "quase_ordenada": [1, 2, 3, 5, 4, 6, 7, 8],
}
print(f"{'caso':15} {'bubble':>9} {'selection':>11} {'insertion':>11}")
for nome, dados in casos.items():
    linha = [f"{c}/{t}" for _, c, t in (f(dados) for f in (bubble_sort, selection_sort, insertion_sort))]
    print(f"{nome:15} {linha[0]:>9} {linha[1]:>11} {linha[2]:>11}")
