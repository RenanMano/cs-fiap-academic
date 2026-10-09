<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=%C3%81rvore%20Bin%C3%A1ria%20de%20Express%C3%B5es&amp;fontSize=30&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=DATA%20STRUCTURES%20AND%20ALGORITHMS%20%E2%80%94%20AULA%2014%20%E2%80%94%2001%2F10%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Árvore Binária de Expressões — Calculadora com Pilhas e Recursão" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=texto%20-%3E%20tokens%20-%3E%20p%C3%B3s-fixa%20-%3E%20%C3%A1rvore;1%C2%BA%20pop%20%3D%20filho%20direito;p%C3%B3s-ordem%20%3D%20nota%C3%A7%C3%A3o%20p%C3%B3s-fixa;%28%2820%20%2F%205%29%20%2B%203%29%20%2A%20%289%20-%20%282%20%2B%201%29%29%20%3D%2042" alt="texto -> tokens -> pós-fixa -> árvore. 1º pop = filho direito. pós-ordem = notação pós-fixa. ((20 / 5) + 3) * (9 - (2 + 1)) = 42." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-DSA-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: DSA" />
  <img src="https://img.shields.io/badge/Aula-14-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 14" />
  <img src="https://img.shields.io/badge/Data-01--10--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 01-10-2026" />
  <img src="https://img.shields.io/badge/Linguagem-Python-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=python&amp;logoColor=white" alt="Linguagem: Python" />
  <img src="https://img.shields.io/badge/Estrutura-%C3%81rvore%20bin%C3%A1ria-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Estrutura: Árvore binária" />
  <img src="https://img.shields.io/badge/T%C3%A9cnicas-Pilha%20e%20recurs%C3%A3o-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Técnicas: Pilha e recursão" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Data Structures and Algorithms](../README.md) |
| Aula | 14 — 01/10/2026 |
| Título | Árvore Binária de Expressões — Calculadora com Pilhas e Recursão |
| Tema central | Calculadora que transforma texto em tokens, converte a expressão infixa em pós-fixa com uma pilha, monta uma árvore binária de expressão e a percorre recursivamente (pré-ordem, em ordem e pós-ordem) para reconstruir e calcular o resultado. |
| Tecnologias e ferramentas | Python 3 |
| Natureza do conteúdo | Atividade prática (código comentado) |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`arvore_binaria.py`](arvore_binaria.py) | Calculadora de expressões com árvore binária: tokenização, conversão infixa → pós-fixa, construção da árvore, percursos, reconstrução, cálculo, exibição da árvore no terminal, testes e respostas às questões de análise (em comentários). |

> [!NOTE]
> **Limitações da documentação.** A pasta contém apenas o código-fonte. O arquivo cita um “PDF” com fluxograma e seções numeradas (4 a 15), que não está no repositório; a estrutura do enunciado foi reconstruída a partir dos comentários do código. O programa foi executado em Python 3 com as entradas indicadas nesta página.

<br />

<h2 id="visao-geral">Visão geral</h2>

Esta aula reúne as ideias da disciplina num único programa: **pilhas** (aulas 3 a 5), **recursão** (aulas 10 e 11) e uma estrutura nova, a **árvore binária**. O arquivo `arvore_binaria.py` é uma calculadora que recebe um texto como `(8 + 4) * 2` e o processa em etapas:

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart LR
    A["Texto digitado"] --> B["tokenizar()"]
    B --> C["para_posfixa()<br/>pilha de operadores"]
    C --> D["construir_arvore()<br/>pilha de nós"]
    D --> E["pre_ordem / em_ordem / pos_ordem"]
    D --> F["gerar_expressao()"]
    D --> G["calcular()"]
