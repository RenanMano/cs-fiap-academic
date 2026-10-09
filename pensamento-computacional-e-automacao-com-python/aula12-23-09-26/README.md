<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Jogo%20de%20Adivinha%C3%A7%C3%A3o&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=PENSAMENTO%20COMPUTACIONAL%20E%20AUTOMA%C3%87%C3%83O%20COM%20PYTHON%20%E2%80%94%20AULA%2012%20%E2%80%94%2023%2F09%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Exercício Extra: Jogo de Adivinhação de Palavras" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=palavras%20%3D%20%7B%27frutas%27%3A%20%5B...%5D%2C%20%27cores%27%3A%20%5B...%5D%7D;Palavra%3A%20_%20a%20_%20a%20_%20a;6%20tentativas;Parab%C3%A9ns%21%20Voc%C3%AA%20descobriu%20a%20palavra" alt="palavras = {'frutas': [...], 'cores': [...]}. Palavra: _ a _ a _ a. 6 tentativas. Parabéns! Você descobriu a palavra." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-PCP-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: PCP" />
  <img src="https://img.shields.io/badge/Aula-12-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 12" />
  <img src="https://img.shields.io/badge/Data-23--09--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 23-09-2026" />
  <img src="https://img.shields.io/badge/Linguagem-Python-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=python&amp;logoColor=white" alt="Linguagem: Python" />
  <img src="https://img.shields.io/badge/Integra-dict%20%C2%B7%20list%20%C2%B7%20while-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Integra: dict · list · while" />
  <img src="https://img.shields.io/badge/Tipo-Desafio%20pr%C3%A1tico-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Tipo: Desafio prático" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Pensamento Computacional e Automação com Python](../README.md) |
| Aula | 12 — 23/09/2026 |
| Título | Exercício Extra: Jogo de Adivinhação de Palavras |
| Tema central | Exercício extra integrador: um jogo de adivinhação de palavras (estilo forca) com categorias em dicionário, listas de palavras, escolha por posição, máscara de letras, laço de tentativas e mensagens de vitória ou derrota. |
| Tecnologias e ferramentas | Python 3 |
| Docente (conforme material) | Prof. Alexandre Russi Junior |
| Natureza do conteúdo | Exercício extra (enunciado) |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`PCP - Extra - Jogo da Adivinhação.pdf`](PCP%20-%20Extra%20-%20Jogo%20da%20Adivinha%C3%A7%C3%A3o.pdf) | Enunciado do exercício extra (5 páginas): regras do jogo, dicionário de categorias, escolha de categoria e posição, máscara da palavra, seis tentativas e mensagens de vitória e derrota. |

> [!NOTE]
> **Limitações da documentação.** O PDF (5 páginas) contém apenas o enunciado, em imagens, lido visualmente; não há código nem gabarito. A solução apresentada é proposta e foi executada com entradas simuladas. Uma inconsistência do exemplo do enunciado é comentada.

<br />

<h2 id="visao-geral">Visão geral</h2>

O exercício extra integra quase tudo do curso até aqui: **dicionários** (categorias), **listas** (palavras), **strings** (máscara de letras), **laços** (rodadas) e **condicionais** (acerto ou erro). O jogo funciona como a forca: o usuário descobre uma palavra escolhendo letras, com **6 tentativas**.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart TD
    A["Escolher categoria<br/>(chave do dicionário)"] --> B["Informar nº de palavras<br/>e escolher a posição"]
    B --> C["Mostrar máscara _ _ _"]
    C --> D{"Letras faltando<br/>e tentativas > 0?"}
    D -->|"sim"| E["Ler letra"]
    E --> F{"Letra na palavra?"}
    F -->|"sim"| G["Revelar todas as ocorrências"]
    F -->|"não"| H["Tentativas − 1<br/>'Você errou!'"]
    G --> D
    H --> D
    D -->|"não"| I{"Descobriu tudo?"}
    I -->|"sim"| V["Parabéns! Você descobriu a palavra"]
    I -->|"não"| P["Suas tentativas terminaram.<br/>A palavra era: ..."]
