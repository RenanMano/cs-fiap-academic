from collections import Counter

dados1 = ["Sim"] * 20 + ["Não"] * 45
respostas1 = Counter(dados1)
print(respostas1)

labels = list(respostas1.keys())      # ordem de primeira aparição
values = list(respostas1.values())
print(labels, values)

total = sum(values)
percent_labels = [f"{100 * v / total:.2f}%".replace(".", ",") for v in values]
print(total, percent_labels)
