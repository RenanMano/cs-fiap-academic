<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Vetores%20e%20Matrizes&amp;fontSize=40&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=MODELAGEM%20MATEM%C3%81TICA%20E%20COMPUTACIONAL%20%E2%80%94%20AULA%2012%20%E2%80%94%2004%2F09%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Resolução do Gini, Vetores, Matrizes e Sistemas Lineares" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=v%20%C2%B7%20u%20%3D%20v%E2%82%81u%E2%82%81%20%2B%20v%E2%82%82u%E2%82%82%20%2B%20v%E2%82%83u%E2%82%83;Receita%20%3D%20pre%C3%A7os%20%C2%B7%20quantidades;%28m%C3%97n%29%28n%C3%97p%29%20%3D%20%28m%C3%97p%29%2C%20AB%20%E2%89%A0%20BA;Gauss%3A%20troca%2C%20multiplica%2C%20soma%20linhas" alt="v · u = v₁u₁ + v₂u₂ + v₃u₃. Receita = preços · quantidades. (m×n)(n×p) = (m×p); AB ≠ BA. Gauss: troca, multiplica, soma linhas." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-MMC-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: MMC" />
  <img src="https://img.shields.io/badge/Aula-12-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 12" />
  <img src="https://img.shields.io/badge/Data-04--09--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 04-09-2026" />
  <img src="https://img.shields.io/badge/Tema-%C3%81lgebra%20linear-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Tema: Álgebra linear" />
  <img src="https://img.shields.io/badge/Opera%C3%A7%C3%A3o-Produto%20escalar-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Operação: Produto escalar" />
  <img src="https://img.shields.io/badge/M%C3%A9todo-Elimina%C3%A7%C3%A3o%20de%20Gauss-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Método: Eliminação de Gauss" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Modelagem Matemática e Computacional](../README.md) |
| Aula | 12 — 04/09/2026 |
| Título | Resolução do Gini, Vetores, Matrizes e Sistemas Lineares |
| Tema central | Resolução da atividade do Índice de Gini; vetores (visões da física, computação e matemática), soma, multiplicação por escalar, produto escalar (receita de vendas, perpendicularidade) e produto vetorial; matrizes (tipos, transposta, soma, multiplicação, identidade, inversa); sistemas lineares na forma Ax = b e escalonamento de Gauss. |
| Tecnologias e ferramentas | Python 3, NumPy (verificações) |
| Docente (conforme material) | Prof. Igor Gimenes Cesca |
| Natureza do conteúdo | Anotações de aula |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`Aula 4 - Turma X.pdf`](Aula%204%20-%20Turma%20X.pdf) | Anotações da aula 4 (8 páginas): resolução da atividade do Índice de Gini (L = x² e ajuste da Tabela 1) e introdução a vetores: notação, representação geométrica, soma, multiplicação por escalar, produto escalar (aplicação em receita) e produto vetorial. |
| [`Aula 5 - Turma X.pdf`](Aula%205%20-%20Turma%20X.pdf) | Anotações da aula 5 (6 páginas): matrizes (definição, classificação, transposta, soma, multiplicação, identidade, inversa), sistemas lineares em forma matricial e escalonamento de Gauss com exemplo e exercício. |

> [!NOTE]
> **Limitações da documentação.** As anotações combinam texto digitado e resoluções manuscritas, lidas visualmente. Todos os cálculos foram conferidos com NumPy e frações exatas; um deslize manuscrito no produto QP está comentado.

<br />

<h2 id="visao-geral">Visão geral</h2>

A aula 4 fecha a atividade do Índice de Gini da [aula 10](../aula10-20-08-26/README.md) (Gini = 1/3 para $L = x^2$ e ≈ 0,508 para o ajuste brasileiro, "alta concentração") e inicia a **Álgebra Linear**. A aula 5 avança para **matrizes** e **sistemas lineares**.

O que é um **vetor**, segundo as anotações:

| Área | Definição |
| :--- | :--- |
| Física | Seta com **direção**, **sentido** e **módulo** |
| Computação | Estrutura com dados gravados **em ordem** |
| Matemática | Seta que parte da origem até um ponto, com coordenadas ordenadas |

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Somar vetores, multiplicá-los por escalar e calcular produtos escalar e vetorial.
- Interpretar o produto escalar (receita, perpendicularidade).
- Classificar matrizes e operar com elas, incluindo a condição de multiplicação.
- Escrever sistemas lineares na forma $Ax = b$ e resolvê-los por escalonamento.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- Plano cartesiano e coordenadas.
- Sistemas de equações do ensino médio (substituição e adição).

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Vetores

