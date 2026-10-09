<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Integrais&amp;fontSize=40&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=MODELAGEM%20MATEM%C3%81TICA%20E%20COMPUTACIONAL%20%E2%80%94%20AULA%2010%20%E2%80%94%2020%2F08%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Retomada do Semestre, Integral Indefinida e Integral Definida" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=%E2%88%AB%20f%28x%29%20dx%20%3D%20F%28x%29%20%2B%20C;%E2%88%AB%20x%E1%B4%BA%20dx%20%3D%20x%E1%B4%BA%E2%81%BA%C2%B9%2F%28N%20%2B%201%29%20%2B%20C%2C%20N%20%E2%89%A0%20%E2%88%921;%E2%88%AB%E2%82%90%E1%B5%87%20f%28x%29%20dx%20%3D%20F%28b%29%20%E2%88%92%20F%28a%29;Gini%20%3D%202%20%E2%88%AB%E2%82%80%C2%B9%20%28x%20%E2%88%92%20L%28x%29%29%20dx" alt="∫ f(x) dx = F(x) + C. ∫ xᴺ dx = xᴺ⁺¹/(N + 1) + C, N ≠ −1. ∫ₐᵇ f(x) dx = F(b) − F(a). Gini = 2 ∫₀¹ (x − L(x)) dx." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-MMC-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: MMC" />
  <img src="https://img.shields.io/badge/Aula-10-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 10" />
  <img src="https://img.shields.io/badge/Data-20--08--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 20-08-2026" />
  <img src="https://img.shields.io/badge/Tema-Integrais-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Tema: Integrais" />
  <img src="https://img.shields.io/badge/Teorema-Fundamental%20do%20C%C3%A1lculo-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Teorema: Fundamental do Cálculo" />
  <img src="https://img.shields.io/badge/Aplica%C3%A7%C3%A3o-%C3%8Dndice%20de%20Gini-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Aplicação: Índice de Gini" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Modelagem Matemática e Computacional](../README.md) |
| Aula | 10 — 20/08/2026 |
| Título | Retomada do Semestre, Integral Indefinida e Integral Definida |
| Tema central | Revisão do 1º semestre e plano do 2º (integral e álgebra linear); integral indefinida como operação inversa da derivada, constante de integração e integrais imediatas; integral definida como área por somas de retângulos, Teorema Fundamental do Cálculo, áreas positivas e negativas; atividade do Índice de Gini e curva de Lorenz. |
| Tecnologias e ferramentas | Python 3, NumPy (verificações numéricas) |
| Docente (conforme material) | Prof. Igor Gimenes Cesca |
| Natureza do conteúdo | Anotações de aula com atividade em grupo |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`Aula 1 - Turma X.pdf`](Aula%201%20-%20Turma%20X.pdf) | Anotações da aula 1 do 2º semestre (3 páginas): o que foi aprendido (limites, derivadas), o que mudou na visão de matemática e os conteúdos do semestre (integral, álgebra linear) com aplicações (Gini, tomografia, sistemas de recomendação). |
| [`Aula 2 - Turma X.pdf`](Aula%202%20-%20Turma%20X.pdf) | Anotações da aula 2 (5 páginas): integral indefinida como inversa da derivada, tabela derivada–integral, constante de integração, derivadas de funções exponenciais e quatro exercícios resolvidos. |
| [`Aula 3 - Turma X.pdf`](Aula%203%20-%20Turma%20X.pdf) | Anotações da aula 3 (7 páginas): integral definida como área, somas de retângulos com bases decrescentes, Teorema Fundamental do Cálculo, três exemplos, áreas negativas e enunciado da atividade “Índice de Gini, Curva de Lorenz e Concentração de Renda”. |
| [`assets/curva-lorenz-gini.svg`](assets/curva-lorenz-gini.svg) | Figura original desta documentação: curva de Lorenz ajustada, dados da Tabela 1 e área do Índice de Gini. |
| [`assets/soma-riemann.svg`](assets/soma-riemann.svg) | Figura original desta documentação: somas de retângulos sob −x²/4 + 2x com bases 1 e 0,25. |

> [!NOTE]
> **Limitações da documentação.** As anotações combinam texto digitado, gráficos e resoluções manuscritas, lidos visualmente. A atividade do Índice de Gini exigia entrega manuscrita; a resolução apresentada na aula seguinte (pasta aula12) foi conferida por execução.

<br />

<h2 id="visao-geral">Visão geral</h2>

O 2º semestre abre com uma retrospectiva: o Cálculo permitiu estudar funções **fora do domínio** (limites), lidar com o **infinito** e calcular taxas de variação **em um único ponto** (derivadas). Os conteúdos anunciados para o semestre são:

