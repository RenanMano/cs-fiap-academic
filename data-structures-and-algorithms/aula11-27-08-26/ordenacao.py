numeros = [
    583, 127, 941, 36, 715, 264, 809, 452, 98, 671,
    320, 887, 54, 763, 219, 496, 832, 145, 608, 27,
    974, 381, 562, 193, 746, 415, 68, 901, 337, 624,
    157, 789, 243, 518, 856, 104, 693, 470, 31, 925,
    276, 641, 182, 734, 509, 83, 968, 354, 597, 211,
    778, 439, 116, 685, 302, 847, 49, 531, 906, 168,
    723, 395, 612, 257, 880, 73, 549, 936, 314, 661,
    202, 795, 428, 95, 570, 818, 346, 629, 14, 983,
    491, 136, 752, 289, 604, 871, 43, 527, 910, 175,
    699, 367, 824, 231, 558, 77, 945, 410, 653, 190,
    786, 325, 514, 862, 109, 678, 453, 22, 997, 371,
    590, 248, 731, 406, 85, 919, 163, 644, 297, 805,
    478, 52, 960, 333, 616, 207, 774, 441, 121, 688,
    359, 842, 66, 535, 928, 184, 707, 271, 623, 399,
    811, 101, 576, 954, 340, 665, 225, 793, 464, 39,
    879, 312, 548, 917, 154, 720, 286, 635, 470, 81,
    999, 363, 601, 214, 767, 432, 118, 684, 295, 850,
    57, 522, 932, 171, 710, 388, 647, 239, 804, 475,
    92, 971, 328, 559, 201, 748, 417, 133, 692, 263,
    836, 45, 615, 903, 178, 725, 350, 581, 110, 660
]
#Para comparar os três algoritmos de forma justa, não se deve usar apenas a variável trocas, 
# porque cada algoritmo realiza operações diferentes.
#O ideal é medir pelo menos duas coisas separadamente:
#Comparações — quantas vezes o algoritmo compara dois valores.
#Movimentações/trocas — quantas vezes os elementos são efetivamente movimentados.

def bubble_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        for j in range(n - 1 - i):
            comparacoes += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return lista, comparacoes, trocas

def selection_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            comparacoes += 1

            if lista[j] < lista[menor]:
                menor = j

        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1

    return lista, comparacoes, trocas

def insertion_sort(lista):
    comparacoes = 0
    deslocamentos = 0

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if lista[j] > atual:
                lista[j + 1] = lista[j]
                j -= 1
                deslocamentos += 1
            else:
                break

        lista[j + 1] = atual

    return lista, comparacoes, deslocamentos

bubble, comp_b, trocas_b = bubble_sort(numeros[:])
insertion, comp_i, desloc_i = insertion_sort(numeros[:])
selection, comp_s, trocas_s = selection_sort(numeros[:])

print("                 Comparações    Movimentações")
print("Bubble Sort:     ", comp_b, "          ", trocas_b)
print("Insertion Sort:  ", comp_i, "          ", desloc_i)
print("Selection Sort:  ", comp_s, "          ", trocas_s)
