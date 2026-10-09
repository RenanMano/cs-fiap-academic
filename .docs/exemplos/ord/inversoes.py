# Por que Bubble (trocas) e Insertion (deslocamentos) empatam: ambos igualam o número de inversões
def inversoes(lista):
    return sum(1 for i in range(len(lista)) for j in range(i + 1, len(lista)) if lista[i] > lista[j])

def bubble(lista):
    lista, comp, trocas = lista[:], 0, 0
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            comp += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    return comp, trocas

def insertion(lista):
    lista, comp, desloc = lista[:], 0, 0
    for i in range(1, len(lista)):
        atual, j = lista[i], i - 1
        while j >= 0:
            comp += 1
            if lista[j] > atual:
                lista[j + 1] = lista[j]
                desloc += 1
                j -= 1
            else:
                break
        lista[j + 1] = atual
    return comp, desloc

def selection(lista):
    lista, comp, trocas = lista[:], 0, 0
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            comp += 1
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1
    return comp, trocas

dados = [7, 3, 9, 1, 5, 3, 8, 2]
print("inversões:", inversoes(dados))
for nome, f in (("Bubble", bubble), ("Insertion", insertion), ("Selection", selection)):
    c, m = f(dados)
    print(f"{nome:9} comparações={c:2}  movimentações={m:2}")
