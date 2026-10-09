<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Derivada%20em%20um%20Ponto&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=MODELAGEM%20MATEM%C3%81TICA%20E%20COMPUTACIONAL%20%E2%80%94%20AULA%2008%20%E2%80%94%2022%2F04%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Número de Euler e Derivada em um Ponto" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=lim%20n%E2%86%92%E2%88%9E%20%281%20%2B%201%2Fn%29%E2%81%BF%20%3D%20e%20%E2%89%88%202%2C71828;Velocidade%20m%C3%A9dia%3A%20%CE%94s%2F%CE%94t;f%27%28a%29%20%3D%20lim%20h%E2%86%920%20%5Bf%28a%20%2B%20h%29%20%E2%88%92%20f%28a%29%5D%2Fh;S%28t%29%20%3D%20t%C2%B2%3A%20v%282%2C5%29%20%3D%205%20m%2Fs" alt="lim n→∞ (1 + 1/n)ⁿ = e ≈ 2,71828. Velocidade média: Δs/Δt. f'(a) = lim h→0 [f(a + h) − f(a)]/h. S(t) = t²: v(2,5) = 5 m/s." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-MMC-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: MMC" />
  <img src="https://img.shields.io/badge/Aula-08-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 08" />
  <img src="https://img.shields.io/badge/Data-22--04--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 22-04-2026" />
  <img src="https://img.shields.io/badge/Tema-Derivada-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Tema: Derivada" />
  <img src="https://img.shields.io/badge/Constante-N%C3%BAmero%20de%20Euler-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Constante: Número de Euler" />
  <img src="https://img.shields.io/badge/Lista-Lista%206-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Lista: Lista 6" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Modelagem Matemática e Computacional](../README.md) |
| Aula | 08 — 22/04/2026 |
| Título | Número de Euler e Derivada em um Ponto |
| Tema central | Resolução da atividade de finanças (capitalização contínua e o limite que define e), derivada como taxa de variação instantânea, velocidade média e instantânea de S(t) = t², notação f'(a) e df/dx, definição da derivada por limite e exercícios com x² e x³ − 3x; Lista 6. |
| Tecnologias e ferramentas | Python 3 (verificações numéricas) |
| Docente (conforme material) | Prof. Igor Gimenes Cesca |
| Natureza do conteúdo | Anotações de aula e lista de exercícios (referências ao Stewart) |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`Aula 7 - Turma X.pdf`](Aula%207%20-%20Turma%20X.pdf) | Anotações da aula 7 (7 páginas): resolução da atividade de finanças, tabela de (1 + 1/n)ⁿ, motivação da derivada com velocidade média e instantânea, notação, definição e exercícios com x² e x³ − 3x. |
| [`Lista 6.pdf`](Lista%206.pdf) | Lista 6 (1 página): exercícios da seção 2.7 do Stewart (derivada em um ponto), 7ª e 8ª edições. |

> [!NOTE]
> **Limitações da documentação.** As anotações combinam texto digitado e cálculos manuscritos, lidos visualmente. A Lista 6 apenas indica exercícios do Stewart (seção 2.7). Os resultados foram conferidos numericamente; um deslize manuscrito e um efeito de arredondamento na tabela de e estão comentados.

<br />

<h2 id="visao-geral">Visão geral</h2>

A aula fecha a atividade de finanças da [aula 07](../aula07-15-04-26/README.md), mostrando numericamente que $\left(1 + \frac{1}{n}\right)^n$ se aproxima de **$e \approx 2{,}71828$**, o número de Euler. Em seguida, inaugura o segundo grande tema do Cálculo: a **derivada**, a taxa de variação **instantânea**.

| Ensino médio | FIAP (Cálculo) |
| :--- | :--- |
| Taxa de variação com **dois** valores (dois pontos) | Taxa de variação com **um único** valor (um ponto) |
| Velocidade média $\Delta s / \Delta t$ | Velocidade instantânea: $\Delta t \to 0$ |

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Reconhecer $e$ como o limite $\lim_{n \to \infty}(1 + 1/n)^n$ e usar $\lim_{n \to \infty}(1 + a/n)^n = e^a$.
- Diferenciar taxa de variação média e instantânea.
- Usar as notações $f'(a)$ e $\frac{df}{dx}(a)$.
- Calcular derivadas em um ponto pela definição.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 04](../aula04-20-03-26/README.md): limites com indeterminação $0/0$.
- Produtos notáveis: $(a + h)^2$ e $(a + h)^3$.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. O número de Euler

$$\lim_{n \to \infty}\left(1 + \frac{1}{n}\right)^n = e \approx 2{,}71828 \qquad \lim_{n \to \infty}\left(1 + \frac{a}{n}\right)^n = e^a$$

O segundo limite fundamenta a capitalização contínua: $M = C\left[\lim_{n \to \infty}\left(1 + \frac{i}{n}\right)^n\right]^t = Ce^{it}$.