| Tema | Ensino médio | FIAP | Aplicação citada |
| :--- | :--- | :--- | :--- |
| **Integral** | Áreas de figuras geométricas | Área de **qualquer** figura | Índice de Gini |
| **Álgebra linear** | — | Vetores, matrizes, determinantes, sistemas | Tomografia e ressonância (sistemas lineares), sistemas de recomendação (vetores) |

Esta pasta reúne as três primeiras aulas: a retomada, a **integral indefinida** (operação inversa da derivada) e a **integral definida** (área), com a atividade do Índice de Gini.

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Calcular integrais indefinidas imediatas e entender a constante $C$.
- Interpretar a integral definida como área (com sinal).
- Aproximar áreas por somas de retângulos.
- Aplicar o Teorema Fundamental do Cálculo.
- Modelar a desigualdade de renda com a curva de Lorenz e o Índice de Gini.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 09](../aula09-11-05-26/README.md): regras de derivação.
- Exponenciais e logaritmos ($e^x$, $\ln$).

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Integral indefinida

A integral é a **operação inversa da derivada**: $\int f(x)\,dx = F(x) + C$, em que $F'(x) = f(x)$. A constante $C \in \mathbb{R}$ indica que há **infinitas** primitivas. Por exemplo, $x^2 - 2$, $x^2 + 1$ e $x^2 + 10$ têm todas derivada $2x$.

| Derivada $f(x)$ | Integral $\int f(x)\,dx$ |
| :--- | :--- |
| $x^N$ ($N \neq -1$) | $\dfrac{x^{N+1}}{N + 1} + C$ |
| $k$ (constante) | $kx + C$ |
| $k \cdot f(x)$ | $k \int f(x)\,dx$ |
| $\cos x$ | $\operatorname{sen} x + C$ |
| $\operatorname{sen} x$ | $-\cos x + C$ |
| $e^x$ | $e^x + C$ |
| $n^x$ | $\dfrac{n^x}{\ln n} + C$, porque $(n^x)' = n^x \ln n$ |

### 2. Integral definida e somas de retângulos

A integral definida de $f$ em $[a, b]$ é a **área entre a função e o eixo horizontal**: a soma das áreas de **infinitos retângulos** de base $dx \to 0$ e altura $f(x)$.

<p align="center">
  <img src="assets/soma-riemann.svg" width="760" alt="Parábola −x²/4 + 2x entre 0 e 8 preenchida por retângulos: com base 1, a soma das áreas é 21,5; com base 0,25, é aproximadamente 21,34. O valor exato é 64/3, cerca de 21,333." />
</p>

*Figura 1 — As anotações mostram a mesma ideia com bases 2, 1, 0,5 e 0,01 (SVG original): quanto menor a base, mais a soma se aproxima da área exata.*

### 3. Teorema Fundamental do Cálculo

Se $f$ é contínua em $[a, b]$ e $g$ é uma primitiva de $f$:

$$\int_a^b f(x)\,dx = g(b) - g(a)$$

**Área com sinal:** se $f > 0$ em $[a, b]$, a integral é positiva; se $f < 0$, é negativa. Na física, a área negativa corresponde a um objeto se deslocando no sentido contrário.

| | Integral indefinida | Integral definida |
| :--- | :--- | :--- |
| Resultado | Uma **função** $F(x) + C$ | Um **número real** |

### 4. Curva de Lorenz e Índice de Gini (atividade)

- A **curva de Lorenz** $L(x)$, definida em $[0, 1]$, mostra a fração da renda ($y$) detida pelos $x$ mais pobres. O ponto $(0{,}4;\,0{,}12)$ significa que os 40% mais pobres detêm 12% da renda.
- A curva começa em $(0, 0)$, termina em $(1, 1)$ e tem concavidade para cima.
- Sem desigualdade, $L(x) = x$.
- O **Índice de Gini** (Corrado Gini, 1912, a partir da curva de Max Lorenz, 1905) mede a área entre $y = x$ e $L(x)$.
- Pelo enunciado, até 0,30 indica desigualdade moderada, e acima de 0,50, desigualdade extrema.

Na resolução apresentada na [aula seguinte](../aula12-04-09-26/README.md), o índice é calculado como o **dobro** dessa área, para variar de 0 a 1:

$$\text{Gini} = 2\int_0^1 \big(x - L(x)\big)\,dx$$

<p align="center">
  <img src="assets/curva-lorenz-gini.svg" width="720" alt="Gráfico com a reta de igualdade y = x tracejada e a curva de Lorenz ajustada L(x) = 0,7604·x^2,0926 abaixo dela, com a área entre as duas sombreada (cerca de 0,2541) e os seis pontos da tabela de renda acumulada. Gini ≈ 0,508, desigualdade extrema." />
</p>

