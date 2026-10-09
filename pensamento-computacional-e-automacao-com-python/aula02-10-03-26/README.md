<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=L%C3%B3gica%20de%20Programa%C3%A7%C3%A3o&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=PENSAMENTO%20COMPUTACIONAL%20E%20AUTOMA%C3%87%C3%83O%20COM%20PYTHON%20%E2%80%94%20AULA%2002%20%E2%80%94%2010%2F03%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Conceitos Básicos de Programação: Lógica, Algoritmos e Tabela Verdade" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=Algoritmo%3A%20sequ%C3%AAncia%20finita%20de%20passos;O%20computador%20faz%20EXATAMENTE%20o%20que%20voc%C3%AA%20diz;P%20%26%26%20Q%3A%20verdadeiro%20s%C3%B3%20se%20ambos%20forem;Teste%20de%20mesa%3A%20execute%20o%20c%C3%B3digo%20no%20papel" alt="Algoritmo: sequência finita de passos. O computador faz EXATAMENTE o que você diz. P && Q: verdadeiro só se ambos forem. Teste de mesa: execute o código no papel." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-PCP-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: PCP" />
  <img src="https://img.shields.io/badge/Aula-02-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 02" />
  <img src="https://img.shields.io/badge/Data-10--03--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 10-03-2026" />
  <img src="https://img.shields.io/badge/Tema-L%C3%B3gica-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Tema: Lógica" />
  <img src="https://img.shields.io/badge/Ferramenta-Fluxograma-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Ferramenta: Fluxograma" />
  <img src="https://img.shields.io/badge/Pr%C3%A1tica-Teste%20de%20mesa-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Prática: Teste de mesa" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Pensamento Computacional e Automação com Python](../README.md) |
| Aula | 02 — 10/03/2026 |
| Título | Conceitos Básicos de Programação: Lógica, Algoritmos e Tabela Verdade |
| Tema central | Áreas de atuação, programação e lógica, algoritmos e refinamento (omelete), algoritmo × linguagem (pseudocódigo), desafios de lógica, fluxogramas, memória RAM e variáveis, tipos de dados, operadores aritméticos, tabela verdade (NÃO, E, OU) e teste de mesa, com exercícios. |
| Tecnologias e ferramentas | Pseudocódigo, fluxogramas (diagrams.net), Python 3 (verificação) |
| Docente (conforme material) | Prof. Alexandre Russi Junior |
| Natureza do conteúdo | Aula teórica com atividades e exercícios |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`PCP - Aula 01 - Conceitos Básicos de Programação.pdf`](PCP%20-%20Aula%2001%20-%20Conceitos%20B%C3%A1sicos%20de%20Programa%C3%A7%C3%A3o.pdf) | Slides (46 páginas): áreas de atuação, programação, lógica, algoritmos (omelete), pseudocódigo, quatro desafios de lógica, atividades de algoritmos e fluxograma, memória e variáveis, tipos de dados, operadores, tabela verdade, teste de mesa e sete exercícios. |

> [!NOTE]
> **Limitações da documentação.** Os slides trazem aviso de direitos autorais; o conteúdo é explicado com redação própria. Os exercícios não têm gabarito no material: as respostas desta página são propostas e foram obtidas executando os algoritmos traduzidos para Python. As planilhas de teste de mesa e tabela verdade citadas (links encurtados) não foram acessadas.

<br />

<h2 id="visao-geral">Visão geral</h2>

Antes de qualquer linguagem vem a **lógica**. A aula define programação como dizer ao computador, passo a passo, como fazer uma tarefa. A máquina faz **exatamente** o que se manda, nem mais nem menos. O conceito central é o **algoritmo**, refinado até o nível de detalhe necessário e representado por pseudocódigo ou fluxograma. A aula termina com as ferramentas para verificar a lógica **sem computador**: a **tabela verdade** e o **teste de mesa**.

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Definir programação, lógica, algoritmo, programa, código-fonte e linguagem de programação.
- Escrever e refinar algoritmos em linguagem natural e em pseudocódigo.
- Representar algoritmos com fluxogramas.
- Relacionar variáveis à memória RAM e reconhecer os tipos de dados.
- Construir tabelas verdade com NÃO, E e OU.
- Executar testes de mesa.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 01](../aula01-08-03-26/README.md): apresentação da disciplina.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Conceitos

| Conceito | Definição (em síntese) |
| :--- | :--- |
| Lógica | Formas de pensamento (dedução, indução, hipótese) para determinar o que é verdadeiro |
| Lógica de programação | Organização coesa de instruções para resolver um problema |
| Algoritmo | Sequência **lógica e finita** de ações que resolve um problema |
| Programa | Conjunto de instruções escrito numa linguagem de programação |
| Código-fonte | O algoritmo escrito numa linguagem; é **compilado** ou **interpretado** para executar |

**Refinamento:** o algoritmo do omelete parte de 8 passos e é detalhado em subpassos (abrir a geladeira, pegar 2 ovos…). Depois ganha **lógica**: "se for para 1 pessoa, separar 2 ovos; senão, 2 ovos por pessoa adicionada".

