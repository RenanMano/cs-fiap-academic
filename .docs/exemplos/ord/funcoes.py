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

