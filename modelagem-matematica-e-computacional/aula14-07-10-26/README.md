<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=%C3%81lgebra%20Linear%20Computacional&amp;fontSize=30&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=MODELAGEM%20MATEM%C3%81TICA%20E%20COMPUTACIONAL%20%E2%80%94%20AULA%2014%20%E2%80%94%2007%2F10%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Álgebra Linear Computacional: Posto, Escalonamento, Determinantes e Inversas" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=posto%28A%29%20%3D%20posto%28%5BA%7Cb%5D%29%20%3D%20n%20%E2%86%92%20SPD;posto%28A%29%20%3C%20posto%28%5BA%7Cb%5D%29%20%E2%86%92%20SI;det%28A%29%20%3D%200%20%E2%86%92%20sem%20inversa;x%20%3D%20A%E2%81%BB%C2%B9b%20%3D%20np.linalg.solve%28A%2C%20b%29" alt="posto(A) = posto([A|b]) = n → SPD. posto(A) < posto([A|b]) → SI. det(A) = 0 → sem inversa. x = A⁻¹b = np.linalg.solve(A, b)." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-MMC-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: MMC" />
  <img src="https://img.shields.io/badge/Aula-14-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 14" />
  <img src="https://img.shields.io/badge/Data-07--10--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 07-10-2026" />
  <img src="https://img.shields.io/badge/Ambiente-Jupyter-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=jupyter&amp;logoColor=white" alt="Ambiente: Jupyter" />
  <img src="https://img.shields.io/badge/Bibliotecas-NumPy%20%C2%B7%20SymPy-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Bibliotecas: NumPy · SymPy" />
  <img src="https://img.shields.io/badge/Tema-Rouch%C3%A9--Capelli-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Tema: Rouché-Capelli" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Modelagem Matemática e Computacional](../README.md) |
| Aula | 14 — 07/10/2026 |
| Título | Álgebra Linear Computacional: Posto, Escalonamento, Determinantes e Inversas |
| Tema central | Notebook de álgebra linear computacional: resolução de sistemas com np.linalg.solve, matriz aumentada e posto para classificar SPD, SPI e SI, escalonamento de Gauss-Jordan com SymPy (rref), determinantes, matriz inversa, sistemas via inversa e os erros esperados para matrizes não quadradas ou singulares. |
| Tecnologias e ferramentas | Python 3, Jupyter/Colab, NumPy, SymPy |
| Natureza do conteúdo | Notebook Jupyter (prática computacional) |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`Aula_8_Álgebra_Linear_Computacional.ipynb`](Aula_8_%C3%81lgebra_Linear_Computacional.ipynb) | Notebook “Aula 8 — Álgebra Linear Computacional” (50 células, sem saídas): sistemas lineares com NumPy, posto e classificação, escalonamento com SymPy (rref) para SPD, SPI e SI, determinantes, matriz inversa e sistemas resolvidos pela inversa e por solve. |

> [!NOTE]
> **Limitações da documentação.** O notebook (50 células) não tem saídas salvas, ou seja, foi entregue sem execução. As células NumPy foram reexecutadas com NumPy 2.5; as células SymPy (rref, rank) não puderam ser executadas porque o SymPy não está instalado no ambiente e não foi instalado — seus resultados foram obtidos com NumPy (posto) e escalonamento próprio. O notebook não contém credenciais.

<br />

<h2 id="visao-geral">Visão geral</h2>

O último material da disciplina reúne, num notebook, as ferramentas computacionais para tudo o que foi visto em álgebra linear:

| Seção do notebook | Ferramentas |
| :--- | :--- |
| Sistemas lineares | `np.linalg.solve`, `np.hstack` (matriz aumentada), `np.linalg.matrix_rank` |
| Escalonamento | `sp.Matrix(...).row_join(b).rref()` (Gauss-Jordan) |
| SPD, SPI e SI | `A.rank()` e `M.rank()` no SymPy |
| Determinantes | `np.linalg.det` |
| Matriz inversa | `np.linalg.inv`, verificação de $AA^{-1} = I$ |
| Inversa e sistemas | $x = A^{-1}b$ comparado com `np.linalg.solve` |