**Algoritmo → linguagem:** o mesmo algoritmo (pedir o nome, guardar, exibir) é escrito primeiro em passos e depois em pseudocódigo do tipo Portugol (`cadeia nome`, `escreva`, `leia`).

### 2. Fluxograma

| Símbolo | Significado |
| :--- | :--- |
| Terminação (oval) | Início e fim |
| Ação (retângulo) | Processo, ação ou função |
| Decisão (losango) | Pergunta sim/não que divide o fluxo |

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart TD
    I(["Início"]) --> L["Ler valor do produto"]
    L --> D{"valor > 200?"}
    D -->|"sim"| A["desconto = 25%"]
    D -->|"não"| B["desconto = 5%"]
    A --> C["final = valor × (1 − desconto)"]
    B --> C
    C --> E["Exibir final"] --> F(["Fim"])
```

*Figura 1 — Fluxograma da Atividade 2 (solução proposta), com os três símbolos apresentados.*

### 3. Memória, variáveis e tipos

A **RAM** guarda dados de curto prazo durante a execução; o **HD/SSD**, de longo prazo. **Variáveis** são porções da RAM reservadas pelo programa.

| Tipo | Exemplos |
| :--- | :--- |
| Inteiro | 0, 1, 40, 135 |
| Real | 1.36, 3.1415, 2.0 |
| Caractere | A, d, F |
| Palavra (cadeia) | Maria, garrafa |
| Booleano | Verdadeiro / Falso |

Operadores aritméticos: `+ - * /` e `%` (resto da divisão).

### 4. Tabela verdade

| $P$ | $Q$ | $P$ && $Q$ (E) | $P \lvert\lvert Q$ (OU) | !$P$ (NÃO) |
| :---: | :---: | :---: | :---: | :---: |
| V | V | V | V | F |
| V | F | F | V | F |
| F | V | F | V | V |
| F | F | F | F | V |

Exemplos dos slides: login exige LOGIN **E** SENHA corretos; o churrasco acontece se houver jogo do Brasil **OU** sol no domingo.

### 5. Teste de mesa

Executar o algoritmo **à mão**, linha a linha, registrando o valor de cada variável numa tabela. Exemplo dos slides: `a = 3; b = 4; a = b` → `a = 4`, `b = 4`.

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — as atividades 1 a 3 em Python

As atividades pedem algoritmos. Aqui eles estão traduzidos para Python, com entradas fixas para que a saída seja reproduzível:

```python
# Atividade 1 (algoritmos traduzidos para Python; entradas fixas no lugar de input())
nome = "Ana"
print(f"Seja bem vindo, {nome}!")                       # A
print("Soma:", 7 + 5)                                   # B
ano_atual, ano_nascimento = 2026, 2007
print("Idade:", ano_atual - ano_nascimento)             # C
preco = 150.0
print(f"Com 27% de desconto: R$ {preco * (1 - 0.27):.2f}")   # D

# Atividade 2: desconto de 25% acima de R$ 200, senão 5%
for valor in (250.0, 200.0, 80.0):
    desconto = 0.25 if valor > 200 else 0.05
    print(f"R$ {valor:.2f} -> R$ {valor * (1 - desconto):.2f}")

# Atividade 3: somar 5 números usando só 2 variáveis
soma = 0
for numero in (2, 3, 5, 8, 10):
    soma = soma + numero
print("Soma da sequência:", soma)
```

Saída esperada:

```text
Seja bem vindo, Ana!
Soma: 12
Idade: 19
Com 27% de desconto: R$ 109.50
R$ 250.00 -> R$ 187.50
R$ 200.00 -> R$ 190.00
R$ 80.00 -> R$ 76.00
Soma da sequência: 28
```

O slide "Tomem cuidado!" alerta para ler o enunciado com atenção: se o problema diz "números inteiros", uma sequência com 3.14 e 10.8 não é uma entrada válida.

### Exemplo intermediário — testes de mesa (exercícios 1 a 3)

```python
# Exercício 1 (pseudocódigo traduzido para Python)
x = 5
y = 10
z = 5 / y
x = x + 1
y = z
z = y + x
print("Ex. 1:", x, y, z)

# Exercício 2 — "a++" não existe em Python; equivale a a += 1
a = 2
b = 3
c = 2 + a
b = a
a = c
a = a + 1
a += 1
a += 1          # a++
b = c
c = b
b = a % 2
print("Ex. 2:", a, b, c)

# Exercício 3 — Resultado e resultado são variáveis DIFERENTES
x = y = z = 0
Resultado = x + y + z
x, y, z = 10, 25, 30
resultado = x + y + z
print("Ex. 3:", Resultado)
```

Saída esperada:

```text
Ex. 1: 6 0.5 6.5
Ex. 2: 7 1 4
Ex. 3: 0
```

### Exemplo aplicado — tabelas verdade (exercícios 4 a 7)

```python
from itertools import product

V = lambda b: "V" if b else "F"

print("P Q | P and not Q | (P or Q) and (P and Q)")
for P, Q in product([True, False], repeat=2):
    print(V(P), V(Q), "|", V(P and not Q), "            |", V((P or Q) and (P and Q)))