```

*Figura 1 — Pipeline da calculadora, conforme o comentário de abertura do arquivo. As três últimas etapas são recursivas e percorrem a mesma árvore.*

O código segue a numeração de seções de um enunciado em PDF que não está na pasta (seções 4 a 15) e termina com seis **questões de análise** respondidas em comentários.

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Representar uma expressão aritmética como **árvore binária**: operadores nos nós internos e números nas folhas.
- Separar um texto em **tokens** (números de vários dígitos, decimais, operadores e parênteses).
- Converter a notação **infixa** em **pós-fixa** com uma pilha e regras de precedência.
- Construir a árvore a partir da pós-fixa, respeitando a **ordem dos filhos**.
- Implementar os três **percursos recursivos** e relacioná-los às notações prefixa, infixa e pós-fixa.
- Avaliar a árvore recursivamente e tratar **erros de entrada**.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- Pilhas (LIFO) com `append` e `pop`, da [aula 3](../aula03-21-03-26/README.md) em diante.
- Recursão e caso-base, das [aulas 10](../aula10-08-09-26/README.md) e [11](../aula11-14-09-26/README.md).
- Classes simples em Python (`__init__`, atributos).
- Tratamento de exceções com `try`/`except` e `raise`.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Árvore binária

Uma **árvore binária** é formada por **nós**. Cada nó guarda um valor e duas referências: o filho **esquerdo** e o **direito**, que podem ser `None`. O nó do topo é a **raiz**, e os nós sem filhos são **folhas**. A **altura** é o número de arestas do caminho mais longo da raiz até uma folha.

Numa **árvore de expressão**:

- toda **folha** é um número;
- todo **nó interno** é um operador binário com exatamente dois filhos, ou seja, os operandos.

A precedência fica embutida na **forma** da árvore: o que precisa ser calculado primeiro fica mais **fundo**. Por isso a árvore dispensa parênteses.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart TD
    m["*"] --> p["+"]
    m --> s["-"]
    p --> d["/"]
    p --> t3["3"]
    d --> v20["20"]
    d --> v5["5"]
    s --> v9["9"]
    s --> q["+"]
    q --> v2["2"]
    q --> v1["1"]
```

*Figura 2 — Árvore de `((20 / 5) + 3) * (9 - (2 + 1))`, um dos casos de teste do arquivo (resultado 42). Em cada nó, o primeiro filho desenhado é o esquerdo.*

### 2. Notações e percursos

| Percurso | Ordem de visita | Notação produzida | Exemplo (`8 + 4 * 2`) |
| :--- | :--- | :--- | :--- |
| Pré-ordem | raiz, esquerda, direita | Prefixa | `+ 8 * 4 2` |
| Em ordem | esquerda, raiz, direita | Infixa (sem parênteses) | `8 + 4 * 2` |
| Pós-ordem | esquerda, direita, raiz | Pós-fixa | `8 4 2 * +` |

Na notação **pós-fixa**, também chamada de notação polonesa reversa, o operador vem **depois** dos operandos. Assim, ela não precisa de parênteses nem de regras de precedência para ser avaliada. O percurso **em ordem** reproduz a ordem dos símbolos, mas perde a hierarquia: `(8 + 4) * 2` e `8 + 4 * 2` produzem a mesma sequência. Por isso, `gerar_expressao()` coloca parênteses em **todo** nó interno.

### 3. Infixa → pós-fixa com pilha (as 5 regras do arquivo)

1. **Número:** vai direto para a saída.
2. **`(`:** é empilhado.
3. **`)`:** desempilha operadores para a saída até encontrar o `(`, que é descartado.
4. **Operador:** antes de empilhá-lo, desempilha os operadores do topo com prioridade **maior ou igual** (`*` e `/` valem 2; `+` e `-` valem 1).
5. **Fim dos tokens:** desempilha tudo o que sobrou.

O "**ou igual**" da regra 4 garante a associatividade à esquerda: `8 - 4 - 2` vira `8 4 - 2 -`, isto é, `(8 - 4) - 2 = 2`, e não `8 - (4 - 2) = 6`.

### 4. Pós-fixa → árvore com pilha de nós

Os tokens da pós-fixa são lidos da esquerda para a direita:

- **número:** cria uma folha e a empilha;
- **operador:** desempilha **dois** nós. O **primeiro** `pop` é o filho **direito**; o **segundo**, o **esquerdo**. O nó do operador liga os dois filhos e volta para a pilha.