*Figura 2 — Curva de Lorenz ajustada aos dados por quintis da Tabela 1, adaptada da PNAD Contínua (SVG original).*

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — integrais indefinidas resolvidas nas anotações

| Exercício | Resolução nas anotações |
| :--- | :--- |
| $\int (4x + 7)\,dx$ | $2x^2 + 7x + C$ |
| $\int (6x^5 - 8x^4 - 9x^3)\,dx$ | $x^6 - \frac{8}{5}x^5 - \frac{9}{4}x^4 + C$ |
| $\int \left(7x^{2/5} + 8x^{-4/5}\right)dx$ | $5x^{7/5} + 40x^{1/5} + C$ |
| $\int (\operatorname{sen} x - 2^x + 3e^x)\,dx$ | $-\cos x - \dfrac{2^x}{\ln 2} + 3e^x + C$ |

**Conferência:** derivando cada resultado, volta-se ao integrando. Por exemplo, $(5x^{7/5})' = 5 \cdot \frac{7}{5}x^{2/5} = 7x^{2/5}$.

### Exemplo intermediário — retângulos e Teorema Fundamental

```python
f = lambda x: -(x ** 2) / 4 + 2 * x            # mesma função do notebook da aula seguinte

def soma_riemann(f, a, b, base):
    """Soma das áreas de retângulos com altura no ponto médio de cada intervalo."""
    n = round((b - a) / base)
    return sum(f(a + (k + 0.5) * base) * base for k in range(n))

for base in (2, 1, 0.5, 0.01):
    print(f"base = {base:<5} -> área ≈ {soma_riemann(f, 0, 8, base):.6f}")

F = lambda x: -(x ** 3) / 12 + x ** 2          # primitiva: F'(x) = f(x)
print(f"Teorema Fundamental: F(8) − F(0) = {F(8) - F(0):.6f}  (= 64/3)")
```

Saída esperada:

```text
base = 2     -> área ≈ 22.000000
base = 1     -> área ≈ 21.500000
base = 0.5   -> área ≈ 21.375000
base = 0.01  -> área ≈ 21.333350
Teorema Fundamental: F(8) − F(0) = 21.333333  (= 64/3)
```

### Exemplo aplicado — integrais definidas e Gini

Exemplos 1 a 3 das anotações e a atividade do Gini:

```python
import math

def integral(f, a, b, n=100_000):
    h = (b - a) / n
    return sum(f(a + (k + 0.5) * h) for k in range(n)) * h

print("∫ x² de −1 a 1     =", round(integral(lambda x: x * x, -1, 1), 6), "(exato 2/3)")
print("∫ x de −2 a 2      =", round(integral(lambda x: x, -2, 2), 6) + 0.0, "(áreas +2 e −2 se cancelam)")
print("∫ sen x de 0 a π   =", round(integral(math.sin, 0, math.pi), 6))
print("∫ sen x de 0 a 3π/2 =", round(integral(math.sin, 0, 3 * math.pi / 2), 6))

# Índice de Gini = 2·∫₀¹ (x − L(x)) dx  (resolução das anotações da aula 4)
gini = lambda L: 2 * integral(lambda x: x - L(x), 0, 1)
print("Gini, L(x) = x²              =", round(gini(lambda x: x * x), 4))
print("Gini, L(x) = 0,7604·x^2,0926 =", round(gini(lambda x: 0.7604 * x ** 2.0926), 5))
```

Saída esperada:

```text
∫ x² de −1 a 1     = 0.666667 (exato 2/3)
∫ x de −2 a 2      = 0.0 (áreas +2 e −2 se cancelam)
∫ sen x de 0 a π   = 2.0
∫ sen x de 0 a 3π/2 = 1.0
Gini, L(x) = x²              = 0.3333
Gini, L(x) = 0,7604·x^2,0926 = 0.50825
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

### Exemplos da aula 3 (solução do material original, conferida acima)

| Integral | Desenvolvimento | Resultado |
| :--- | :--- | :---: |
| $\int_{-1}^{1} x^2\,dx$ | $\left[\frac{x^3}{3}\right]_{-1}^{1} = \frac{1}{3} - \left(-\frac{1}{3}\right)$ | $2/3$ |
| $\int_{-2}^{2} x\,dx$ | $\left[\frac{x^2}{2}\right]_{-2}^{2} = 2 - 2$ | 0 (área positiva cancela a negativa) |
| $\int_0^{3\pi/2} \operatorname{sen} x\,dx$ | $[-\cos x]_0^{3\pi/2} = 0 + 1$ | 1 (área 2 de 0 a π, menos 1 de π a 3π/2) |
| $\int_0^{\pi} \operatorname{sen} x\,dx$ | $-\cos \pi + \cos 0$ | 2 |

### Atividade do Índice de Gini (resolução da aula seguinte)

1. $\text{Área} = \int_0^1 (x - L(x))\,dx$ e $\text{Gini} = 2\int_0^1 (x - L(x))\,dx$.
2. Com $L(x) = x^2$: $2\left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = 2 \cdot \frac{1}{6} = \frac{1}{3} \approx 0{,}333$, desigualdade moderada.
3. Com $L(x) = 0{,}7604\,x^{2{,}0926}$: $2(0{,}2541227) \approx 0{,}508$. As anotações concluem "alta concentração".

> [!NOTE]
> **Observação sobre o ajuste da Tabela 1.** Uma curva de Lorenz deve passar por $(1, 1)$, mas o ajuste do material dá $L(1) = 0{,}7604$ (veja a Figura 2). Calculando o índice **diretamente dos dados** pela regra dos trapézios, sem ajuste, obtém-se Gini ≈ 0,492. A conclusão de alta desigualdade se mantém, mas o valor depende do método.

```python
import numpy as np