**Notação:** $\vec{v} = \langle x, y \rangle = (x\ \ y) = \begin{pmatrix} x \\ y \end{pmatrix}$.

| Operação | Definição | Resultado |
| :--- | :--- | :--- |
| Soma | $\langle a, b \rangle + \langle x, y \rangle = \langle a + x, b + y \rangle$ | Vetor |
| Multiplicação por constante | $k\langle x, y \rangle = \langle kx, ky \rangle$ | Vetor |
| **Produto escalar** | $\vec{v} \cdot \vec{u} = v_1u_1 + v_2u_2 + v_3u_3 = \lvert\vec{v}\rvert\,\lvert\vec{u}\rvert \cos\theta$ | **Número** |
| **Produto vetorial** | $\vec{v} \times \vec{u} = \det\begin{pmatrix} \vec{i} & \vec{j} & \vec{k} \\ v_1 & v_2 & v_3 \\ u_1 & u_2 & u_3 \end{pmatrix}$ | Vetor **perpendicular** a ambos |

Pela forma com $\cos\theta$, vetores **perpendiculares** ($\theta = 90°$) têm produto escalar **zero**. As anotações mostram isso com $\langle 2, 0 \rangle \cdot \langle 0, 3 \rangle = 0$.

**Grandezas** (tabela das anotações): vetoriais, como velocidade e gravidade, × escalares, como massa e tempo.

### 2. Matrizes

Uma matriz $A = (a_{ij})_{m \times n}$ é uma tabela cujos elementos são identificados por linha $i$ e coluna $j$.

| Tipo | Característica |
| :--- | :--- |
| Quadrada | Nº de linhas = nº de colunas |
| Linha / coluna | Uma só linha ou coluna; também é um vetor |
| Identidade $I$ | Diagonal de 1, demais elementos 0; elemento neutro: $AI = IA = A$ |
| Transposta $A^T$ | Linhas viram colunas: $(a_{ij}) \to (a_{ji})$ |
| Inversa $A^{-1}$ | $AA^{-1} = I$; exige matriz **quadrada** com **determinante ≠ 0** |

**Multiplicação:** $(A_{m \times n})(B_{n \times p}) = C_{m \times p}$. O número de colunas da primeira deve ser igual ao número de linhas da segunda. Ela **não é comutativa**: em geral $AB \neq BA$, e às vezes só um dos produtos existe.

### 3. Sistemas lineares e escalonamento

Um sistema com $m$ equações e $n$ variáveis (todas com expoente 1) escreve-se como $A_{m \times n}\,X_{n \times 1} = b_{m \times 1}$, com $A$ a matriz dos coeficientes, $X$ a das variáveis e $b$ a dos termos independentes.

**Escalonamento (eliminação de Gauss):** aplica **operações elementares** à **matriz expandida** $[A \mid b]$:

1. trocar linhas;
2. multiplicar uma linha por uma constante (não nula);
3. somar a uma linha um múltiplo de outra.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart LR
    S["Sistema"] --> M["Matriz expandida [A | b]"]
    M --> E["Operações elementares:<br/>zerar abaixo dos pivôs"]
    E --> T["Forma escalonada<br/>(triangular)"]
    T --> R["Retrossubstituição:<br/>última equação → primeira"]
```

*Figura 1 — Etapas do método de Gauss.*

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — vetores das anotações

```python
import numpy as np

u, v = np.array([1, 3]), np.array([3, 2])
print("u + v =", u + v, "| 2·<3, 3> =", 2 * np.array([3, 3]))

a, b = np.array([1, -2, 0]), np.array([-2, 4, -3])
print("a · b =", a @ b)                                  # produto escalar: um número

precos, quantidades = np.array([4, 2, 5]), np.array([5, 10, 6])
print("receita = preços · quantidades =", precos @ quantidades)

print("<2, 0> · <0, 3> =", np.array([2, 0]) @ np.array([0, 3]), "→ vetores perpendiculares")

