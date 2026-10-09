<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Limites%20no%20Infinito&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=MODELAGEM%20MATEM%C3%81TICA%20E%20COMPUTACIONAL%20%E2%80%94%20AULA%2006%20%E2%80%94%2002%2F04%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Limites Infinitos, Limites no Infinito e Assíntotas" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=lim%20x%E2%86%922%E2%81%BA%201%2F%28x%20%E2%88%92%202%29%20%3D%20%2B%E2%88%9E;lim%20x%E2%86%92%E2%88%9E%20a%2Fx%E1%B5%96%20%3D%200%20%28p%20%3E%200%29;Divida%20pela%20maior%20pot%C3%AAncia%20de%20x;lim%20x%E2%86%92%E2%88%9E%20e%CB%A3%20%3D%20%E2%88%9E" alt="lim x→2⁺ 1/(x − 2) = +∞. lim x→∞ a/xᵖ = 0 (p > 0). Divida pela maior potência de x. lim x→∞ eˣ = ∞." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-MMC-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: MMC" />
  <img src="https://img.shields.io/badge/Aula-06-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 06" />
  <img src="https://img.shields.io/badge/Data-02--04--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 02-04-2026" />
  <img src="https://img.shields.io/badge/Tema-Limites%20no%20infinito-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Tema: Limites no infinito" />
  <img src="https://img.shields.io/badge/Conceito-Ass%C3%ADntotas-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Conceito: Assíntotas" />
  <img src="https://img.shields.io/badge/Lista-Lista%204-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Lista: Lista 4" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Modelagem Matemática e Computacional](../README.md) |
| Aula | 06 — 02/04/2026 |
| Título | Limites Infinitos, Limites no Infinito e Assíntotas |
| Tema central | Limites infinitos e assíntotas verticais (1/x, 1/(x − 2), produto de limites), limites no infinito e assíntotas horizontais (regra a/xᵖ → 0, divisão pela maior potência), limites infinitos no infinito (x², x − 1, eˣ, 2ˣ) e o número de Euler. |
| Tecnologias e ferramentas | Python 3 (verificações) |
| Docente (conforme material) | Prof. Igor Gimenes Cesca |
| Natureza do conteúdo | Anotações de aula e lista de exercícios (referências ao Stewart) |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`Aula 5 - Turma X.pdf`](Aula%205%20-%20Turma%20X.pdf) | Anotações da aula 5 (6 páginas): hotel de infinitos quartos e macaco na máquina de escrever, limites infinitos (1/x, 1/(x − 2), exemplos do Stewart p. 77 e 80), limites no infinito com tabelas e fórmula a/xᵖ, exemplos das p. 109 e 119, limites infinitos no infinito e o número e. |
| [`Lista 4.pdf`](Lista%204.pdf) | Lista 4 (1 página): exercícios das seções 2.2, 2.3 e 2.6 do Stewart, 7ª e 8ª edições. |
| [`assets/assintotas.svg`](assets/assintotas.svg) | Figura original desta documentação: 1/(x − 2) com assíntota vertical e (x² − 1)/(x² + 1) com assíntota horizontal. |

> [!NOTE]
> **Limitações da documentação.** As anotações contêm cálculos e gráficos manuscritos, lidos visualmente. A Lista 4 apenas indica exercícios do Stewart (seções 2.2, 2.3 e 2.6). Os limites resolvidos foram conferidos por cálculo e numericamente.

<br />

<h2 id="visao-geral">Visão geral</h2>

Esta aula completa o estudo de limites com o **infinito** nos dois papéis possíveis:

| Tipo | Notação | Ideia | Gráfico |
| :--- | :--- | :--- | :--- |
| Limite infinito | $\lim_{x \to a} f(x) = \infty$ | $x$ perto de $a$, $f$ explode | Assíntota **vertical** $x = a$ |
| Limite no infinito | $\lim_{x \to \infty} f(x) = L$ | $x$ cresce sem fim, $f$ se estabiliza | Assíntota **horizontal** $y = L$ |
| Limite infinito no infinito | $\lim_{x \to \infty} f(x) = \infty$ | Ambos crescem sem fim | Sem assíntota horizontal |

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Calcular limites infinitos e identificar assíntotas verticais.
- Calcular limites no infinito de funções racionais pela maior potência de $x$.
- Usar a regra $\lim_{x \to \pm\infty} a/x^p = 0$.
- Reconhecer funções que crescem sem limite ($x^2$, $e^x$, $2^x$).

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 05](../aula05-30-03-26/README.md): limites laterais e $1/x$.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Limites infinitos

