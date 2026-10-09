<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Limites%20Laterais&amp;fontSize=40&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=MODELAGEM%20MATEM%C3%81TICA%20E%20COMPUTACIONAL%20%E2%80%94%20AULA%2005%20%E2%80%94%2030%2F03%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Limites Laterais e Limites Infinitos" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=x%E2%86%92a%E2%81%BB%20%28esquerda%29%20e%20x%E2%86%92a%E2%81%BA%20%28direita%29;Laterais%20diferentes%3A%20o%20limite%20n%C3%A3o%20existe;lim%20x%E2%86%920%E2%81%BA%201%2Fx%20%3D%20%2B%E2%88%9E;Hotel%20de%20infinitos%20quartos" alt="x→a⁻ (esquerda) e x→a⁺ (direita). Laterais diferentes: o limite não existe. lim x→0⁺ 1/x = +∞. Hotel de infinitos quartos." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-MMC-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: MMC" />
  <img src="https://img.shields.io/badge/Aula-05-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 05" />
  <img src="https://img.shields.io/badge/Data-30--03--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 30-03-2026" />
  <img src="https://img.shields.io/badge/Tema-Limites%20laterais-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Tema: Limites laterais" />
  <img src="https://img.shields.io/badge/Extens%C3%A3o-Limites%20infinitos-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Extensão: Limites infinitos" />
  <img src="https://img.shields.io/badge/Lista-Lista%203-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Lista: Lista 3" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Modelagem Matemática e Computacional](../README.md) |
| Aula | 05 — 30/03/2026 |
| Título | Limites Laterais e Limites Infinitos |
| Tema central | Limites pela esquerda e pela direita, existência do limite, funções definidas por partes (alíquota de imposto, exercícios do Stewart), |x|/x, e introdução aos limites infinitos com 1/x; histórias do hotel de infinitos quartos e do macaco na máquina de escrever. |
| Tecnologias e ferramentas | Python 3 (verificações) |
| Docente (conforme material) | Prof. Igor Gimenes Cesca |
| Natureza do conteúdo | Anotações de aula e lista de exercícios (referências ao Stewart) |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`Aula 4 - Turma X.pdf`](Aula%204%20-%20Turma%20X.pdf) | Anotações da aula 4 (5 páginas): limites laterais com o exemplo da alíquota de imposto, exemplos gráficos, funções por partes (Stewart p. 86 e 88), |x|/x e início dos limites infinitos (1/x). |
| [`Lista 3.pdf`](Lista%203.pdf) | Lista 3 (1 página): exercícios das seções 2.2 e 2.3 do Stewart sobre limites laterais, 7ª e 8ª edições. |
| [`assets/limites-laterais.svg`](assets/limites-laterais.svg) | Figura original desta documentação: gráfico da função por partes g(x) do exercício 52 com limites laterais em x = 1 e x = 2. |

> [!NOTE]
> **Limitações da documentação.** As anotações contêm gráficos e cálculos manuscritos, lidos visualmente. A Lista 3 apenas indica exercícios do livro de Stewart. Os exemplos resolvidos nas anotações foram conferidos por cálculo.

<br />

<h2 id="visao-geral">Visão geral</h2>

Na [aula 04](../aula04-20-03-26/README.md), $x$ se aproximava de $a$ "por todos os lados". Agora as aproximações são separadas: **pela esquerda** ($x \to a^-$, valores menores que $a$) e **pela direita** ($x \to a^+$, valores maiores). Funções definidas **por partes**, comuns em tarifas e impostos, podem ter comportamentos diferentes em cada lado. O limite só existe quando **os dois lados concordam**.

A aula termina introduzindo os **limites infinitos**, em que a função cresce sem parar perto de um ponto. Ilustram a ideia duas histórias: o **hotel de infinitos quartos** e o **macaco na máquina de escrever**.

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Calcular limites laterais em funções por partes e a partir de gráficos.
- Decidir se um limite existe comparando os limites laterais.
- Diferenciar limite e valor da função num ponto de descontinuidade.
- Reconhecer o comportamento de $1/x$ perto de zero.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 04](../aula04-20-03-26/README.md): definição de limite e substituição direta.
- Módulo: $|x| = x$ se $x \geq 0$ e $|x| = -x$ se $x < 0$.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Limites laterais e existência

