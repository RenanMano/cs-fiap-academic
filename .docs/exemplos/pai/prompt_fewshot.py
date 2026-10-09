# Monta um prompt few-shot com delimitadores, a partir dos exemplos rotulados do slide
exemplos = [
    ("Amei a experiência. O sanduíche de queijo é ótimo!", "Positivo"),
    ("A comida é gostosa, mas o atendimento é péssimo. Não recomendo.", "Negativo"),
    ("A comida chegou fria.", "Negativo"),
    ("Sempre vou neste restaurante e mais uma vez, estava tudo perfeito", "Positivo"),
]

def montar_prompt(avaliacao):
    linhas = [
        "Classifique o sentimento da avaliação delimitada por <avaliacao>.",
        "Responda apenas com uma palavra: Positivo ou Negativo.",
        "",
        "Exemplos:",
    ]
    for texto, rotulo in exemplos:
        linhas.append(f"<avaliacao>{texto}</avaliacao> -> {rotulo}")
    linhas += ["", f"<avaliacao>{avaliacao}</avaliacao> ->"]
    return "\n".join(linhas)

print(montar_prompt("O garçom foi atencioso e a sobremesa, excelente."))