O notebook também provoca **erros intencionais**: determinante e inversa de matriz não quadrada, inversa de matriz singular e `solve` de sistema sem solução única. Eles ilustram as condições teóricas.

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Classificar sistemas pelo posto (teorema de Rouché-Capelli).
- Escalonar por Gauss-Jordan e ler a solução na matriz reduzida.
- Calcular determinantes e inversas e reconhecer quando não existem.
- Resolver sistemas por $A^{-1}b$ e por `solve`, sabendo por que o segundo é preferível.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 12](../aula12-04-09-26/README.md) (matrizes, inversa, Gauss) e [aula 13](../aula13-09-09-26/README.md) (pivôs, SPD, SPI).

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Posto e classificação (Rouché-Capelli)

O **posto** é o número de pivôs (linhas não nulas) após o escalonamento. Para $Ax = b$ com $n$ variáveis:

| Condição | Classificação |
| :--- | :--- |
| $\operatorname{posto}(A) = \operatorname{posto}([A \mid b]) = n$ | **SPD**: solução única |
| $\operatorname{posto}(A) = \operatorname{posto}([A \mid b]) < n$ | **SPI**: infinitas soluções |
| $\operatorname{posto}(A) < \operatorname{posto}([A \mid b])$ | **SI**: sem solução |

### 2. Gauss-Jordan (`rref`)

Gauss-Jordan continua o escalonamento até a **forma escalonada reduzida**, com pivôs iguais a 1 e zeros acima e abaixo. Num SPD, a parte de $A$ vira a **identidade**, e a última coluna mostra a **solução**, como diz o comentário do notebook.

### 3. Determinante e inversa

- O **determinante** só existe para matrizes **quadradas**.
- A **inversa** exige matriz quadrada e $\det(A) \neq 0$. Se $\det(A) = 0$, a matriz é **singular**.

### 4. Inversa × `solve`

$x = A^{-1}b$ é correto na teoria, mas na prática `np.linalg.solve(A, b)` é **preferível**: faz menos operações e é numericamente mais estável, porque não forma a inversa explicitamente.

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — as células do notebook reexecutadas com NumPy

Inclui os erros intencionais do notebook, capturados com `try`/`except`:

```python
import numpy as np

def classificar(A, b):
    """Teorema de Rouché-Capelli: compara posto(A), posto([A|b]) e nº de variáveis."""
    pa = np.linalg.matrix_rank(A)
    pab = np.linalg.matrix_rank(np.hstack((A, b)))
    n = A.shape[1]
    if pa < pab:
        return "SI"
    return "SPD" if pa == n else "SPI"

casos = {
    "célula 2  (SPD)": (np.array([[1, 1, 1], [1, -1, 1], [2, 1, -1]]), np.array([[6], [2], [7]])),
    "célula 17 (SPD)": (np.array([[1, 1, 1], [2, -1, 1], [1, 2, -1]]), np.array([[6], [2], [7]])),
    "célula 19 (SPI)": (np.array([[1, 1, 1], [2, 2, 2]]), np.array([[2], [4]])),
    "célula 26 (SI)":  (np.array([[1, 1, 1], [2, 2, 2]]), np.array([[2], [5]])),
}
for nome, (A, b) in casos.items():
    print(f"{nome}: {classificar(A, b)}")

print("solução célula 7 :", np.linalg.solve(*casos["célula 2  (SPD)"]).ravel())
print("solução célula 17:", np.linalg.solve(*casos["célula 17 (SPD)"]).ravel().round(6))

A = np.array([[2, 1], [3, 4]])
B = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
print("det(A) =", round(np.linalg.det(A), 6), "| det(B) =", round(np.linalg.det(B), 6))
print("A⁻¹ =", np.linalg.inv(A).round(4).tolist())
print("A·A⁻¹ = I?", np.allclose(A @ np.linalg.inv(A), np.eye(2)))
print("x = A⁻¹b =", np.linalg.inv(A) @ np.array([5, 6]), "| solve:", np.linalg.solve(A, [5, 6]))

for rotulo, acao in [("det de matriz 3×1", lambda: np.linalg.det(np.array([[6], [2], [7]]))),
                     ("inversa de [[2, 2], [3, 3]]", lambda: np.linalg.inv(np.array([[2, 2], [3, 3]]))),
                     ("solve com [[2, 2], [4, 4]]", lambda: np.linalg.solve(np.array([[2, 2], [4, 4]]), [2, 5]))]:
    try:
        acao()
    except np.linalg.LinAlgError as erro:
        print(f"{rotulo}: LinAlgError — {erro}")
```

