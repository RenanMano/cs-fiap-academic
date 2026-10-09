vetor_inteiros = []
vetor_inteiros.append(10)
vetor_inteiros.append(1999)
print(vetor_inteiros, "tamanho:", len(vetor_inteiros))      # a lista cresce conforme append
vetor_inteiros.append(42)
print("após mais um append:", len(vetor_inteiros))

fixo = [0] * 10                                             # "vetor" de 10 posições, como no desenho do slide
fixo[0], fixo[1] = 10, 1999
print(fixo)

nomes = ["Ana", "Bia", "Caio", "Davi"]                      # Atividade 1: duplas
duplas = [(nomes[i], nomes[j]) for i in range(len(nomes)) for j in range(i + 1, len(nomes))]
print(len(duplas), "duplas:", duplas)

matriz = [[linha * 5 + coluna + 1 for coluna in range(5)] for linha in range(4)]   # Atividade 2
for linha in matriz:
    print(" ".join(f"{v:>2}" for v in linha))

tabuleiro = [[" "] * 3 for _ in range(3)]                   # jogo da velha
tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2] = "X", "O", "X"
print("\n".join("|".join(l) for l in tabuleiro))
