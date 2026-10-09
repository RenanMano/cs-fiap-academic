# Solução proposta para estudo — Central de Triagem Orbital, Versão A (Bubble Sort)
containers_A = [
    482, 173, 905, 241, 667, 318, 754, 126, 590, 433, 812, 205, 691, 347, 978, 154, 526, 739, 284, 861,
    615, 92, 447, 830, 271, 704, 358, 999, 116, 563, 790, 225, 648, 401, 876, 139, 512, 733, 296, 944,
    187, 620, 455, 808, 332, 571, 14, 684, 253, 917, 365, 742, 198, 536, 889, 307, 651, 420, 773, 105,
    598, 246, 934, 381, 719, 160, 547, 825, 293, 672, 438, 981, 121, 504, 756, 339, 690, 214, 867, 475,
    928, 146, 583, 261, 714, 396, 845, 72, 631, 287, 960, 518, 352, 799, 183, 606, 449, 874, 235, 697,
    323, 910, 167, 552, 781, 409, 995, 128, 644, 274, 835, 491, 759, 203, 576, 341, 888, 64, 622, 457,
    936, 312, 705, 149, 539, 820, 266, 681, 427, 973, 111, 594, 748, 384, 862, 229, 517, 301, 793, 176,
    655, 470, 921, 137, 568, 245, 730, 414, 856, 98, 609, 286, 947, 361, 712, 194, 525, 804, 257, 678,
    443, 986, 119, 591, 764, 335, 841, 208, 549, 392, 913, 155, 632, 278, 725, 461, 870, 83, 603, 319,
    958, 171, 557, 240, 699, 406, 823, 132, 586, 270, 932, 375, 716, 201, 531, 788, 349, 663, 454, 902,
]


def analisar_carga(lista):                       # Missão 1: sem min(), max(), sort() ou sorted()
    menor = maior = lista[0]
    quantidade = 0
    for codigo in lista:
        quantidade += 1
        if codigo < menor:
            menor = codigo
        if codigo > maior:
            maior = codigo
    return quantidade, menor, maior


def busca_linear(lista, codigo):                 # Missão 2: 1 comparação por elemento verificado
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == codigo:
            return i, comparacoes
    return -1, comparacoes


def ordenar(lista):                              # Missão 3: Bubble Sort
    comparacoes = movimentacoes = 0
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                movimentacoes += 1                # cada troca efetiva
    return lista, comparacoes, movimentacoes


def busca_binaria(lista, codigo):                # Missão 4 (somente sobre a lista ordenada)
    # Critério: 1 comparação por elemento do meio examinado (o teste == e o teste <
    # sobre o mesmo lista[meio] contam juntos como uma única consulta).
    inicio, fim, comparacoes = 0, len(lista) - 1, 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio] == codigo:
            return meio, comparacoes
        if lista[meio] < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes


quantidade, menor, maior = analisar_carga(containers_A)
ordenada, comparacoes, movimentacoes = ordenar(containers_A[:])   # preserva o vetor original

print("Teste inexistente:", busca_linear(containers_A, 500), busca_binaria(ordenada, 500))

codigo = 733                                      # Missão 5: o mesmo código nas duas buscas
pos_l, comp_l = busca_linear(containers_A, codigo)
pos_b, comp_b = busca_binaria(ordenada, codigo)
print("========== CENTRAL DE TRIAGEM ==========")
print("Quantidade de contêineres:", quantidade)
print("Menor código:", menor)
print("Maior código:", maior)
print("---------- ORDENAÇÃO ----------")
print("Algoritmo: Bubble Sort")
print("Comparações:", comparacoes)
print("Movimentações:", movimentacoes)
print("---------- BUSCAS ----------")
print("Código procurado:", codigo)
print(f"Busca Linear - Posição: {pos_l} | Comparações: {comp_l}")
print(f"Busca Binária - Posição: {pos_b} | Comparações: {comp_b}")
print("========================================")