No final, deve sobrar **exatamente um** nó, a raiz. Se sobrar mais de um, faltou operador (`8 4`); se faltarem nós para um operador, faltou operando (`8 +`).

### 5. Cálculo recursivo e custo

`calcular(no)` tem como **caso-base** a folha, que converte o texto em `float`. Para um operador, calcula a esquerda, calcula a direita e aplica a operação. Cada nó é visitado uma vez, portanto o custo é **O(n)**. A profundidade máxima da pilha de chamadas é a **altura** da árvore: cerca de $\log_2 n$ se ela for balanceada, e cerca de $n$ numa expressão "em fila", como `1 + (2 + (3 + ...))`.

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — os três percursos

```python
class No:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

def pre_ordem(no):
    if no is None:
        return []
    return [no.valor] + pre_ordem(no.esquerda) + pre_ordem(no.direita)

def em_ordem(no):
    if no is None:
        return []
    return em_ordem(no.esquerda) + [no.valor] + em_ordem(no.direita)

def pos_ordem(no):
    if no is None:
        return []
    return pos_ordem(no.esquerda) + pos_ordem(no.direita) + [no.valor]

# árvore de 8 + 4 * 2: o "*" fica mais fundo porque é calculado antes
raiz = No("+", No("8"), No("*", No("4"), No("2")))

print("pré-ordem :", " ".join(pre_ordem(raiz)))
print("em ordem  :", " ".join(em_ordem(raiz)))
print("pós-ordem :", " ".join(pos_ordem(raiz)))
```

Saída esperada:

```text
pré-ordem : + 8 * 4 2
em ordem  : 8 + 4 * 2
pós-ordem : 8 4 2 * +
```

### Exemplo intermediário — rastreando a conversão para pós-fixa

Versão reduzida de `para_posfixa()`, sem as validações de erro, que imprime a saída e a pilha a cada token:

```python
def precedencia(op):
    return 2 if op in "*/" else 1 if op in "+-" else 0

def para_posfixa(tokens):
    saida, pilha = [], []
    for t in tokens:
        if t == "(":
            pilha.append(t)
        elif t == ")":
            while pilha[-1] != "(":
                saida.append(pilha.pop())
            pilha.pop()
        elif t in "+-*/":
            while pilha and pilha[-1] != "(" and precedencia(pilha[-1]) >= precedencia(t):
                saida.append(pilha.pop())
            pilha.append(t)
        else:
            saida.append(t)
        print(f"{t:>2} | saída: {' '.join(saida):<14} | pilha: {''.join(pilha)}")
    while pilha:
        saida.append(pilha.pop())
    return saida

print("pós-fixa:", " ".join(para_posfixa(["2", "*", "(", "3", "+", "4", ")", "-", "5"])))
```

Saída esperada:

```text
 2 | saída: 2              | pilha: 
 * | saída: 2              | pilha: *
 ( | saída: 2              | pilha: *(
 3 | saída: 2 3            | pilha: *(
 + | saída: 2 3            | pilha: *(+
 4 | saída: 2 3 4          | pilha: *(+
 ) | saída: 2 3 4 +        | pilha: *
 - | saída: 2 3 4 + *      | pilha: -
 5 | saída: 2 3 4 + * 5    | pilha: -
pós-fixa: 2 3 4 + * 5 -
```

Ao chegar o `-`, o `*` do topo tem prioridade maior e vai para a saída antes. Por isso, `2 * (3 + 4)` é calculado antes de subtrair 5, com resultado 9.

### Exemplo aplicado — por que o primeiro `pop` é o filho direito

```python
def calcular_posfixa(posfixa):
    pilha = []
    for t in posfixa:
        if t in "+-*/":
            b = pilha.pop()   # 1º pop: operando DIREITO
            a = pilha.pop()   # 2º pop: operando ESQUERDO
            pilha.append({"+": a + b, "-": a - b, "*": a * b, "/": a / b}[t])
        else:
            pilha.append(float(t))
    return pilha[0]

def altura_cadeia(n):
    # 1 + (2 + (3 + ...)): cada "+" tem outro "+" como filho direito
    return n - 1

print(calcular_posfixa("8 4 - 2 -".split()))   # (8 - 4) - 2
print(calcular_posfixa("8 4 2 - -".split()))   # 8 - (4 - 2)
print("altura da cadeia com 1200 números:", altura_cadeia(1200))
```