c, d = np.array([1, -1, 2]), np.array([2, -1, 3])
cxd = np.cross(c, d)                                     # produto vetorial: um vetor
print("c × d =", cxd, "| perpendicular a c e d?", cxd @ c == 0 and cxd @ d == 0)
```

Saída esperada:

```text
u + v = [4 5] | 2·<3, 3> = [6 6]
a · b = -10
receita = preços · quantidades = 70
<2, 0> · <0, 3> = 0 → vetores perpendiculares
c × d = [-1  1  1] | perpendicular a c e d? True
```

A **receita** é o produto escalar do vetor de preços (\$ 4, \$ 2, \$ 5) pelo vetor de quantidades (5, 10, 6): $20 + 20 + 30 = 70$.

### Exemplo intermediário — matrizes das anotações

```python
import numpy as np

A = np.array([[1, 2, 3]])                       # 1×3
B = np.array([[-1], [1], [2]])                  # 3×1
C = np.array([[1, 2], [0, -1], [1, 0]])         # 3×2
print("AB =", A @ B, "| AC =", A @ C)
try:
    C @ A                                       # (3×2)(1×3): colunas de C ≠ linhas de A
except ValueError:
    print("CA: multiplicação impossível (3×2 por 1×3)")

Q = np.array([[1, 2, 3], [-1, 0, 1]])
P = np.array([[1, -1, 1], [2, 0, 1], [0, 4, -1]])
print("QP =\n", Q @ P)
print("PI = P?", np.array_equal(P @ np.eye(3, dtype=int), P))
print("transposta de [[1, 2], [3, 4]] =", np.array([[1, 2], [3, 4]]).T.tolist())
```

Saída esperada:

```text
AB = [[7]] | AC = [[4 0]]
CA: multiplicação impossível (3×2 por 1×3)
QP =
 [[ 5 11  0]
 [-1  5 -2]]
PI = P? True
transposta de [[1, 2], [3, 4]] = [[1, 3], [2, 4]]
```

> [!NOTE]
> Nas anotações, $QP$ aparece como $\begin{pmatrix} 5 & 11 & 0 \\ -1 & 5 & 0 \end{pmatrix}$. O elemento da 2ª linha e 3ª coluna é $(-1)(1) + (0)(1) + (1)(-1) = -2$, e não 0, como confirma a execução acima.

### Exemplo aplicado — escalonamento passo a passo

Implementação própria com frações exatas, aplicada ao exemplo e ao exercício das anotações:

```python
from fractions import Fraction as Fr

def escalonar(M):
    """Eliminação de Gauss com retrossubstituição, imprimindo cada operação."""
    M = [[Fr(x) for x in linha] for linha in M]
    n = len(M)
    for i in range(n):
        if M[i][i] == 0:                                       # troca de linhas
            k = next(k for k in range(i + 1, n) if M[k][i] != 0)
            M[i], M[k] = M[k], M[i]
            print(f"L{i+1} ↔ L{k+1}")
        for k in range(i + 1, n):
            fator = M[k][i] / M[i][i]
            M[k] = [a - fator * b for a, b in zip(M[k], M[i])]
            print(f"L{k+1} ← L{k+1} − ({fator})·L{i+1}:", [str(x) for x in M[k]])
    x = [Fr(0)] * n
    for i in reversed(range(n)):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return [str(v) for v in x]

