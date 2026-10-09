<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Vetores%20e%20Matrizes&amp;fontSize=40&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=PENSAMENTO%20COMPUTACIONAL%20E%20AUTOMA%C3%87%C3%83O%20COM%20PYTHON%20%E2%80%94%20AULA%2007%20%E2%80%94%2026%2F04%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Strings, Vetores (Listas) e Matrizes" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=vetor%5B0%5D%20%C3%A9%20a%20primeira%20posi%C3%A7%C3%A3o;for%20i%20in%20range%28len%28lista%29%29;matriz%5Blinha%5D%5Bcoluna%5D;Jogo%20da%20velha%3A%20matriz%203%C3%973" alt="vetor[0] é a primeira posição. for i in range(len(lista)). matriz[linha][coluna]. Jogo da velha: matriz 3×3." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-PCP-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: PCP" />
  <img src="https://img.shields.io/badge/Aula-07-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 07" />
  <img src="https://img.shields.io/badge/Data-26--04--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 26-04-2026" />
  <img src="https://img.shields.io/badge/Linguagem-Python-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=python&amp;logoColor=white" alt="Linguagem: Python" />
  <img src="https://img.shields.io/badge/Estruturas-Listas%20e%20matrizes-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Estruturas: Listas e matrizes" />
  <img src="https://img.shields.io/badge/Pr%C3%A1tica-8%20exerc%C3%ADcios-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Prática: 8 exercícios" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Pensamento Computacional e Automação com Python](../README.md) |
| Aula | 07 — 26/04/2026 |
| Título | Strings, Vetores (Listas) e Matrizes |
| Tema central | Variáveis compostas, vetores (arrays) e sua implementação com listas em Python, índices, percurso com for indexado e for each, combinações em duplas com laços aninhados, matrizes (aplicações, jogo da velha, matriz 4×5) e oito exercícios. |
| Tecnologias e ferramentas | Python 3 |
| Docente (conforme material) | Prof. Alexandre Russi Junior |
| Natureza do conteúdo | Aula prática com atividades e exercícios |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`PCP - Aula 05 - Strings, arrays e matrizes.pdf`](PCP%20-%20Aula%2005%20-%20Strings%2C%20arrays%20e%20matrizes.pdf) | Slides (22 páginas): motivação das variáveis compostas, vetores, percurso com for, atividade de duplas, matrizes (motivação e aplicações), jogo da velha, matriz 4×5, atividade de preenchimento e oito exercícios. |

> [!NOTE]
> **Limitações da documentação.** Os slides trazem aviso de direitos autorais; o conteúdo é explicado com redação própria. O código aparece em imagens, lidas visualmente. Alguns textos dos slides descrevem vetores como em Java (tamanho fixo, atributo length), enquanto os códigos usam listas Python; a diferença é comentada. Os exercícios não têm gabarito: as soluções são propostas, com entradas fixas e semente aleatória fixa.

<br />

<h2 id="visao-geral">Visão geral</h2>

Até aqui, cada variável guardava **um** valor. Para calcular a média de uma turma e depois comparar **cada** nota com ela, é preciso guardar todas as notas. Entram as **variáveis compostas**:

- **vetores** (arrays), com uma dimensão, um índice;
- **matrizes**, com duas dimensões, linha e coluna.

Em Python, ambos são representados por **listas** (e listas de listas).

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Criar, preencher e percorrer listas com índice e com *for each*.
- Gerar combinações com laços aninhados.
- Criar e percorrer matrizes como listas de listas.
- Resolver problemas clássicos: média e comparação, inversão e soma de matrizes.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 05](../aula05-04-04-26/README.md): laços `for` e `while`, laços aninhados.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Vetores

Um **vetor** é uma estrutura **indexada**: cada elemento é acessado por um índice que começa em **0**. Num vetor de 10 posições, `v[0]` é o primeiro e `v[9]`, o último.

| Índice | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Valor | 10 | 1999 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

> [!NOTE]
> **Vetor clássico × lista Python.** Parte do texto dos slides descreve o vetor "clássico" de linguagens como Java e C: tamanho **fixo**, um único tipo e capacidade dada pelo atributo `length`. Os códigos dos slides, porém, usam **listas Python**, que **crescem** com `append`, aceitam tipos diferentes e têm o tamanho dado por `len(lista)`. Além disso, o código do slide (lista vazia com dois `append`) gera uma lista de **2** posições, e não as 10 do desenho. Para reproduzir um vetor de tamanho fixo, use `[0] * 10`.

**Percurso:**

<!-- norun -->
```python
for i in range(len(numeros)):        # FOR indexado: posição e valor
    print(f"Pos: {i} -- Valor: {numeros[i]}")

for num in numeros:                  # FOR EACH: percorre diretamente os valores
    print(f"Valor: {num}")
```

### 2. Matrizes

Estruturas com **linhas e colunas**: planilhas (células), telas (pixels), tabuleiros (casas) e tabelas de banco de dados (registros). Outras aplicações citadas são visão computacional (imagens, rotação), criptografia (chaves) e o **jogo da velha**.

Em Python, uma matriz $m \times n$ é uma lista com $m$ listas de $n$ elementos. O acesso é `matriz[linha][coluna]`.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart LR
    M["matriz 4×5"] --> L0["linha 0: [1, 2, 3, 4, 5]"]
    M --> L1["linha 1: [6, 7, 8, 9, 10]"]
    M --> L2["linha 2: [11, ..., 15]"]
    M --> L3["linha 3: [16, ..., 20]"]