Saída esperada:

```text
2.0
6.0
altura da cadeia com 1200 números: 1199
```

As duas pós-fixas têm os mesmos símbolos, mas representam árvores diferentes. Trocar a ordem dos `pop` inverteria `a - b` para `b - a`.

### Executando o programa original

O programa é interativo: aceita expressões, `testes` ou `sair`. Uma execução real com a entrada `(8 + 4) * 2`:

<!-- norun -->
```text
Digite uma expressão: (8 + 4) * 2
Tokens:            ['(', '8', '+', '4', ')', '*', '2']
Pós-fixa:          8 4 + 2 *
Pré-ordem:         * + 8 4 2
Em ordem:          8 + 4 * 2
Pós-ordem:         8 4 + 2 *
Expr. reconstruída: ((8 + 4) * 2)
Árvore:
    2
*
        4
    +
        8
Resultado:         24
```

A função `mostrar_arvore()` desenha a árvore "deitada": a raiz fica à esquerda, o filho **direito** aparece acima e o **esquerdo** abaixo. Inclinando a cabeça para a esquerda, a figura vira a árvore usual.

O comando `testes` executa os 5 casos válidos e os 9 inválidos de `executar_testes()`. Na execução feita para esta documentação, **todos os 14 resultaram em `[OK]`**: entre eles, `((15 - 3) / 4) + (2 * 5) = 13`, `12.5 + 2.5 * 4 = 22.5`, divisão por zero, parênteses incompatíveis, expressão vazia, caractere inválido (`8 + a`), operador sem operandos (`8 +`), operandos sem operador (`8 4`) e número malformado (`1.2.3`).

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

### Questões de análise (seção 15 do arquivo)

O próprio arquivo traz respostas em comentários, com a observação "revise e reescreva com suas palavras antes de entregar". A síntese abaixo é a **solução do material original**:

| Questão | Resposta do arquivo (síntese) |
| :--- | :--- |
| 1. Por que tokenizar? | Agrupa caracteres em unidades com significado (`"15"` em vez de `'1'` e `'5'`), descarta espaços e detecta caracteres inválidos. |
| 2. Por que uma pilha para operadores e parênteses? | Ela é LIFO: o último `(` aberto é o primeiro fechado, e o operador mais recente é o primeiro comparado. Isso reproduz o aninhamento e a precedência. |
| 3. Por que o primeiro `pop` é o filho direito? | Em `a b op`, `b` foi empilhado por último e sai primeiro. Inverter trocaria `a - b` por `b - a`. |
| 4. Relação entre pós-ordem e pós-fixa | A pós-ordem visita esquerda, direita e raiz: operando, operando, operador, exatamente a notação pós-fixa. |
| 5. Complexidade de calcular uma árvore de n nós | O(n): cada nó é visitado uma vez, com trabalho constante. |
| 6. O que limita as chamadas recursivas simultâneas? | A altura h: no máximo h + 1 chamadas ativas. Balanceada: h ≈ log n; "em fila": h ≈ n, com risco de estourar o limite de recursão do Python (cerca de 1000). |

> [!TIP]
> A resposta 6 foi confirmada por execução: `calcular_texto()` aplicado a uma expressão encadeada `1199 + (... + (2 + (1)))` com 1.199 números lançou `RecursionError: maximum recursion depth exceeded`.

### Exercícios propostos para estudo

1. Converta `7 - 2 * 3` para pós-fixa e calcule o resultado.
2. Desenhe a árvore de `(15 - 3) / 4` e escreva seus três percursos.
3. Por que a calculadora rejeita `-3 + 5`? Que mudança seria necessária para aceitá-la?
4. Qual a altura da árvore de `((20 / 5) + 3) * (9 - (2 + 1))`?

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