print("\nP Q R | (P or R) or (not Q and R) | exercício 7")
for P, Q, R in product([True, False], repeat=3):
    e6 = (P or R) or (not Q and R)
    e7 = ((P or not Q) and (P and Q)) or e6
    print(V(P), V(Q), V(R), "|", V(e6), "                        |", V(e7))
```

Saída esperada:

```text
P Q | P and not Q | (P or Q) and (P and Q)
V V | F             | V
V F | V             | F
F V | F             | F
F F | F             | F

P Q R | (P or R) or (not Q and R) | exercício 7
V V V | V                         | V
V V F | V                         | V
V F V | V                         | V
V F F | V                         | V
F V V | V                         | V
F V F | F                         | F
F F V | V                         | V
F F F | F                         | F
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

O material não traz gabarito. As respostas abaixo são **soluções propostas para estudo**, conferidas pelas execuções acima.

<details>
<summary><strong>Solução proposta para estudo</strong> — exercícios 1 a 7</summary>

| Exercício | Resposta | Comentário |
| :--- | :--- | :--- |
| 1 | `x = 6`, `y = 0.5`, `z = 6.5` | `z = 5 / y` usa o **y antigo** (10) |
| 2 | `a = 7`, `b = 1`, `c = 4` | `a` passa por 4 → 5 → 6 → 7; `b = 7 % 2 = 1`. `a++` é pseudocódigo (não existe em Python) |
| 3 | `0` | `Resultado` e `resultado` são variáveis **diferentes**: maiúsculas importam |
| 4 | $P \wedge \neg Q$: V só em (V, F) | |
| 5 | $(P \vee Q) \wedge (P \wedge Q)$ = $P \wedge Q$ | Se ambos são V, o OU também é |
| 6 | $(P \vee R) \vee (\neg Q \wedge R)$: F só em (F, V, F) e (F, F, F) | Equivale a $P \vee R$, porque $\neg Q \wedge R$ já implica $R$ |
| 7 | Mesma coluna do exercício 6 | O primeiro bloco só é V quando $P$ é V, caso já coberto por $P \vee R$ |

</details>

<details>
<summary><strong>Solução proposta para estudo</strong> — desafios de lógica</summary>

1. **Desafio matemático:** bola = 6, relógio = 3, ventilador = 3 (3 × 3 − 3 = 6). Logo, relógio × bola − ventilador = 3 × 6 − 3 = **15**, supondo que as figuras da última linha sejam iguais às anteriores.
2. **Avião na fronteira:** sobreviventes não são enterrados.
3. **Casar com a irmã da viúva:** se ele tem uma viúva, ele morreu.
4. **Dia da semana:** "há cinco dias foi um dia antes de sábado" (sexta), então hoje é quarta, e depois de amanhã será **sexta-feira**.

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Áreas citadas:** desenvolvimento *front-end*, *back-end* e *full stack* e análise de banco de dados.
- **Especificação de software:** algoritmos e fluxogramas documentam regras de negócio antes da implementação.
- **Depuração:** o teste de mesa é a base do uso de *debuggers* (executar passo a passo e inspecionar variáveis).
- **Lógica booleana:** regras de acesso (login E senha), filtros de busca e condições de negócio.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Começar pelo código | Escrever o algoritmo e refiná-lo primeiro | Separa o problema da sintaxe |
| Ignorar restrições do enunciado | Ler com atenção ("somente inteiros") | O slide "Tomem cuidado!" |
| Nomes de variáveis parecidos | Nomes distintos e descritivos | `Resultado` × `resultado` (exercício 3) |
| Supor que o computador "entende a intenção" | Lembrar que ele faz exatamente o que foi escrito | Origem de muitos *bugs* |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Algoritmo = passos finitos e ordenados; refina-se até o detalhe necessário.
- Fluxograma: oval (início e fim), retângulo (ação), losango (decisão).
- Variáveis ocupam a RAM; tipos: inteiro, real, caractere, cadeia, booleano.
- E: V só se ambos forem V; OU: F só se ambos forem F; NÃO inverte.
- Teste de mesa: rastrear valores linha a linha.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Qual a diferença entre algoritmo e programa?
2. Qual o valor de `V && !V`?
3. Após `a = 3; b = 4; a = b; b = a`, quanto valem `a` e `b`?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. O algoritmo é a sequência lógica de passos; o programa é esse algoritmo escrito numa linguagem e executável pelo computador.
2. Falso, porque $!V = F$ e $V \wedge F = F$.
3. Ambos valem 4: `a = b` copia o 4, e `b = a` copia de volta o 4. Para trocar valores, seria preciso uma variável auxiliar ou `a, b = b, a`.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [diagrams.net](https://diagrams.net/), ferramenta de fluxogramas indicada nos slides.
- [Pesquisa Código Fonte TV 2025](https://pesquisa.codigofonte.com.br/2025), citada nos slides sobre o mercado.
- Material da pasta: [slides](PCP%20-%20Aula%2001%20-%20Conceitos%20B%C3%A1sicos%20de%20Programa%C3%A7%C3%A3o.pdf)

<br />

<p align="center"><a href="../aula01-08-03-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula03-15-03-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
