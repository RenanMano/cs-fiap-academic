<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Limite%20de%20uma%20Fun%C3%A7%C3%A3o&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=MODELAGEM%20MATEM%C3%81TICA%20E%20COMPUTACIONAL%20%E2%80%94%20AULA%2004%20%E2%80%94%2020%2F03%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Limite de uma Função e Substituição Direta" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=lim%20x%E2%86%921%20%28x%C2%B2%20%E2%88%92%201%29%2F%28x%20%E2%88%92%201%29%20%3D%202;Perto%20de%20a%2C%20mas%20sem%20ser%20igual%20a%20a;Cont%C3%ADnua%3A%20lim%20x%E2%86%92a%20f%28x%29%20%3D%20f%28a%29;0%2F0%3A%20simplifique%20e%20substitua" alt="lim x→1 (x² − 1)/(x − 1) = 2. Perto de a, mas sem ser igual a a. Contínua: lim x→a f(x) = f(a). 0/0: simplifique e substitua." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-MMC-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: MMC" />
  <img src="https://img.shields.io/badge/Aula-04-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 04" />
  <img src="https://img.shields.io/badge/Data-20--03--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 20-03-2026" />
  <img src="https://img.shields.io/badge/Tema-Limites-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Tema: Limites" />
  <img src="https://img.shields.io/badge/T%C3%A9cnica-Substitui%C3%A7%C3%A3o%20direta-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Técnica: Substituição direta" />
  <img src="https://img.shields.io/badge/Lista-Lista%202-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Lista: Lista 2" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Modelagem Matemática e Computacional](../README.md) |
| Aula | 04 — 20/03/2026 |
| Título | Limite de uma Função e Substituição Direta |
| Tema central | Ideia intuitiva de limite por tabelas de aproximação, definição e notação, diferença entre limite e valor da função, regra da substituição direta para funções contínuas e simplificação algébrica (fatoração) para indeterminações 0/0, com exemplos do Stewart e a Lista 2. |
| Tecnologias e ferramentas | Python 3 (aproximações numéricas) |
| Docente (conforme material) | Prof. Igor Gimenes Cesca |
| Natureza do conteúdo | Anotações de aula e lista de exercícios (referências ao Stewart) |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`Aula 3 - Turma X.pdf`](Aula%203%20-%20Turma%20X.pdf) | Anotações da aula 3 (6 páginas): tabela de aproximação de (x² − 1)/(x − 1), definição e notação de limite, exemplos gráficos, regra da substituição direta e exemplos resolvidos das páginas 83 e 88 do Stewart. |
| [`Lista 2.pdf`](Lista%202.pdf) | Lista 2 (1 página): exercícios das seções 2.2 e 2.3 do Stewart, 7ª e 8ª edições. |
| [`assets/limite-buraco.svg`](assets/limite-buraco.svg) | Figura original desta documentação: gráfico de (x² − 1)/(x − 1) com o “buraco” em (1, 2) e valores de aproximação. |

> [!NOTE]
> **Limitações da documentação.** As anotações de aula contêm trechos manuscritos, lidos visualmente. A Lista 2 apenas indica exercícios do livro de Stewart (seções 2.2 e 2.3), cujos enunciados não estão na pasta e não são reproduzidos. Os limites resolvidos nas anotações foram conferidos numericamente.

<br />

<h2 id="visao-geral">Visão geral</h2>

O **limite** é a primeira ferramenta nova do Cálculo. A pergunta da aula é: o que acontece com $f(x) = \dfrac{x^2 - 1}{x - 1}$ quando $x$ fica **muito próximo** de 1, sem nunca ser igual a 1? Em $x = 1$ a função não existe, porque há divisão por zero. Mesmo assim, os valores ao redor se aproximam de **2**. O limite descreve esse comportamento **na vizinhança** de um ponto, independentemente do que acontece exatamente nele.

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Estimar limites por tabelas de valores à esquerda e à direita.
- Usar corretamente a notação $\lim_{x \to a} f(x) = L$.
- Diferenciar o **limite** em $a$ do **valor** $f(a)$.
- Aplicar a substituição direta em funções contínuas.
- Resolver indeterminações $0/0$ por fatoração e simplificação.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 03](../aula03-13-03-26/README.md): funções e domínio.
- Fatoração: diferença de quadrados, trinômio e evidência.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Definição e notação

O **limite** de $f(x)$ quando $x$ tende a $a$ é o valor $L$ do qual a função se aproxima à medida que $x$ se aproxima de $a$, **sem ser igual** a $a$:

$$\lim_{x \to a} f(x) = L \quad \text{(lê-se: "o limite de } f(x) \text{ quando } x \text{ tende a } a \text{ é } L\text{")}$$

