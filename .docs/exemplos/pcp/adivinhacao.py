palavras = {"frutas": ["banana", "morango", "abacaxi", "melancia"],
            "cores": ["azul", "verde", "amarelo", "vermelho"]}

def jogar(ler=input, tentativas=6):
    categorias = list(palavras)
    print("Escolha uma categoria:")
    for n, nome in enumerate(categorias, start=1):
        print(f"{n} - {nome.capitalize()}")
    lista = palavras[categorias[int(ler("Digite a opção: ")) - 1]]
    print(f"A categoria possui {len(lista)} palavras.")
    palavra = lista[int(ler("Escolha a posição da palavra: ")) - 1]   # posição a partir de 1

    descobertas = set()
    print(f"Você terá {tentativas} tentativas para descobrir a palavra.")
    while tentativas > 0 and not set(palavra) <= descobertas:
        print("Palavra:", " ".join(c if c in descobertas else "_" for c in palavra))
        letra = ler("Digite uma letra: ").strip().lower()
        if letra in palavra:
            descobertas.add(letra)
        else:
            tentativas -= 1
            print(f"Você errou! Tentativas restantes: {tentativas}")
    if set(palavra) <= descobertas:
        print("Parabéns! Você descobriu a palavra:", palavra)
    else:
        print(f"Suas tentativas terminaram.\nA palavra era: {palavra}")

def simular(respostas):
    """Substitui input(): devolve as respostas em ordem e as exibe como se fossem digitadas."""
    fila = iter(respostas)
    def ler(msg):
        valor = next(fila)
        print(msg + valor)
        return valor
    return ler

jogar(ler=simular(["1", "1", "a", "x", "n", "b"]))      # frutas, posição 1 (banana)