```

*Figura 1 — Fluxo do jogo segundo o enunciado.*

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Organizar dados em um dicionário de listas.
- Controlar um jogo com laço, contador de tentativas e condição de vitória.
- Revelar todas as ocorrências de uma letra numa string.
- Estruturar o programa em função e torná-lo testável.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 09](../aula09-10-08-26/README.md) (dicionários), [aula 07](../aula07-26-04-26/README.md) (listas) e [aula 05](../aula05-04-04-26/README.md) (laços).

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### Requisitos do enunciado

1. Palavras num **dicionário**, em que a chave é a categoria e o valor, uma lista de palavras. Exemplo: `{"frutas": ["banana", "morango", "abacaxi", "melancia"], "cores": ["azul", "verde", "amarelo", "vermelho"]}`.
2. O usuário escolhe a **categoria**; o programa informa **quantas palavras** ela tem e o usuário escolhe a **posição** da palavra.
3. A palavra **não é exibida**: aparece só uma sequência de `_`, uma por letra.
4. Antes das tentativas: "Você terá 6 tentativas para descobrir a palavra."
5. A cada rodada: mostrar a palavra com as letras descobertas, as tentativas restantes, pedir uma letra e verificar se ela está na palavra.
6. Acerto: revelar **todas** as ocorrências (com "banana" e a letra `a`: `_ a _ a _ a`). Erro: descontar uma tentativa ("Você errou! Tentativas restantes: 5").
7. O jogo continua enquanto houver letras a descobrir e tentativas disponíveis. As mensagens finais são "Parabéns! Você descobriu a palavra: banana" ou "Suas 6 tentativas terminaram. A palavra era: banana".

### Ideia central: conjunto de letras descobertas

Guardar as letras certas num **conjunto** (`set`) facilita tudo:

- a máscara é `" ".join(c if c in descobertas else "_" for c in palavra)`;
- a vitória acontece quando `set(palavra) <= descobertas`, ou seja, todas as letras da palavra já foram descobertas.

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo — solução proposta, com partida simulada

Para que a execução seja reproduzível, `input` é substituído por uma função que devolve respostas pré-definidas (categoria 1, posição 1 = "banana"):

```python
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
```

Saída esperada:

```text
Escolha uma categoria:
1 - Frutas
2 - Cores
Digite a opção: 1
A categoria possui 4 palavras.
Escolha a posição da palavra: 1
Você terá 6 tentativas para descobrir a palavra.
Palavra: _ _ _ _ _ _
Digite uma letra: a
Palavra: _ a _ a _ a
Digite uma letra: x
Você errou! Tentativas restantes: 5
Palavra: _ a _ a _ a
Digite uma letra: n
Palavra: _ a n a n a
Digite uma letra: b
Parabéns! Você descobriu a palavra: banana
```

Para jogar de verdade, basta chamar `jogar()`, que usa `input` por padrão.

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

A solução acima é **proposta para estudo**: o enunciado não traz código.

> [!NOTE]
> **Inconsistências do enunciado.** O texto diz "para uma palavra com **sete** letras", mas o exemplo mostra **seis** traços (`_ _ _ _ _ _`). A mensagem final de derrota aparece como "Suas **6** tentativas terminaram", que só é exata se o número de tentativas não mudar. A solução usa "Suas tentativas terminaram". Além disso, o enunciado não diz se a posição começa em 0 ou em 1. A solução adota **1**, que é mais natural para o usuário, e converte com `- 1`.

**Melhorias propostas para estudo:**

1. Validar a categoria e a posição com laços (entradas fora do intervalo).
2. Não descontar tentativa ao repetir uma letra já tentada.
3. Aceitar apenas **uma** letra por jogada (`len(letra) == 1 and letra.isalpha()`).
4. Sortear a palavra com `random.choice(lista)`, em vez de pedir a posição, para que o próprio jogador não saiba qual é.

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Lógica de jogos e de estado:** controlar estado (tentativas, letras), regras e condição de término é a base de jogos e sistemas interativos.
- **Testabilidade:** injetar a função de entrada (`ler=...`) é uma técnica de testes automatizados, que substitui dependências externas por versões controladas.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Mostrar a palavra escolhida | Exibir só a máscara | Requisito do enunciado |
| Revelar só a primeira ocorrência | Revelar todas (`c in descobertas`) | "banana" tem três letras `a` |
| Comparar maiúsculas e minúsculas diretamente | `.lower()` na letra digitada | "A" e "a" são a mesma letra no jogo |
| `input` espalhado pelo código | Uma função de leitura injetável | Permite testar sem digitar |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Dicionário de listas para as categorias; escolha da posição na lista.
- Máscara com `_`, revelando todas as ocorrências.
- O laço continua enquanto houver letras faltando e tentativas.
- Vitória: `set(palavra) <= descobertas`.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Como obter as categorias do dicionário `palavras`?
2. Qual a máscara de "morango" após acertar `o`?
3. Por que usar um `set` para as letras descobertas?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. `list(palavras)` ou `palavras.keys()`.
2. `_ o _ _ _ _ o`.
3. Porque o teste de pertinência é rápido, as letras não se repetem e a comparação `set(palavra) <= descobertas` resolve a condição de vitória.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [Python — conjuntos (`set`)](https://docs.python.org/pt-br/3/tutorial/datastructures.html#sets)
- Material da pasta: [enunciado](PCP%20-%20Extra%20-%20Jogo%20da%20Adivinha%C3%A7%C3%A3o.pdf)

<br />

<p align="center"><a href="../aula11-09-09-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula13-28-09-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