<p align="center">
  <img src="assets/limite-buraco.svg" width="720" alt="Gráfico de (x² − 1)/(x − 1), que coincide com a reta y = x + 1 exceto em x = 1, onde há um círculo vazio no ponto (1, 2). Valores próximos: f(0,9) = 1,9; f(0,99) = 1,99; f(1,01) = 2,01; f(1,1) = 2,1. O limite é 2, embora f(1) não exista." />
</p>

*Figura 1 — O exemplo de abertura da aula (SVG original).*

### 2. Limite × valor da função

As anotações mostram três gráficos com o mesmo limite, $\lim_{x \to 3} f(x) = 6$:

| Situação | $f(3)$ | $\lim_{x \to 3} f(x)$ |
| :--- | :---: | :---: |
| $3 \notin D$ (buraco no gráfico) | Não existe | 6 |
| $3 \in D$, mas $f(3) = 8$ (ponto deslocado) | 8 | 6 |
| Função contínua, como $y = 2x$ | 6 | 6 |

**O limite analisa o que acontece perto de $a$, e não em $a$.**

### 3. Regra da substituição direta

Se $f$ é **contínua** em $a$, então $\lim_{x \to a} f(x) = f(a)$: basta substituir. Exemplo: $\lim_{x \to 2} x^2 = 2^2 = 4$.

### 4. Quando a substituição dá $0/0$

A orientação das anotações é **simplificar ao máximo** a função até que a substituição seja possível:

$$\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} \frac{(x + 1)(x - 1)}{x - 1} = \lim_{x \to 1} (x + 1) = 2$$

A simplificação é válida porque, no limite, $x \neq 1$, então $x - 1 \neq 0$ pode ser cancelado.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart TD
    A["Calcular lim x→a f(x)"] --> B{"Substituir x = a<br/>dá um número?"}
    B -->|"sim (f contínua em a)"| C["Esse número é o limite"]
    B -->|"0/0"| D["Fatorar ou expandir<br/>e cancelar o fator comum"]
    D --> A
```

*Figura 2 — Estratégia da aula para calcular limites.*

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — a tabela de aproximação da aula

```python
def f(x):
    return (x**2 - 1) / (x - 1)       # não definida em x = 1

for h in (0.1, 0.01, 0.001, 0.0001):
    print(f"x = {1 - h:<7} f(x) = {f(1 - h):.4f}    |    x = {1 + h:<7} f(x) = {f(1 + h):.4f}")

# após simplificar, (x² − 1)/(x − 1) = x + 1, e a substituição direta dá o limite
print("limite por substituição em x + 1:", 1 + 1)
```

Saída esperada:

```text
x = 0.9     f(x) = 1.9000    |    x = 1.1     f(x) = 2.1000
x = 0.99    f(x) = 1.9900    |    x = 1.01    f(x) = 2.0100
x = 0.999   f(x) = 1.9990    |    x = 1.001   f(x) = 2.0010
x = 0.9999  f(x) = 1.9999    |    x = 1.0001  f(x) = 2.0001
limite por substituição em x + 1: 2
```

### Exemplo intermediário — os limites resolvidos nas anotações

| Limite (fonte nas anotações) | Técnica | Resultado |
| :--- | :--- | :---: |
| $\lim_{x \to 5} (2x^2 - 3x + 4)$ (p. 83, ex. 2a) | Substituição direta | 39 |
| $\lim_{x \to -2} \dfrac{x^3 + 2x^2 - 1}{5 - 3x}$ (p. 83, ex. 2b) | Substituição direta ($5 - 3x \neq 0$) | $-1/11$ |
| $\lim_{h \to 0} \dfrac{(3 + h)^2 - 9}{h}$ (p. 83, ex. 5) | Expandir: $\dfrac{6h + h^2}{h} = 6 + h$ | 6 |
| $\lim_{x \to 2} \dfrac{x^2 + x - 6}{x - 2}$ (p. 88, ex. 11) | Fatorar: $(x + 3)(x - 2)$ | 5 |
| $\lim_{x \to -3} \dfrac{x^2 + 3x}{x^2 - x - 12}$ (p. 88, ex. 12) | Fatorar: $\dfrac{x(x + 3)}{(x - 4)(x + 3)}$ | $3/7$ |

### Exemplo aplicado — conferência numérica

```python
def lim_numerico(f, a, h=1e-6):
    """Aproxima o limite pelos dois lados: f(a − h) e f(a + h)."""
    return round(f(a - h), 4), round(f(a + h), 4)