Saída esperada:

```text
célula 2  (SPD): SPD
célula 17 (SPD): SPD
célula 19 (SPI): SPI
célula 26 (SI): SI
solução célula 7 : [3. 2. 1.]
solução célula 17: [2. 3. 1.]
det(A) = 5.0 | det(B) = 1.0
A⁻¹ = [[0.8, -0.2], [-0.6, 0.4]]
A·A⁻¹ = I? True
x = A⁻¹b = [ 2.8 -0.6] | solve: [ 2.8 -0.6]
det de matriz 3×1: LinAlgError — Last 2 dimensions of the array must be square
inversa de [[2, 2], [3, 3]]: LinAlgError — Singular matrix
solve com [[2, 2], [4, 4]]: LinAlgError — Singular matrix
```

**Leitura:**

- As células 2 e 47 resolvem o mesmo sistema da [aula 13](../aula13-09-09-26/README.md), com solução $(3, 2, 1)$.
- A célula 17 tem solução $(2, 3, 1)$.
- O par das células 19 e 26 só difere no termo independente ($4$ × $5$): $2x + 2y + 2z = 4$ é o dobro da primeira equação (SPI), e $= 5$ a contradiz (SI).

### Exemplo intermediário — o escalonamento do SymPy (código original)

Verificado estaticamente, pois o SymPy não está instalado no ambiente:

<!-- norun -->
```python
import sympy as sp

A = sp.Matrix([[1, 1, 1], [1, -1, 1], [2, 1, -1]])
b = sp.Matrix([[6], [2], [7]])
Expandida = A.row_join(b)            # matriz aumentada [A | b]
A_esc, pivots = Expandida.rref()     # Gauss-Jordan e índices das colunas-pivô
```

Pela teoria, `A_esc` deve ser $\begin{pmatrix} 1 & 0 & 0 & 3 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 1 \end{pmatrix}$ e `pivots` deve ser `(0, 1, 2)`, coerente com a solução $(3, 2, 1)$ obtida por `solve` acima.

### Exemplo aplicado — atenção à lógica da célula 9

A célula 9 classifica o sistema assim:

<!-- norun -->
```python
if posto_A == n_variaveis:
    print("Sistema SPD")
elif posto_A < n_variaveis:
    print("Sistema SPI")
else:
    print("Sistema SI")
```

> [!WARNING]
> Essa lógica **não usa o posto da matriz aumentada** (calculado na mesma célula) e nunca chega ao ramo "SI": o posto de $A$ nunca é maior que o número de variáveis. Um sistema impossível, como o da célula 26, seria rotulado como **SPI**. A versão do exemplo básico (`classificar`) compara primeiro `posto(A) < posto([A|b])`. As células 17, 24 e 29, feitas com SymPy, imprimem os dois postos, o que permite a classificação correta.