$$\lim_{x \to a} f(x) = L \iff \lim_{x \to a^-} f(x) = L \;\text{ e }\; \lim_{x \to a^+} f(x) = L$$

Se os limites laterais forem **diferentes**, o limite (bilateral) **não existe** ($\nexists$).

**Exemplo motivador das anotações:** uma alíquota de imposto que vale 0% até uma renda de \$ 35.000 e 7% acima disso. Aproximando-se de 35.000 pela esquerda, a alíquota é 0%; pela direita, 7%. Logo, $\lim_{x \to 35000} f(x)$ não existe.

<p align="center">
  <img src="assets/limites-laterais.svg" width="720" alt="Função por partes g: reta y = x até x = 1 com círculo vazio em (1, 1); ponto cheio isolado em (1, 3); parábola 2 − x² entre 1 e 2, com ponto cheio em (2, −2); reta x − 3 após 2, com círculo vazio em (2, −1). Em x = 1 os dois lados tendem a 1, mas g(1) = 3; em x = 2 os lados tendem a −2 e −1, e o limite não existe." />
</p>

*Figura 1 — Exercício 52 resolvido nas anotações (SVG original): em $x = 1$, o limite existe mas difere do valor da função; em $x = 2$, o limite não existe.*

### 2. Limites infinitos (introdução)

Quando $x \to a$ e $f(x)$ assume valores **arbitrariamente grandes** em módulo, diz-se que a função tende ao infinito:

$$\lim_{x \to 0^-} \frac{1}{x} = -\infty \qquad \lim_{x \to 0^+} \frac{1}{x} = +\infty$$

Mesmo escrevendo "$= \infty$", o limite **não existe** como número, porque a função não se aproxima de um valor único. O tema continua na [aula 06](../aula06-02-04-26/README.md).

**Hotel de infinitos quartos (Hilbert):** um hotel lotado com infinitos quartos ainda acomoda um novo hóspede, bastando cada hóspede mudar do quarto $n$ para o $n + 1$. O infinito não se comporta como um número grande comum.

**Macaco na máquina de escrever:** digitando teclas ao acaso por um tempo infinito, o macaco acabaria escrevendo uma obra de Shakespeare. Eventos de probabilidade minúscula se tornam inevitáveis no infinito.

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — exemplos resolvidos nas anotações

| Exemplo | Esquerda | Direita | Limite |
| :--- | :---: | :---: | :---: |
| Gráfico da aula, $x \to -5$ | 5 | 1 | $\nexists$ |
| Gráfico da aula, $x \to 4$ ($f(4) = 2$) | 3 | 3 | 3 |
| p. 86, ex. 9: $f(x) = \sqrt{x - 4}$ ($x > 4$) e $8 - 2x$ ($x < 4$), em $x \to 4$ | $8 - 8 = 0$ | $\sqrt{0} = 0$ | **0** |
| p. 86, ex. 8: $\dfrac{\lvert x \rvert}{x}$, em $x \to 0$ | $-1$ | $1$ | $\nexists$ |
| p. 88, ex. 44: $\dfrac{2 - \lvert x \rvert}{2 + x}$, em $x \to -2$ | Perto de $-2$, $\lvert x \rvert = -x$: $\dfrac{2 + x}{2 + x} = 1$ | 1 | **1** |
| p. 88, ex. 40: $\left(\dfrac{1}{x} - \dfrac{1}{\lvert x \rvert}\right)$, em $x \to 0^+$ | — | $\dfrac{1}{x} - \dfrac{1}{x} = 0$ | 0 (lateral) |

### Exemplo aplicado — conferência numérica

```python
def g(x):                                  # exercício 52 das anotações
    if x < 1:  return x
    if x == 1: return 3
    if x <= 2: return 2 - x**2
    return x - 3

h = 1e-9
for a in (1, 2):
    esq, dir_ = round(g(a - h), 6), round(g(a + h), 6)
    print(f"x→{a}⁻: {esq:>4}   x→{a}⁺: {dir_:>4}   g({a}) = {g(a)}   limite:", esq if esq == dir_ else "não existe")

aliquota = lambda renda: 0.0 if renda <= 35_000 else 0.07    # exemplo do imposto
print("imposto:", aliquota(35_000 - 1), "à esquerda |", aliquota(35_000 + 1), "à direita")

modulo_sobre_x = lambda x: abs(x) / x                         # exemplo 8, p. 86
print("|x|/x:", modulo_sobre_x(-1e-9), "à esquerda |", modulo_sobre_x(1e-9), "à direita")
for x in (-0.1, -0.001, 0.001, 0.1):
    print(f"1/x em x = {x:>6}: {1 / x:>8.1f}")
```