exemplos = {
    "lim x→5  (2x² − 3x + 4)":              (lambda x: 2*x**2 - 3*x + 4, 5),
    "lim x→−2 (x³ + 2x² − 1)/(5 − 3x)":     (lambda x: (x**3 + 2*x**2 - 1) / (5 - 3*x), -2),
    "lim h→0  ((3 + h)² − 9)/h":            (lambda h: ((3 + h)**2 - 9) / h, 0),
    "lim x→2  (x² + x − 6)/(x − 2)":        (lambda x: (x**2 + x - 6) / (x - 2), 2),
    "lim x→−3 (x² + 3x)/(x² − x − 12)":     (lambda x: (x**2 + 3*x) / (x**2 - x - 12), -3),
}
for nome, (f, a) in exemplos.items():
    print(f"{nome:<36} ≈ {lim_numerico(f, a)}")
print("valores exatos: 39, −1/11 ≈", round(-1/11, 4), ", 6, 5, 3/7 ≈", round(3/7, 4))
```

Saída esperada:

```text
lim x→5  (2x² − 3x + 4)              ≈ (39.0, 39.0)
lim x→−2 (x³ + 2x² − 1)/(5 − 3x)     ≈ (-0.0909, -0.0909)
lim h→0  ((3 + h)² − 9)/h            ≈ (6.0, 6.0)
lim x→2  (x² + x − 6)/(x − 2)        ≈ (5.0, 5.0)
lim x→−3 (x² + 3x)/(x² − x − 12)     ≈ (0.4286, 0.4286)
valores exatos: 39, −1/11 ≈ -0.0909 , 6, 5, 3/7 ≈ 0.4286
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

A **Lista 2** indica exercícios do Stewart:

| Edição | Seção 2.2 | Seção 2.3 |
| :--- | :--- | :--- |
| 8ª | 1, 19–24, 26 | 3–9, 11, 12, 15–27, 29–32, 59, 64, 65 |
| 7ª | 1, 19–23, 25, 26 | 3–9, 11, 12, 15–32, 57, 58, 62, 63 |

Os livros estão na [aula 02](../aula02-04-03-26/README.md). As anotações deixam **sem resolução** o limite $\lim_{t \to -3} \dfrac{t^2 - 9}{2t^2 + 7t + 3}$ (ex. 15).

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

Em $t = -3$, a substituição dá $\dfrac{0}{18 - 21 + 3} = \dfrac{0}{0}$. Fatorando:

$$\frac{t^2 - 9}{2t^2 + 7t + 3} = \frac{(t - 3)(t + 3)}{(2t + 1)(t + 3)} = \frac{t - 3}{2t + 1} \;\xrightarrow{t \to -3}\; \frac{-6}{-5} = \frac{6}{5}$$

```python
f = lambda t: (t**2 - 9) / (2*t**2 + 7*t + 3)
print(round(f(-3 - 1e-6), 4), round(f(-3 + 1e-6), 4))
```

Saída esperada:

```text
1.2 1.2
```

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Fundamento da derivada:** a taxa de variação instantânea ([aula 08](../aula08-22-04-26/README.md)) é um limite do tipo $0/0$, como o exemplo com $h \to 0$.
- **Computação numérica:** algoritmos aproximam valores por sequências que convergem (limites) e precisam lidar com divisões por números muito pequenos.
- **Engenharia:** analisar o comportamento de um sistema perto de um ponto crítico, onde a fórmula "quebra".

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Concluir "não existe" ao obter $0/0$ | Tratar $0/0$ como **indeterminação** e simplificar | $0/0$ indica que é preciso mais trabalho |
| Achar que $\lim_{x \to a} f(x)$ é sempre $f(a)$ | Só vale para funções **contínuas** em $a$ | Ver a tabela da seção 2 |
| Usar só valores de um lado na tabela | Aproximar pela esquerda **e** pela direita | Os lados podem diferir ([aula 05](../aula05-30-03-26/README.md)) |
| Confiar apenas na tabela numérica | Confirmar algebricamente | Arredondamentos podem enganar |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- $\lim_{x \to a} f(x) = L$: valores de $f$ próximos de $L$ para $x$ próximo de $a$ (com $x \neq a$).
- Limite ≠ valor da função.
- Função contínua em $a$: **substituição direta**.
- $0/0$: fatorar ou expandir, cancelar e substituir.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Calcule $\lim_{x \to 4} \dfrac{x^2 - 16}{x - 4}$.
2. Se $f(2) = 7$ e $\lim_{x \to 2} f(x) = 3$, a função é contínua em 2?
3. Calcule $\lim_{x \to 0} (3x^2 - x + 5)$.

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. $\dfrac{(x + 4)(x - 4)}{x - 4} = x + 4 \to 8$.
2. Não, porque o limite (3) é diferente do valor da função (7).
3. Por substituição direta: 5.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- STEWART, J. *Cálculo*, v. 1, seções 2.2 e 2.3 (arquivos na [aula 02](../aula02-04-03-26/README.md)).
- Materiais da pasta: [Aula 3](Aula%203%20-%20Turma%20X.pdf) · [Lista 2](Lista%202.pdf)

<br />

<p align="center"><a href="../aula03-13-03-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula05-30-03-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