```

*Figura 1 — Uma matriz como lista de listas (Atividade 2): o elemento `[i][j]` vale `5·i + j + 1`.*

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — listas, duplas, matriz 4×5 e tabuleiro

```python
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
```

Saída esperada:

```text
[10, 1999] tamanho: 2
após mais um append: 3
[10, 1999, 0, 0, 0, 0, 0, 0, 0, 0]
6 duplas: [('Ana', 'Bia'), ('Ana', 'Caio'), ('Ana', 'Davi'), ('Bia', 'Caio'), ('Bia', 'Davi'), ('Caio', 'Davi')]
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
X| | 
 |O| 
 | |X
```

Na Atividade 1, com 4 nomes, há $\binom{4}{2} = 6$ duplas. O laço interno começa em `i + 1` para não repetir pares nem formar dupla de alguém consigo mesmo.

### Exemplo aplicado — exercícios 1 a 8

```python
import random

random.seed(5)
print("1)", [round(random.uniform(0, 10), 2) for _ in range(4)])

notas = [7.0, 5.5, 8.0, 7.0, 9.5, 4.0]
media = sum(notas) / len(notas)
print(f"2) média {media:.2f} | iguais {sum(n == media for n in notas)} | acima {sum(n > media for n in notas)} | abaixo {sum(n < media for n in notas)}")

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for mes, d in list(zip(meses, dias))[:3]:
    print(f"3) O mês de {mes} tem {d} dias ao todo.")

print("4) soma:", sum([3, 8, -1, 10]))

nomes = ["Ana", "Bia", "Caio"]                  # 5) lidos até um Enter vazio
print("5)", nomes[::-1])

v = list("python")                              # 6) inversão por trocas
for i in range(len(v) // 2):
    v[i], v[-1 - i] = v[-1 - i], v[i]
print("6)", "".join(v))

m = [[random.randint(0, 9) for _ in range(4)] for _ in range(3)]
print("7)", m)

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
print("8) A + B =", C)
```

Saída esperada:

```text
1) [6.23, 7.42, 7.95, 9.42]
2) média 6.83 | iguais 0 | acima 4 | abaixo 2
3) O mês de Jan tem 31 dias ao todo.
3) O mês de Fev tem 28 dias ao todo.
3) O mês de Mar tem 31 dias ao todo.
4) soma: 20
5) ['Caio', 'Bia', 'Ana']
6) nohtyp
7) [[8, 0, 7, 3], [0, 2, 1, 5], [7, 3, 6, 8]]
8) A + B = [[6, 8], [10, 12]]
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

As soluções acima são **propostas para estudo** (o material não traz gabarito). Versão interativa do exercício 5, em que a lista termina com um Enter vazio:

<details>
<summary><strong>Solução proposta para estudo</strong> — leitura até Enter vazio</summary>

<!-- norun -->
```python
nomes = []
while True:
    nome = input("Nome (Enter para terminar): ")
    if nome == "":
        break
    nomes.append(nome)
for nome in reversed(nomes):
    print(nome)
```

</details>

**Comentários:**

- **Exercício 2:** a média só pode ser comparada depois que todas as notas estão guardadas. É exatamente a motivação das variáveis compostas.
- **Exercício 6:** basta percorrer até a metade (`len(v) // 2`), trocando `v[i]` com `v[-1 - i]`. Ir até o fim desfaria as trocas.
- **Exercício 8:** a soma de matrizes exige **mesmas dimensões** e é feita elemento a elemento.

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Imagens:** uma foto em tons de cinza é uma matriz de pixels; filtros e rotações são operações matriciais.
- **Dados tabulares:** listas de registros e matrizes são a base de planilhas e do pandas.
- **Jogos:** tabuleiros (velha, xadrez, batalha naval) são matrizes.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| `[[0] * 3] * 3` para criar matriz | `[[0] * 3 for _ in range(3)]` | O primeiro repete a **mesma** lista 3 vezes; alterar uma linha altera todas |
| Acessar `v[len(v)]` | O último índice é `len(v) - 1` (ou `v[-1]`) | Evita `IndexError` |
| Inverter trocando até o fim | Trocar só até a metade | Senão o vetor volta ao original |
| Tratar lista Python como vetor de tamanho fixo | Usar `append` ou `[valor] * n` conforme o caso | São estruturas diferentes |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Vetor: estrutura indexada a partir de 0; em Python, `list`.
- `len(lista)`, `append`, `lista[i]`, `lista[-1]`, `lista[::-1]`.
- Matriz: lista de listas; `m[linha][coluna]`.
- Laços aninhados percorrem matrizes e geram combinações.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Em `v = [4, 8, 15, 16]`, quanto valem `v[1]` e `v[-1]`?
2. Como acessar o elemento da 3ª linha e 2ª coluna de `m`?
3. Quantas duplas podem ser formadas com 5 pessoas?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. `8` e `16`.
2. `m[2][1]`, porque os índices começam em 0.
3. $\binom{5}{2} = 10$.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [Python — listas](https://docs.python.org/pt-br/3/tutorial/datastructures.html#more-on-lists)
- Material da pasta: [slides](PCP%20-%20Aula%2005%20-%20Strings%2C%20arrays%20e%20matrizes.pdf)

<br />

<p align="center"><a href="../aula06-24-04-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula08-03-08-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