print("2x + y = 1, −x − y = 4  →", escalonar([[2, 1, 1], [-1, -1, 4]]))
print("2x + y = 7,  x + y = 5  →", escalonar([[2, 1, 7], [1, 1, 5]]))
```

Saída esperada:

```text
L2 ← L2 − (-1/2)·L1: ['0', '-1/2', '9/2']
2x + y = 1, −x − y = 4  → ['5', '-9']
L2 ← L2 − (1/2)·L1: ['0', '1/2', '3/2']
2x + y = 7,  x + y = 5  → ['2', '3']
```

As anotações resolvem o primeiro sistema trocando as linhas antes de eliminar e chegam ao mesmo resultado: $y = -9$ e $x = 5$. O exercício dá $x = 2$ e $y = 3$, conferindo com as anotações.

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

| Exercício das anotações | Solução do material original | Conferência |
| :--- | :--- | :--- |
| Gini com $L = x^2$ | $2\left(\frac{3 - 2}{6}\right) = \frac{1}{3} \approx 0{,}333$ | ✔ |
| Gini com $L = 0{,}7604x^{2{,}0926}$ | $2(0{,}2541227) = 0{,}50824$, "alta concentração" | ✔ (≈ 0,50825) |
| $\vec{a} \cdot \vec{b}$ com $\langle 1, -2, 0 \rangle$ e $\langle -2, 4, -3 \rangle$ | $-10$ | ✔ |
| $\langle 1, -1, 2 \rangle \times \langle 2, -1, 3 \rangle$ | $\langle -1, 1, 1 \rangle$ | ✔ |
| $AB$, $CA$, $AC$ | $(7)$; impossível; $(4\ \ 0)$, logo $AC \neq CA$ | ✔ |
| $QP$ | ver a nota acima | ⚠ elemento (2,3) |
| $2x + y = 7$; $x + y = 5$ | $y = 3$, $x = 2$ | ✔ |

**Exercício proposto para estudo:** resolva por escalonamento $x + y + z = 6$, $2x - y + z = 3$, $x + 2y - z = 3$ (o mesmo sistema resolvido com NumPy no notebook da [aula 13](../aula13-09-09-26/README.md)).

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

```python
import numpy as np
from fractions import Fraction

A = np.array([[1, 1, 1], [2, -1, 1], [1, 2, -1]])
b = np.array([6, 3, 3])
x = np.linalg.solve(A, b)
print([str(Fraction(v).limit_denominator(100)) for v in x])
```

Saída esperada:

```text
['9/7', '15/7', '18/7']
```

$L_2 \leftarrow L_2 - 2L_1$ e $L_3 \leftarrow L_3 - L_1$ geram $-3y - z = -9$ e $y - 2z = -3$. Daí $y = 2z - 3$; substituindo, $-3(2z - 3) - z = -9 \Rightarrow z = 18/7$, $y = 15/7$ e $x = 6 - y - z = 9/7$.

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Sistemas de recomendação:** usuários e itens viram vetores, e a similaridade é medida pelo produto escalar ([aula 13](../aula13-09-09-26/README.md)).
- **Machine learning:** dados em matrizes; a previsão de uma rede neural é uma sequência de multiplicações matriciais.
- **Computação gráfica e física:** o produto vetorial dá normais de superfícies e torques.
- **Imagens médicas:** tomografia e ressonância reconstroem imagens resolvendo grandes sistemas lineares, aplicação citada na aula 1 do semestre.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Multiplicar matrizes sem checar dimensões | Conferir colunas da 1ª = linhas da 2ª | Senão o produto não existe |
| Supor $AB = BA$ | Calcular os dois produtos | A multiplicação não é comutativa |
| Usar `*` do NumPy para produto matricial | Usar `@` ou `np.matmul` | `*` multiplica elemento a elemento |
| Escalonar com decimais arredondados | Usar frações | Evita acúmulo de erros |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Produto escalar → número (zero se perpendiculares); produto vetorial → vetor perpendicular.
- $(m \times n)(n \times p) = m \times p$; $AB \neq BA$; $AI = A$.
- Inversa: só para matriz quadrada com $\det \neq 0$.
- Sistema $Ax = b$; Gauss: operações elementares na matriz expandida + retrossubstituição.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Calcule $\langle 3, -1, 2 \rangle \cdot \langle 1, 4, 0 \rangle$.
2. Uma matriz $2 \times 3$ pode ser multiplicada por uma $2 \times 3$?
3. Quais são as três operações elementares do escalonamento?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. $3 - 4 + 0 = -1$.
2. Não: a primeira tem 3 colunas e a segunda, 2 linhas. Com a transposta da segunda ($3 \times 2$), sim.
3. Trocar linhas, multiplicar uma linha por constante não nula e somar a uma linha um múltiplo de outra.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- STEINBRUCH, W. *Álgebra Linear*. Saraiva, 2006 (bibliografia básica do [plano de ensino](../aula01-03-03-26/README.md)).
- [NumPy — `cross`](https://numpy.org/doc/stable/reference/generated/numpy.cross.html) · [`linalg.solve`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)
- Materiais da pasta: [Aula 4](Aula%204%20-%20Turma%20X.pdf) · [Aula 5](Aula%205%20-%20Turma%20X.pdf)

<br />

<p align="center"><a href="../aula11-25-08-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula13-09-09-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
