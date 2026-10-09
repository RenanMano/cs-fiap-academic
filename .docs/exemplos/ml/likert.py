from collections import Counter

escala = ["Discordo totalmente", "Discordo", "Neutro", "Concordo", "Concordo totalmente"]
# respostas ilustrativas de 12 participantes (códigos 1 a 5)
respostas = [4, 5, 3, 4, 4, 2, 5, 4, 3, 1, 4, 5]

contagem = Counter(respostas)
for codigo, rotulo in enumerate(escala, start=1):
    fi = contagem.get(codigo, 0)
    print(f"{codigo} {rotulo:<20} {fi:>2} {'#' * fi}")
favoraveis = contagem[4] + contagem[5]
print(f"Concordância (4 ou 5): {favoraveis}/{len(respostas)} = {favoraveis / len(respostas):.0%}")