### 2. Taxas de variação conhecidas

Velocidade ($\Delta s/\Delta t$, em km/h ou m/s), aceleração ($\Delta v/\Delta t$, em m/s²) e coeficiente angular de uma reta ($\Delta y/\Delta x$). Todas são razões de variações.

### 3. Definição da derivada

**Notação:** $f'(a)$ ("$f$ linha de $a$") ou $\dfrac{df}{dx}(a)$ ("derivada de $f$ em $a$ na variável $x$").

$$f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{(a + h) - a} = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$$

É a taxa média num intervalo $[a, a + h]$ que **encolhe até um ponto**. A substituição direta daria $0/0$: por isso a derivada é um limite.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart LR
    A["Taxa média<br/>Δy/Δx em [a, a+h]"] -->|"h → 0"| B["Taxa instantânea<br/>f'(a)"]
    B --> C["Inclinação da<br/>reta tangente em a"]
```

*Figura 1 — Da taxa média à derivada. A interpretação geométrica vem na [aula 09](../aula09-11-05-26/README.md).*

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — a tabela de $e$

```python
import math

for n in (1, 2, 10, 100, 10_000, 1_000_000):
    print(f"n = {n:>9,}: (1 + 1/n)^n = {(1 + 1 / n) ** n:.9f}".replace(",", "."))
print(f"e = {math.e:.9f}")

# n enorme: 1 + 1/n perde dígitos no ponto flutuante e o resultado "passa" de e
for n in (10**9, 10**10, 10**12):
    ingenuo = (1 + 1 / n) ** n
    estavel = math.exp(n * math.log1p(1 / n))       # log1p(x) calcula ln(1 + x) sem perder precisão
    print(f"n = 10^{len(str(n)) - 1}: ingênuo = {ingenuo:.9f} {'> e!' if ingenuo > math.e else ''} | estável = {estavel:.9f}")
```

Saída esperada:

```text
n =         1: (1 + 1/n)^n = 2.000000000
n =         2: (1 + 1/n)^n = 2.250000000
n =        10: (1 + 1/n)^n = 2.593742460
n =       100: (1 + 1/n)^n = 2.704813829
n =    10.000: (1 + 1/n)^n = 2.718145927
n = 1.000.000: (1 + 1/n)^n = 2.718280469
e = 2.718281828
n = 10^9: ingênuo = 2.718282052 > e! | estável = 2.718281827
n = 10^10: ingênuo = 2.718282053 > e! | estável = 2.718281828
n = 10^12: ingênuo = 2.718523496 > e! | estável = 2.718281828
```

> [!NOTE]
> A tabela das anotações traz, para $n = 10^9$ e $10^{10}$, os valores 2,718282031 e 2,718282053, **maiores** que $e$. Isso é impossível em teoria, porque $(1 + 1/n)^n$ cresce e nunca ultrapassa $e$. A causa é o **erro de arredondamento em ponto flutuante**: para $n$ enorme, $1 + 1/n$ perde dígitos significativos. A última parte da saída reproduz o efeito e mostra a forma estável com `math.log1p`.

### Exemplo intermediário — da velocidade média à instantânea (problema da aula)

> Um móvel parte do repouso com $S(t) = t^2$. Calcule a velocidade média entre 2,5 s e 10 s e a velocidade no instante 2,5 s.

- **Média:** $\dfrac{10^2 - 2{,}5^2}{10 - 2{,}5} = \dfrac{93{,}75}{7{,}5} = 12{,}5$ m/s.
- **Instantânea:** $\lim_{h \to 0} \dfrac{(2{,}5 + h)^2 - 2{,}5^2}{h} = \lim_{h \to 0} \dfrac{5h + h^2}{h} = \lim_{h \to 0} (5 + h) = 5$ m/s.

```python
S = lambda t: t ** 2                               # função horária S(t) = t²

print("velocidade média entre 2,5 s e 10 s:", (S(10) - S(2.5)) / (10 - 2.5), "m/s")
for h in (1, 0.1, 0.001, 0.00001):                 # intervalo encolhendo: h → 0
    print(f"h = {h:<8} taxa média em [2,5; 2,5 + h] = {(S(2.5 + h) - S(2.5)) / h:.5f}")

def derivada(f, a, h=1e-6):
    """f'(a) ≈ [f(a + h) − f(a − h)] / 2h (diferença central)."""
    return round((f(a + h) - f(a - h)) / (2 * h), 4)