1. Pós-fixa `7 2 3 * -`; resultado `7 - 6 = 1`. O programa original retorna `1.0` em `calcular_texto("7 - 2 * 3")`.
2. Raiz `/`, com filho esquerdo `-` (folhas 15 e 3) e filho direito 4. Pré-ordem: `/ - 15 3 4`; em ordem: `15 - 3 / 4`; pós-ordem: `15 3 - 4 /`.
3. O tokenizador trata todo `-` como operador **binário**. A pós-fixa fica `3 - 5 +`, e o `-` não encontra dois operandos, gerando o erro "operador sem operandos" (verificado). Para aceitar o menos unário, seria preciso reconhecê-lo na tokenização (um `-` no início ou logo após `(` ou de outro operador) e tratá-lo como um operador de **um** filho, ou incorporá-lo ao número.
4. **3**. O caminho mais longo é `*` → `-` → `+` → `2` (ou `1`), conforme a Figura 2.

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Compiladores e interpretadores:** a análise sintática de linguagens de programação gera **árvores sintáticas abstratas** (*AST*) do mesmo tipo. O módulo `ast` do Python expõe a árvore do próprio código-fonte.
- **Planilhas e calculadoras:** fórmulas digitadas pelo usuário passam por tokenização, análise e avaliação, como nesta calculadora.
- **Bancos de dados:** consultas SQL viram árvores de operadores (filtros, junções, projeções) que o otimizador reorganiza antes de executar.
- **Validação de entrada:** os testes de expressões inválidas ilustram como tratar dados do usuário sem derrubar o programa.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Ler a expressão caractere por caractere direto na árvore | Tokenizar primeiro | Números de vários dígitos e decimais viram um único token |
| Usar só "maior" na regra 4 | Desempilhar operadores de prioridade **maior ou igual** | Mantém a associatividade à esquerda (`8 - 4 - 2 = 2`) |
| Ligar o primeiro `pop` como filho esquerdo | Primeiro `pop` = **direito** | Evita inverter subtrações e divisões |
| Converter os valores para número ao criar os nós | Guardar texto e converter só em `calcular()` | Mantém a árvore fiel à entrada para percursos e reconstrução |
| Deixar o programa encerrar com exceção | `try`/`except` no laço principal | O usuário pode corrigir a expressão e continuar |
| Recursão sem considerar a altura | Saber que a profundidade da pilha de chamadas = altura | Expressões muito encadeadas estouram o limite de recursão |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Árvore de expressão: **folhas = números**, **nós internos = operadores**; a forma da árvore codifica a precedência.
- Pipeline: `tokenizar` → `para_posfixa` (pilha de operadores) → `construir_arvore` (pilha de nós) → percursos e cálculo.
- Pré-ordem = prefixa; em ordem = infixa sem parênteses; **pós-ordem = pós-fixa**.
- Na construção, **o primeiro `pop` é o filho direito**.
- `calcular` é O(n) em tempo; a profundidade da recursão é a **altura** da árvore.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Qual é a pós-fixa de `(8 + 4) * 2`?
2. Ao construir a árvore a partir de `9 3 /`, qual nó vira filho esquerdo de `/`?
3. Qual percurso, sozinho, não basta para reconstruir a expressão sem ambiguidade? Por quê?
4. Por que `8 4` é inválida, se não contém nenhum caractere proibido?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. `8 4 + 2 *`, a mesma sequência impressa pelo programa.
2. O nó `9`. O `3` sai primeiro da pilha e vira o filho direito, então a expressão é `9 / 3`.
3. O percurso **em ordem**: `(8 + 4) * 2` e `8 + 4 * 2` produzem a mesma sequência `8 + 4 * 2`. Por isso `gerar_expressao()` acrescenta parênteses.
4. Ao final da construção, sobram **dois** nós na pilha. Falta um operador para uni-los, e o programa acusa "operandos sem operador".

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [Python — módulo `ast` (árvores sintáticas abstratas)](https://docs.python.org/pt-br/3/library/ast.html)
- [Python — `sys.getrecursionlimit`](https://docs.python.org/pt-br/3/library/sys.html#sys.getrecursionlimit)
- Material da pasta: [`arvore_binaria.py`](arvore_binaria.py)

<br />

<p align="center"><a href="../aula13-24-09-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