$f(x) \to \pm\infty$ quando $x \to a$. O sinal depende do lado da aproximação:

$$\lim_{x \to 2^+} \frac{1}{x - 2} = +\infty \qquad \lim_{x \to 2^-} \frac{1}{x - 2} = -\infty$$

Quando a substituição dá **número ≠ 0 dividido por 0** e não há o que simplificar, separa-se o produto. Por exemplo (Stewart p. 77, nas anotações):

$$\lim_{x \to 3^+} \frac{2x}{x - 3} = \left(\lim_{x \to 3^+} 2x\right)\left(\lim_{x \to 3^+} \frac{1}{x - 3}\right) = 6 \cdot (+\infty) = +\infty$$

### 2. Limites no infinito

**Fórmula das anotações:** para $p > 0$ e $a \in \mathbb{R}$,

$$\lim_{x \to \pm\infty} \frac{a}{x^p} = 0$$

**Técnica para funções racionais:** colocar em evidência (ou dividir por) a **maior potência** de $x$:

$$\lim_{x \to \infty} \frac{x^2 - 1}{x^2 + 1} = \lim_{x \to \infty} \frac{x^2\left(1 - \frac{1}{x^2}\right)}{x^2\left(1 + \frac{1}{x^2}\right)} = \frac{1 - 0}{1 + 0} = 1$$

<p align="center">
  <img src="assets/assintotas.svg" width="720" alt="À esquerda, o gráfico de 1/(x − 2) com assíntota vertical tracejada em x = 2: sobe a +∞ pela direita e desce a −∞ pela esquerda. À direita, (x² − 1)/(x² + 1) parte de −1 em x = 0 e se aproxima da assíntota horizontal tracejada y = 1." />
</p>

*Figura 1 — Assíntota vertical (limite infinito) e horizontal (limite no infinito) nos exemplos da aula (SVG original).*

### 3. Limites infinitos no infinito e o número $e$

Para $y = x^2$, $y = x - 1$, $y = e^x$ e $y = 2^x$, $\lim_{x \to \infty} f(x) = \infty$. As anotações terminam apresentando o número de Euler, $e \approx 2{,}7\ldots$, retomado na [aula 08](../aula08-22-04-26/README.md).

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — exemplos resolvidos nas anotações

| Limite (fonte) | Desenvolvimento | Resultado |
| :--- | :--- | :---: |
| $\lim_{x \to 2^-} \dfrac{x^2 - 2x}{x^2 - 4x + 4}$ (p. 80, ex. 40) | $\dfrac{x(x - 2)}{(x - 2)^2} = \dfrac{x}{x - 2}$; $2 \cdot (-\infty)$ | $-\infty$ |
| $\lim_{x \to \infty} \dfrac{x^2 - 1}{x^2 + 1}$ (p. 109) | Maior potência $x^2$ | 1 |
| $\lim_{x \to \infty} \dfrac{3x + 5}{x - 4}$ (p. 119, ex. 16) | $\dfrac{x(3 + 5/x)}{x(1 - 4/x)}$ | 3 |
| $\lim_{x \to -\infty} \dfrac{1 - x - x^2}{2x^2 - 7}$ (p. 119, ex. 17) | $\dfrac{x^2(1/x^2 - 1/x - 1)}{x^2(2 - 7/x^2)} = \dfrac{-1}{2}$ | $-1/2$ |

### Exemplo aplicado — conferência numérica

```python
import math

def tabela(f, xs):
    return [round(f(x), 6) for x in xs]

grandes = [10, 1_000, 1_000_000]
print("1/x                    ->", tabela(lambda x: 1 / x, grandes))
print("(x² − 1)/(x² + 1)      ->", tabela(lambda x: (x*x - 1) / (x*x + 1), [1, 10, 50, 100, 10_000]))
print("(3x + 5)/(x − 4)       ->", tabela(lambda x: (3*x + 5) / (x - 4), grandes))
print("(1 − x − x²)/(2x² − 7) ->", tabela(lambda x: (1 - x - x*x) / (2*x*x - 7), [-10, -1_000, -1_000_000]))
print("e^x                    ->", [f"{math.exp(x):.3g}" for x in (1, 10, 100)])

# limites infinitos: lados de x = 2 em 1/(x − 2) e x/(x − 2) (ex. 40, p. 80)
for h in (0.1, 0.001):
    print(f"x = 2 ± {h}: 1/(x−2) = {1 / h:+.0f} e {-1 / h:+.0f}   x/(x−2) à esquerda = {(2 - h) / (-h):+.1f}")
```