f = lambda x: x ** 3 - 3 * x
print("f(x) = x² : f'(1) =", derivada(lambda x: x ** 2, 1), "| f'(−2) =", derivada(lambda x: x ** 2, -2))
print("f(x) = x³ − 3x : f'(1) =", derivada(f, 1), "| f'(0) =", derivada(f, 0))
```

Saída esperada:

```text
velocidade média entre 2,5 s e 10 s: 12.5 m/s
h = 1        taxa média em [2,5; 2,5 + h] = 6.00000
h = 0.1      taxa média em [2,5; 2,5 + h] = 5.10000
h = 0.001    taxa média em [2,5; 2,5 + h] = 5.00100
h = 1e-05    taxa média em [2,5; 2,5 + h] = 5.00001
f(x) = x² : f'(1) = 2.0 | f'(−2) = -4.0
f(x) = x³ − 3x : f'(1) = 0.0 | f'(0) = -3.0
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

Exercícios resolvidos nas anotações (**solução do material original**, conferida numericamente acima):

| Função | Ponto | Desenvolvimento | $f'(a)$ |
| :--- | :---: | :--- | :---: |
| $f(x) = x^2$ | $a = 1$ | $\dfrac{(1 + h)^2 - 1}{h} = 2 + h$ | 2 |
| $f(x) = x^2$ | $a = -2$ | ver nota abaixo | $-4$ |
| $f(x) = x^3 - 3x$ | $a = 1$ | $\dfrac{3h^2 + h^3}{h} = 3h + h^2$ | 0 |
| $f(x) = x^3 - 3x$ | $a = 0$ | $\dfrac{h^3 - 3h}{h} = h^2 - 3$ | $-3$ |

> [!NOTE]
> No item b ($f'(-2)$ para $f(x) = x^2$), o desenvolvimento manuscrito usa $f(2 + h) - f(2)$ e chega a 4, que é $f'(2)$. Para $a = -2$: $\dfrac{(-2 + h)^2 - 4}{h} = \dfrac{-4h + h^2}{h} = -4 + h \to -4$, valor confirmado pela execução acima.

A **Lista 6** indica, na seção 2.7 do Stewart, os exercícios 13–16, 27, 28, 31–36, 43 e 44 da 8ª edição, ou 13–16, 23–25, 27–32, 39 e 40 da 7ª.

**Exercício proposto para estudo:** pela definição, calcule $f'(3)$ para $f(x) = 2x^2 - x$.

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

$f(3 + h) = 2(9 + 6h + h^2) - 3 - h = 15 + 11h + 2h^2$ e $f(3) = 15$. Então:

$$f'(3) = \lim_{h \to 0} \frac{11h + 2h^2}{h} = \lim_{h \to 0} (11 + 2h) = 11$$

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Física e engenharia:** velocidade, aceleração e vazão são derivadas.
- **Economia:** custo e receita **marginais** são derivadas do custo e da receita totais.
- **Aprendizado de máquina:** o gradiente descendente usa derivadas para ajustar parâmetros. A aproximação numérica do exemplo é a mesma ideia usada para verificar gradientes.
- **Computação científica:** o cuidado com o ponto flutuante (nota sobre $e$) é essencial em qualquer cálculo numérico.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Substituir $h = 0$ antes de simplificar | Expandir, fatorar $h$ e cancelar | Senão dá $0/0$ |
| Trocar o ponto durante a conta | Reescrever $a$ em cada linha | Evita o deslize do item b |
| Usar $h$ muito pequeno sem critério na aproximação numérica | Diferença central e $h \approx 10^{-6}$ | Equilibra truncamento e arredondamento |
| Calcular $(1 + 1/n)^n$ ingenuamente com $n$ enorme | `math.exp(n * math.log1p(1/n))` | Evita resultados maiores que $e$ |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- $e = \lim_{n \to \infty}(1 + 1/n)^n \approx 2{,}71828$; capitalização contínua: $Ce^{it}$.
- Derivada = taxa de variação instantânea = limite da taxa média quando $h \to 0$.
- $f'(a) = \lim_{h \to 0} \dfrac{f(a + h) - f(a)}{h}$.
- $S(t) = t^2$: $v(2{,}5) = 5$ m/s.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Qual a diferença entre velocidade média e instantânea?
2. Pela definição, quanto vale $f'(4)$ para $f(x) = x^2$?
3. Quanto vale $\lim_{n \to \infty}(1 + 2/n)^n$?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. A média usa dois instantes; a instantânea, um único instante, como limite com $\Delta t \to 0$.
2. $\dfrac{(4 + h)^2 - 16}{h} = 8 + h \to 8$.
3. $e^2 \approx 7{,}389$.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- STEWART, J. *Cálculo*, v. 1, seção 2.7 (arquivos na [aula 02](../aula02-04-03-26/README.md)).
- [Python — `math.log1p`](https://docs.python.org/pt-br/3/library/math.html#math.log1p)
- Materiais da pasta: [Aula 7](Aula%207%20-%20Turma%20X.pdf) · [Lista 6](Lista%206.pdf)

<br />

<p align="center"><a href="../aula07-15-04-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula09-11-05-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
