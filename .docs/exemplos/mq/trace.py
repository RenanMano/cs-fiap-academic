def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


def merge_sort(lista, nivel=0):
    recuo = "  " * nivel
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda, direita = lista[:meio], lista[meio:]
    print(f"{recuo}dividir {lista} -> {esquerda} {direita}")
    esquerda = merge_sort(esquerda, nivel + 1)
    direita = merge_sort(direita, nivel + 1)
    resultado = merge(esquerda, direita)
    print(f"{recuo}merge {esquerda} + {direita} -> {resultado}")
    return resultado


def quick_sort(lista, nivel=0):
    recuo = "  " * nivel
    if len(lista) <= 1:
        return lista
    pivo = lista[-1]
    menores = [e for e in lista if e < pivo]
    iguais = [e for e in lista if e == pivo]
    maiores = [e for e in lista if e > pivo]
    print(f"{recuo}{lista}: pivô={pivo} menores={menores} iguais={iguais} maiores={maiores}")
    return quick_sort(menores, nivel + 1) + iguais + quick_sort(maiores, nivel + 1)