Saída esperada:

```text
1/x                    -> [0.1, 0.001, 1e-06]
(x² − 1)/(x² + 1)      -> [0.0, 0.980198, 0.9992, 0.9998, 1.0]
(3x + 5)/(x − 4)       -> [5.833333, 3.017068, 3.000017]
(1 − x − x²)/(2x² − 7) -> [-0.46114, -0.499501, -0.5]
e^x                    -> ['2.72', '2.2e+04', '2.69e+43']
x = 2 ± 0.1: 1/(x−2) = +10 e -10   x/(x−2) à esquerda = -19.0
x = 2 ± 0.001: 1/(x−2) = +1000 e -1000   x/(x−2) à esquerda = -1999.0
```

Os valores confirmam a tabela: 1, 3 e $-0{,}5$ como limites no infinito; $e^x$ crescendo sem parar; e $x/(x - 2)$ indo a $-\infty$ pela esquerda de 2.

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

A **Lista 4** indica exercícios do Stewart:

| Edição | Seção 2.2 | Seção 2.3 | Seção 2.6 |
| :--- | :--- | :--- | :--- |
| 8ª | 3, 8, 9, 31–34, 40–45 | 13, 14 | 1, 3–10, 13–26 |
| 7ª | 3, 8, 9, 29–31, 36–39 | 13, 14 | 1, 3–10, 13–26 |

**Exercício proposto para estudo:** calcule $\lim_{x \to \infty} \dfrac{5x^3 - 2x}{2x^3 + x^2 + 1}$ e $\lim_{x \to \infty} \dfrac{x + 1}{x^2}$.

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

1. Dividindo por $x^3$: $\dfrac{5 - 2/x^2}{2 + 1/x + 1/x^3} \to \dfrac{5}{2}$. Com graus iguais, o limite é a razão dos coeficientes líderes.
2. Dividindo por $x^2$: $\dfrac{1/x + 1/x^2}{1} \to 0$. Quando o grau do numerador é menor, o limite é 0.

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Comportamento de longo prazo:** custo médio, receita acumulada e saturação de mercado são limites no infinito ([aula 07](../aula07-15-04-26/README.md)).
- **Complexidade de algoritmos:** comparar o crescimento de funções ($x^2$ × $2^x$) quando $n \to \infty$ é a base da notação Big-O.
- **Estabilidade numérica:** assíntotas verticais indicam pontos em que uma fórmula gera valores enormes ou divisões por zero.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Tratar $\infty$ como número ($\infty - \infty = 0$) | Reescrever a expressão antes de substituir | $\infty - \infty$ e $\infty/\infty$ são indeterminações |
| Ignorar o sinal em limites infinitos | Analisar o sinal de cada fator perto de $a$ | Ex. 40: $2 \cdot (-\infty) = -\infty$ |
| Dividir pela potência errada | Usar a **maior** potência do denominador | Garante termos que vão a 0 |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Limite infinito ($x \to a$, $f \to \infty$): assíntota vertical.
- Limite no infinito ($x \to \infty$, $f \to L$): assíntota horizontal $y = L$.
- $a/x^p \to 0$ para $p > 0$.
- Racionais: graus iguais → razão dos líderes; grau do numerador menor → 0; maior → $\pm\infty$.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Qual a assíntota horizontal de $f(x) = \dfrac{4x + 1}{2x - 3}$?
2. Qual a assíntota vertical da mesma função?
3. Quanto vale $\lim_{x \to \infty} 7/x^3$?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. $y = 4/2 = 2$.
2. $x = 3/2$, onde o denominador se anula e o numerador não.
3. 0.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- STEWART, J. *Cálculo*, v. 1, seções 2.2, 2.3 e 2.6 (arquivos na [aula 02](../aula02-04-03-26/README.md)).
- Materiais da pasta: [Aula 5](Aula%205%20-%20Turma%20X.pdf) · [Lista 4](Lista%204.pdf)

<br />

<p align="center"><a href="../aula05-30-03-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula07-15-04-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