pop = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0])      # população acumulada (Tabela 1)
renda = np.array([0, 0.03, 0.10, 0.22, 0.42, 1.0])  # renda acumulada

area_lorenz = np.trapezoid(renda, pop)              # área sob a poligonal de Lorenz
print(f"área sob a curva (trapézios) = {area_lorenz:.3f}")
print(f"Gini direto dos dados = 1 − 2·área = {1 - 2 * area_lorenz:.3f}")
print(f"ajuste do material em x = 1: L(1) = {0.7604 * 1 ** 2.0926}  (uma curva de Lorenz deveria valer 1)")
```

Saída esperada:

```text
área sob a curva (trapézios) = 0.254
Gini direto dos dados = 1 − 2·área = 0.492
ajuste do material em x = 1: L(1) = 0.7604  (uma curva de Lorenz deveria valer 1)
```

**Exercício proposto para estudo:** calcule o Gini para $L(x) = x^3$ e compare com $L(x) = x^2$.

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

$2\int_0^1 (x - x^3)\,dx = 2\left(\frac{1}{2} - \frac{1}{4}\right) = 0{,}5$. É maior que $1/3$, porque $x^3$ fica mais abaixo da reta $y = x$, ou seja, a renda está mais concentrada.

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Economia e políticas públicas:** o Índice de Gini é o indicador padrão de desigualdade de renda (IBGE, Banco Mundial).
- **Engenharia:** trabalho, energia, volumes e cargas distribuídas são integrais.
- **Ciência de dados:** a área sob a curva ROC (AUC) é uma integral; a curva de Lorenz também mede concentração (por exemplo, a fatia das vendas vinda dos maiores clientes).
- **Física:** deslocamento como área sob a curva de velocidade, incluindo as áreas negativas.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Esquecer o $+ C$ na indefinida | Sempre escrever $+ C$ | Há infinitas primitivas |
| Somar áreas com sinal quando se quer a área geométrica | Separar os intervalos onde $f < 0$ e usar o módulo | $\int_{-2}^{2} x\,dx = 0$, mas a área total é 4 |
| Aplicar $x^{N+1}/(N+1)$ com $N = -1$ | Usar $\int x^{-1}dx = \ln\lvert x \rvert + C$ | A regra da potência não vale para $N = -1$ |
| Ajustar curvas sem checar as restrições do modelo | Verificar $L(0) = 0$ e $L(1) = 1$ | Ver a nota sobre o ajuste da Tabela 1 |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- $\int f\,dx = F + C$ com $F' = f$; tabela de integrais imediatas.
- Integral definida = área com sinal = limite das somas de retângulos.
- TFC: $\int_a^b f = F(b) - F(a)$.
- Gini $= 2\int_0^1 (x - L(x))\,dx$; $L = x^2 \Rightarrow 1/3$.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Calcule $\int (3x^2 + 2)\,dx$.
2. Calcule $\int_0^2 3x^2\,dx$.
3. Por que $\int_{-\pi}^{\pi} \operatorname{sen} x\,dx = 0$?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. $x^3 + 2x + C$.
2. $[x^3]_0^2 = 8$.
3. Porque $\operatorname{sen} x$ é ímpar: a área negativa em $[-\pi, 0]$ cancela a positiva em $[0, \pi]$.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- STEWART, J. *Cálculo*, v. 1, capítulos 4 e 5 (arquivos na [aula 02](../aula02-04-03-26/README.md)).
- [NumPy — `trapezoid`](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html)
- Materiais da pasta: [Aula 1](Aula%201%20-%20Turma%20X.pdf) · [Aula 2](Aula%202%20-%20Turma%20X.pdf) · [Aula 3](Aula%203%20-%20Turma%20X.pdf)

<br />

<p align="center"><a href="../aula09-11-05-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula11-25-08-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