Saída esperada:

```text
x→1⁻:  1.0   x→1⁺:  1.0   g(1) = 3   limite: 1.0
x→2⁻: -2.0   x→2⁺: -1.0   g(2) = -2   limite: não existe
imposto: 0.0 à esquerda | 0.07 à direita
|x|/x: -1.0 à esquerda | 1.0 à direita
1/x em x =   -0.1:    -10.0
1/x em x = -0.001:  -1000.0
1/x em x =  0.001:   1000.0
1/x em x =    0.1:     10.0
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

A **Lista 3** indica exercícios do Stewart:

| Edição | Seção 2.2 | Seção 2.3 |
| :--- | :--- | :--- |
| 8ª | 2, 4, 5, 7, 10–12 | 41–44, 46, 47, 49, 50, 52 |
| 7ª | 2, 4, 5, 7, 10–12 | 41–44, 46–50 |

O exercício 52 (p. 88, conforme a indicação das anotações) foi resolvido em aula (**solução do material original**): a) $\lim_{x \to 1^-} g = 1$; b) $\lim_{x \to 1^+} g = 1$; c) $g(1) = 3$; d) $\lim_{x \to 2^-} g = -2$; e) $\lim_{x \to 2^+} g = -1$; f) $\lim_{x \to 2} g$ não existe (laterais diferentes).

**Exercício proposto para estudo:** uma transportadora cobra R$ 15 até 5 kg e R$ 25 acima de 5 kg (até 10 kg). Calcule os limites laterais em $x = 5$ e diga se o limite existe.

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

$\lim_{x \to 5^-} p(x) = 15$ e $\lim_{x \to 5^+} p(x) = 25$. Como os laterais são diferentes, $\lim_{x \to 5} p(x)$ **não existe**. O valor da função em 5 é $p(5) = 15$, já que "até 5 kg" inclui o 5. O "salto" de R$ 10 é uma descontinuidade.

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Tributação e tarifas:** faixas de imposto, fretes por peso e planos por consumo são funções por partes, com saltos nos limites das faixas.
- **Sistemas de controle:** chaveamentos (liga/desliga) geram funções com limites laterais diferentes.
- **Análise numérica:** detectar descontinuidades evita resultados errados em algoritmos de interpolação e integração.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Usar a expressão errada de uma função por partes | Verificar em qual intervalo está o lado analisado | Cada lado usa sua própria fórmula |
| Confundir $f(a)$ com os limites laterais | Calcular os três separadamente | Em $x = 1$, no exemplo, $g(1) = 3$ e o limite é 1 |
| Escrever "o limite é ∞" como se existisse | Dizer que $f \to \infty$ e que o limite não existe como número | Convenção das anotações |
| Abrir $\lvert x \rvert$ sem considerar o sinal | Perto de $a < 0$, use $\lvert x \rvert = -x$ | Ex. 44 |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- $x \to a^-$: pela esquerda; $x \to a^+$: pela direita.
- O limite existe se e somente se os laterais existem e são iguais.
- O valor $f(a)$ não interfere no limite.
- $1/x$ perto de 0: $-\infty$ pela esquerda e $+\infty$ pela direita.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Se $\lim_{x \to 3^-} f = 4$ e $\lim_{x \to 3^+} f = 4$, quanto vale $\lim_{x \to 3} f$?
2. Calcule $\lim_{x \to 0^-} \dfrac{\lvert x \rvert}{x}$.
3. O que acontece com $1/x$ quando $x \to 0^+$?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. 4, porque os dois laterais coincidem.
2. Para $x < 0$, $\lvert x \rvert = -x$, então $\dfrac{-x}{x} = -1$.
3. Cresce sem limite ($+\infty$).

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- STEWART, J. *Cálculo*, v. 1, seções 2.2 e 2.3 (arquivos na [aula 02](../aula02-04-03-26/README.md)).
- Materiais da pasta: [Aula 4](Aula%204%20-%20Turma%20X.pdf) · [Lista 3](Lista%203.pdf)

<br />

<p align="center"><a href="../aula04-20-03-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula06-02-04-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