```python
import numpy as np

A, b = np.array([[1, 1, 1], [2, 2, 2]]), np.array([[2], [5]])
pa, n = np.linalg.matrix_rank(A), A.shape[1]
print("lógica da célula 9:", "SPD" if pa == n else "SPI" if pa < n else "SI")
print("posto(A) =", pa, "| posto([A|b]) =", np.linalg.matrix_rank(np.hstack((A, b))))
```

Saída esperada:

```text
lógica da célula 9: SPI
posto(A) = 1 | posto([A|b]) = 2
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

O notebook não traz exercícios propostos. Abaixo, um exercício **proposto para estudo**.

> Para quais valores de $k$ o sistema $x + 2y = 3$, $2x + ky = 6$ é SPD, SPI ou SI?

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

$\det\begin{pmatrix} 1 & 2 \\ 2 & k \end{pmatrix} = k - 4$.

- **$k \neq 4$:** $\det \neq 0$, posto 2 = nº de variáveis, logo **SPD**.
- **$k = 4$:** a 2ª equação é $2x + 4y = 6$, o dobro da 1ª. Os postos de $A$ e de $[A \mid b]$ são ambos 1 < 2, logo **SPI**.
- Nunca é SI, porque o termo independente 6 também é o dobro de 3. Com $2x + 4y = 7$, seria SI.

```python
import numpy as np

for k in (1, 4):
    A = np.array([[1, 2], [2, k]])
    b = np.array([[3], [6]])
    print(k, np.linalg.matrix_rank(A), np.linalg.matrix_rank(np.hstack((A, b))))
```

Saída esperada:

```text
1 2 2
4 1 1
```

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Ciência de dados:** o posto de uma matriz de atributos revela colunas redundantes (multicolinearidade), que atrapalham regressões.
- **Engenharia e simulação:** grandes sistemas lineares (elementos finitos, circuitos) são resolvidos com variações de `solve`, nunca com inversas explícitas.
- **Computação gráfica:** inversas de matrizes de transformação desfazem rotações e escalas.
- **Qualidade de código científico:** tratar `LinAlgError` evita que um sistema singular derrube uma aplicação.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Classificar sistemas só pelo posto de $A$ | Comparar também com o posto de $[A \mid b]$ | Senão um SI vira SPI (célula 9) |
| `np.linalg.inv(A) @ b` | `np.linalg.solve(A, b)` | Mais rápido e estável |
| Testar `det(A) == 0` com floats | `np.isclose(det, 0)` ou o posto | `det` retorna valores como 4,999999999999999 |
| Entregar notebook sem executar | Executar do início ao fim (*Restart & Run All*) antes de entregar | O notebook da pasta não tem saídas |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Rouché-Capelli: postos iguais e = $n$ → SPD; iguais e < $n$ → SPI; diferentes → SI.
- `rref()` dá a forma escalonada reduzida; num SPD, a solução aparece na última coluna.
- `det` e `inv` exigem matriz quadrada; `inv` também exige $\det \neq 0$.
- Prefira `solve` a `inv @ b`.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Que erro o NumPy gera ao inverter $\begin{pmatrix} 2 & 2 \\ 3 & 3 \end{pmatrix}$? Por quê?
2. Um sistema com 3 variáveis tem $\operatorname{posto}(A) = \operatorname{posto}([A \mid b]) = 2$. Como se classifica?
3. Por que $\det$ de uma matriz $3 \times 1$ gera erro?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. `LinAlgError: Singular matrix`. As linhas são proporcionais, então $\det = 0$ e não há inversa.
2. SPI, com uma variável livre.
3. Porque o determinante só é definido para matrizes quadradas.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [NumPy — `linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [SymPy — matrizes (`rref`, `rank`)](https://docs.sympy.org/latest/modules/matrices/matrices.html)
- STEINBRUCH, W. *Álgebra Linear*. Saraiva, 2006 (bibliografia básica).
- Material da pasta: [notebook](Aula_8_%C3%81lgebra_Linear_Computacional.ipynb)

<br />

<p align="center"><a href="../aula13-09-09-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
