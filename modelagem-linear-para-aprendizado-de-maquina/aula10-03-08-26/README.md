<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Probabilidade%20e%20Normal&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=MODELAGEM%20LINEAR%20PARA%20APRENDIZADO%20DE%20M%C3%81QUINA%20%E2%80%94%20AULA%2009%20%E2%80%94%2003%2F08%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Probabilidade, Variáveis Aleatórias e Distribuição Normal" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=P%28A%29%20%3D%20casos%20favor%C3%A1veis%20%2F%20casos%20poss%C3%ADveis;0%20%3C%3D%20P%28E%29%20%3C%3D%201%20e%20P%28%CE%A9%29%20%3D%201;X%20~%20N%28%CE%BC%2C%20%CF%83%C2%B2%29;Z%20%3D%20%28x%20%E2%88%92%20%CE%BC%29%20%2F%20%CF%83" alt="P(A) = casos favoráveis / casos possíveis. 0 <= P(E) <= 1 e P(Ω) = 1. X ~ N(μ, σ²). Z = (x − μ) / σ." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-MLAM-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: MLAM" />
  <img src="https://img.shields.io/badge/Aula-09-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 09" />
  <img src="https://img.shields.io/badge/Data-03--08--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 03-08-2026" />
  <img src="https://img.shields.io/badge/Linguagem-Python-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=python&amp;logoColor=white" alt="Linguagem: Python" />
  <img src="https://img.shields.io/badge/Tema-Probabilidade-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Tema: Probabilidade" />
  <img src="https://img.shields.io/badge/Distribui%C3%A7%C3%A3o-Normal-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Distribuição: Normal" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Modelagem Linear para Aprendizado de Máquina](../README.md) |
| Aula | 09 — 03/08/2026 |
| Título | Probabilidade, Variáveis Aleatórias e Distribuição Normal |
| Tema central | Experimento aleatório, espaço amostral e evento; visões clássica e frequentista; axiomas e teoremas da probabilidade; variáveis aleatórias discretas e contínuas; função e distribuição de probabilidade; distribuição normal, regra empírica, padronização Z e cálculo de probabilidades acumuladas e quantis em Python. |
| Tecnologias e ferramentas | Python 3, scipy.stats (nos slides), statistics.NormalDist (verificação) |
| Docente (conforme material) | Prof. Me. Eng. Rodolfo Magliari de Paiva |
| Natureza do conteúdo | Aula teórica e prática com exemplos e exercícios resolvidos |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`Aula 01-2 - Modelagem Linear para Aprendizado de Máquina.pptx.pdf`](Aula%2001-2%20-%20Modelagem%20Linear%20para%20Aprendizado%20de%20M%C3%A1quina.pptx.pdf) | Slides da aula 01 do 2º semestre (90 páginas): probabilidade, espaço amostral, interpretações clássica e frequentista, axiomas e teoremas, variáveis aleatórias, funções e distribuições de probabilidade, distribuição normal e normal padrão, com exemplos e exercícios resolvidos. |
| [`assets/normal-alturas.svg`](assets/normal-alturas.svg) | Figura original desta documentação: curva normal N(175, 10) com as áreas do exemplo das alturas. |
| [`assets/regra-empirica.svg`](assets/regra-empirica.svg) | Figura original desta documentação: regra empírica 68–95–99,7 da distribuição normal. |

> [!NOTE]
> **Limitações da documentação.** Os slides usam scipy.stats.norm; o SciPy não está instalado no ambiente usado nesta documentação e não foi instalado. Todos os resultados numéricos do material foram conferidos com statistics.NormalDist, da biblioteca padrão, que implementa as mesmas funções (cdf, inv_cdf). Fórmulas e diagramas presentes como imagem foram lidos visualmente. Os slides trazem aviso de direitos autorais.

<br />

<h2 id="visao-geral">Visão geral</h2>

O 2º semestre começa pela **Probabilidade**, a parte da Matemática e da Estatística que estuda a chance de um evento acontecer. Ela trata apenas de eventos **probabilísticos**, de resultado incerto, e não dos **determinísticos**, de resultado certo. Se a variabilidade dá origem à aleatoriedade, a Probabilidade dá as ferramentas para **quantificar a incerteza**, estimar riscos e escolher alternativas com menor chance de prejuízo.

Os slides citam como aplicações: meteorologia, análise de risco, jogos de azar, sexagem, genética, sucesso × fracasso e inteligência artificial.

A aula culmina na **distribuição normal**, base de grande parte da inferência estatística das próximas aulas.

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Definir experimento aleatório, espaço amostral e evento.
- Calcular probabilidades pelas visões clássica e frequentista e classificar eventos.
- Aplicar os três axiomas e os quatro teoremas básicos.
- Definir variável aleatória (v.a.) e diferenciar v.a. discreta de contínua.
- Montar a distribuição de probabilidade de uma v.a. discreta.
- Calcular probabilidades e quantis na distribuição normal, inclusive pela padronização Z.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 07](../aula07-06-05-26/README.md): média, desvio padrão, quartis e boxplot.
- Noções de conjuntos (união, interseção, complemento).

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Espaço amostral e eventos

- **Experimento aleatório:** produz resultados incertos.
- **Espaço amostral** ($S$ ou $\Omega$): conjunto de **todos** os resultados possíveis.
- **Evento:** subconjunto do espaço amostral, ou seja, os resultados de interesse.

Espaços amostrais pequenos podem ser listados à mão, por **tabela de dupla entrada** ou **diagrama de árvore**. Os grandes exigem **análise combinatória**: princípio fundamental da contagem, permutações, arranjos e combinações.

### 2. Interpretações de probabilidade

$$P(A) = \frac{n^\circ \text{ de casos favoráveis}}{n^\circ \text{ de casos possíveis}}$$

| Visão | Condição | Cálculo |
| :--- | :--- | :--- |
| **Clássica** | $n(S)$ finito e conhecido, resultados **equiprováveis** | $P(A) = \dfrac{n(A)}{n(S)}$ |
| **Frequentista** | Número de tentativas **muito grande** | $P(A) \approx \dfrac{n(A)}{n(\text{tentativas})}$ (frequência relativa) |

**Classificação de eventos**, conforme a escala do slide do 1º axioma:

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart LR
    A["P = 0<br/>impossível"] --- B["0 < P < 0,5<br/>pouco provável"] --- C["P = 0,5<br/>provável<br/>(máxima incerteza)"] --- D["0,5 < P < 1<br/>muito provável"] --- E["P = 1<br/>certo"]
```

*Figura 1 — Escala de classificação usada nas respostas dos exercícios.*

### 3. Axiomas e teoremas

| Axiomas (aceitos sem demonstração) | Teoremas (demonstrados a partir dos axiomas) |
| :--- | :--- |
| 1º) $0 \leq P(E) \leq 1$ | 1º) $P(\varnothing) = 0$ |
| 2º) $P(\Omega) = 1$ | 2º) $P(A^c) = 1 - P(A)$ (complemento) |
| 3º) $P(A \cup B) = P(A) + P(B)$, se $A$ e $B$ são **mutuamente exclusivos** (disjuntos) | 3º) Se $A \subset B$, então $P(A) \leq P(B)$ |
| | 4º) $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, para eventos **não** mutuamente exclusivos |

O 4º teorema subtrai a interseção porque ela seria contada **duas vezes**.

### 4. Variável aleatória

Uma **variável aleatória** $X$ é uma **função** que associa um número real a cada resultado do espaço amostral. A letra maiúscula ($X$) denota a variável; a minúscula ($x = 70$ cm), o valor observado.

| Tipo | Natureza | Exemplos dos slides |
| :--- | :--- | :--- |
| **Discreta** | Contagem; valores enumeráveis | Nº de pessoas com doença celíaca; nº de ligações por dia (0, 1, 2, …) |
| **Contínua** | Medição; intervalo de números reais | Tempo de espera no hospital; duração de uma ligação, $y \in [0; 120]$ min |

**Distribuição de probabilidade** é a função que atribui a cada valor $x_i$ sua probabilidade. Ela exige que cada probabilidade esteja entre 0 e 1 e que **todas somem 1**.

| v.a. discreta | v.a. contínua |
| :--- | :--- |
| Função massa de probabilidade: $f(x) = P(X = x)$ | Função densidade: $P(a \leq X \leq b) = \int_a^b f(x)\,dx$ |
| Acumulada: $F(x) = \sum_{x_i \leq x} f(x_i)$ | Acumulada: $F(x) = \int_{-\infty}^{x} f(u)\,du$ |
| Exemplos: uniforme discreta, binomial, geométrica, hipergeométrica, Poisson | Exemplos: uniforme contínua, **normal**, exponencial, gama, Weibull, lognormal |

Numa v.a. contínua, a probabilidade é a **área** sob a curva de densidade.

### 5. Distribuição normal

A **distribuição normal** (gaussiana, ou "curva de sino") é simétrica em torno da média e descreve bem fenômenos como altura, peso, pressão arterial e tempos de reação. Notação: $X \sim N(\mu, \sigma^2)$.

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

- $\mu$ desloca a curva no eixo horizontal; $\sigma$ a alarga ou estreita.
- Média, mediana e moda coincidem em $\mu$.

<p align="center">
  <img src="assets/regra-empirica.svg" width="720" alt="Curva normal com três faixas sombreadas centradas na média: entre μ−σ e μ+σ ficam cerca de 68,27% dos valores; entre μ−2σ e μ+2σ, 95,45%; entre μ−3σ e μ+3σ, 99,73%." />
</p>

*Figura 2 — Regra empírica, apresentada nos slides (SVG original; percentuais calculados com `statistics.NormalDist`).*

Os slides destacam ainda a ligação com o **boxplot** da [aula 07](../aula07-06-05-26/README.md). Em dados normais, Q1 e Q3 ficam a cerca de $\pm 0{,}6745\sigma$ da média, e os limites de *outliers* a $\pm 2{,}698\sigma$. Assim, o boxplot ajuda a avaliar simetria e desvios da normalidade.

**Padronização:** $Z = \dfrac{x - \mu}{\sigma}$ transforma qualquer normal na **normal padrão** $N(0, 1)$. Isso facilita os cálculos manuais (com tabela) e permite comparar variáveis de unidades diferentes.

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — probabilidade clássica e variável aleatória

O exercício de genética dos slides (homem Ab/ab × mulher aB/ab) e a v.a. "número de caras em 3 lançamentos de moeda":

```python
from fractions import Fraction
from itertools import product
from collections import Counter

def classificar(p):
    if p == 0: return "impossível"
    if p == 1: return "certo"
    if p == Fraction(1, 2): return "provável (máxima incerteza)"
    return "pouco provável" if p < Fraction(1, 2) else "muito provável"

# genética (exercício dos slides): homem Ab x ab, mulher aB x ab
pai, mae = ["Ab", "ab"], ["aB", "ab"]
filhos = []
for gp, gm in product(pai, mae):
    filhos.append("".join(sorted(gp[0] + gm[0])) + "".join(sorted(gp[1] + gm[1])))
homozigoto = [g for g in filhos if g[0] == g[1] and g[2] == g[3]]
p = Fraction(len(homozigoto), len(filhos))
print("espaço amostral:", filhos)
print(f"P(homozigoto) = {p} = {float(p)} -> {classificar(p)}")

# variável aleatória: nº de caras em 3 lançamentos de moeda
omega = ["".join(r) for r in product("kc", repeat=3)]
X = Counter(s.count("k") for s in omega)
print("Ω =", omega)
print("distribuição de X:", {x: str(Fraction(X[x], len(omega))) for x in sorted(X)})
```

Saída esperada:

```text
espaço amostral: ['AaBb', 'Aabb', 'aaBb', 'aabb']
P(homozigoto) = 1/4 = 0.25 -> pouco provável
Ω = ['kkk', 'kkc', 'kck', 'kcc', 'ckk', 'ckc', 'cck', 'ccc']
distribuição de X: {0: '1/8', 1: '3/8', 2: '3/8', 3: '1/8'}
```

Só `aabb` é homozigoto nos dois genes, e por isso a probabilidade é $1/4$, como na resposta do material.

### Exemplo intermediário — distribuição de probabilidade do nível de estresse (exemplo dos slides)

150 funcionários classificados de 1 (muito calmo) a 5 (muito irritado):

```python
freq = {1: 24, 2: 33, 3: 42, 4: 30, 5: 21}     # nível de estresse x: frequência (150 funcionários)
n = sum(freq.values())

dist = {x: f / n for x, f in freq.items()}
for x, p in dist.items():
    print(f"P(X = {x}) = {freq[x]}/{n} = {p:.2f}")
print("soma das probabilidades:", round(sum(dist.values()), 10))

acumulada = 0
for x, p in dist.items():
    acumulada += p
    print(f"F({x}) = P(X <= {x}) = {acumulada:.2f}")
```

Saída esperada:

```text
P(X = 1) = 24/150 = 0.16
P(X = 2) = 33/150 = 0.22
P(X = 3) = 42/150 = 0.28
P(X = 4) = 30/150 = 0.20
P(X = 5) = 21/150 = 0.14
soma das probabilidades: 1.0
F(1) = P(X <= 1) = 0.16
F(2) = P(X <= 2) = 0.38
F(3) = P(X <= 3) = 0.66
F(4) = P(X <= 4) = 0.86
F(5) = P(X <= 5) = 1.00
```

As probabilidades coincidem com a tabela do slide (0,16; 0,22; 0,28; 0,20; 0,14) e somam 1.

### Exemplo aplicado — normal: probabilidades acumuladas e quantis

Os slides usam `scipy.stats.norm`. O código abaixo usa `statistics.NormalDist`, da biblioteca padrão, que tem as mesmas operações. A correspondência é `norm.cdf(x, μ, σ)` → `NormalDist(μ, σ).cdf(x)`, `norm.sf` → `1 − cdf` e `norm.ppf(p, μ, σ)` → `NormalDist(μ, σ).inv_cdf(p)`.

```python
from statistics import NormalDist      # biblioteca padrão; equivalente a scipy.stats.norm

alturas = NormalDist(mu=175, sigma=10)

a = alturas.cdf(164)                    # norm.cdf(164, 175, 10)
b = 1 - alturas.cdf(164)                # norm.sf(164, 175, 10)
c = alturas.cdf(174) - alturas.cdf(164)
print(f"a) P(X <= 164)       = {a:.4f}")
print(f"b) P(X >= 164)       = {b:.4f}")
print(f"c) P(164 <= X <= 174) = {c:.4f}")

# padronização: Z = (x - μ) / σ leva ao mesmo resultado
z = (164 - 175) / 10
print(f"z = {z}  ->  Φ(z) = {NormalDist().cdf(z):.4f}")

# quantil (inversa da acumulada), como norm.ppf: tempo de produção N(120, 15)
lote = NormalDist(120, 15)
print(f"95% dos lotes em até {lote.inv_cdf(0.95):.2f} min")
print(f"80% centrais entre {lote.inv_cdf(0.10):.2f} e {lote.inv_cdf(0.90):.2f} min")
```

Saída esperada:

```text
a) P(X <= 164)       = 0.1357
b) P(X >= 164)       = 0.8643
c) P(164 <= X <= 174) = 0.3245
z = -1.1  ->  Φ(z) = 0.1357
95% dos lotes em até 144.67 min
80% centrais entre 100.78 e 139.22 min
```

<p align="center">
  <img src="assets/normal-alturas.svg" width="720" alt="Curva normal de média 175 cm e desvio 10 cm. A área à esquerda de 164 cm, em vermelho, vale cerca de 0,1357; a área entre 164 e 174 cm, em laranja, vale cerca de 0,3245; a área à direita de 164 cm vale cerca de 0,8643." />
</p>

*Figura 3 — As três probabilidades do exemplo das alturas como áreas sob a curva (SVG original).*

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

### Probabilidade clássica e variáveis aleatórias

| Exercício | Solução do material original |
| :--- | :--- |
| Pulso corrompido (2 em 10 pulsos) | $P = 2/10 = 0{,}2$, pouco provável |
| Clima: chuvoso e sem sol (12 dias) | $P = 5/12 \approx 0{,}42$, pouco provável |
| Genética: criança homozigótica | $P = 1/4 = 0{,}25$, pouco provável (conferido acima) |
| Discreta ou contínua: a) tempo de retorno de um projétil; b) mudanças de estado de um transistor; c) volume de gasolina evaporado; d) diâmetro de um eixo | a) contínua; b) **discreta**; c) contínua; d) contínua |

### Distribuição normal

Todas as respostas do material foram **recalculadas** com `statistics.NormalDist`:

| Exercício | Solução do material original | Conferência |
| :--- | :--- | :--- |
| Alturas N(175, 10): a) $P(X \leq 164)$; b) $P(X \geq 164)$; c) $P(164 \leq X \leq 174)$ | a) ≈ 0,1356, pouco provável; b) ≈ 0,8643, muito provável; c) ≈ 0,3245, pouco provável | 0,13567; 0,86433; 0,32451 ✔ (o material trunca a 4ª casa em a) |
| Arruelas N(11,15; 2,238): a) $< 8{,}70$; b) $< 14{,}70$; c) entre os dois | a) ≈ 0,1368; b) ≈ 0,9436; c) ≈ 0,8068 | 0,13682; 0,94366; 0,80684 ✔ |
| Alturas com variância 64 cm²: $P(X > 180)$ | $\sigma = \sqrt{64} = 8$; ≈ 0,2266, pouco provável | 0,22663 ✔ |
| Porcos N(64, 15), 800 animais: entre 42 e 73 kg | ≈ 0,6545; ≈ 524 porcos | 0,65451; 523,6 ✔ |
| Poluente N(8; 1,5): $P(X > 10)$ ppm | ≈ 0,0912 (9,12%), pouco provável | 0,09121 ✔ |
| Teste de aptidão N(45, 400), 50 candidatos: $X > 50$ ou $X < 30$ | $\sigma = 20$; ≈ 0,6279; "≈ 32 candidatos" | 0,62792; $50 \times 0{,}6279 = 31{,}4$ ⚠ |
| Produção N(120, 15): a) $< 100$ min; b) quantil de 95%; c) 80% centrais | a) ≈ 0,0912; b) ≈ 144,67 min; c) 100,77 a 139,22 min | 0,09121; 144,67; 100,78 e 139,22 ✔ |

> [!NOTE]
> No teste de aptidão, $50 \times 0{,}6279 \approx 31{,}4$: o arredondamento usual daria **31** candidatos. O material indica 32. A diferença é apenas de arredondamento; a probabilidade está correta.

**Por que somar no exercício do teste de aptidão?** "Mais de 50" e "menos de 30" são eventos **mutuamente exclusivos** (não há tempo nas duas faixas ao mesmo tempo). Pelo 3º axioma, $P(A \cup B) = P(A) + P(B)$.

**Exercício proposto para estudo:** em um dado honesto, sejam $A$ = "número par" e $B$ = "número maior que 3". Calcule $P(A \cup B)$.

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

$A = \{2, 4, 6\}$, $B = \{4, 5, 6\}$ e $A \cap B = \{4, 6\}$. Os eventos **não** são mutuamente exclusivos, então pelo 4º teorema:

$$P(A \cup B) = \tfrac{3}{6} + \tfrac{3}{6} - \tfrac{2}{6} = \tfrac{4}{6} \approx 0{,}67$$

Conferência direta: $A \cup B = \{2, 4, 5, 6\}$, com 4 de 6 casos, um evento muito provável.

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Controle de qualidade:** a probabilidade de uma peça sair da especificação (como as arruelas) define taxas de refugo e limites de tolerância.
- **Meio ambiente e conformidade:** estimar a chance de exceder limites regulatórios (exercício do poluente).
- **Planejamento de produção:** quantis (`inv_cdf`/`ppf`) definem prazos que atendem, por exemplo, 95% dos pedidos.
- **Aprendizado de máquina:** modelos probabilísticos, padronização de atributos (*z-score*) e detecção de anomalias usam diretamente estes conceitos.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Passar a **variância** como desvio em `norm.cdf` ou `NormalDist` | Converter: $\sigma = \sqrt{\sigma^2}$ | Os exercícios 2 e 5 dão a variância de propósito |
| Somar probabilidades de eventos com interseção | Subtrair $P(A \cap B)$ (4º teorema) | Evita contar a interseção duas vezes |
| Calcular $P(X > x)$ com `cdf(x)` | Usar `1 - cdf(x)` (ou `norm.sf`) | `cdf` é a área **à esquerda** |
| Resolver sem esboçar a curva | Esboçar e sombrear a área pedida (recomendação dos slides) | Evita confundir cauda esquerda e direita |
| Esperar $P(X = x) > 0$ em v.a. contínua | Trabalhar com intervalos | A área sobre um ponto é zero |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- $P(A) = n(A)/n(S)$ (clássica) ou frequência relativa em muitas tentativas (frequentista).
- Axiomas: $0 \leq P \leq 1$; $P(\Omega) = 1$; aditividade para eventos disjuntos.
- Teoremas: $P(\varnothing) = 0$; $P(A^c) = 1 - P(A)$; $A \subset B \Rightarrow P(A) \leq P(B)$; $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
- v.a.: função que associa números aos resultados; discreta (contagem) ou contínua (medição).
- Normal $N(\mu, \sigma^2)$: simétrica; 68–95–99,7; $Z = (x - \mu)/\sigma$.
- Python: `cdf` (área à esquerda), `1 - cdf` (à direita), diferença de `cdf` (intervalo), `inv_cdf`/`ppf` (quantil).

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Se $P(A) = 0{,}7$, quanto vale $P(A^c)$?
2. Uma v.a. normal tem $\mu = 100$ e $\sigma = 15$. Qual o valor de $z$ para $x = 130$?
3. Aproximadamente que porcentagem dos valores de uma normal fica entre $\mu - 2\sigma$ e $\mu + 2\sigma$?
4. O número de e-mails recebidos por hora é uma v.a. discreta ou contínua?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. $1 - 0{,}7 = 0{,}3$ (2º teorema).
2. $z = (130 - 100)/15 = 2$.
3. Cerca de 95% (95,45%).
4. Discreta, porque é uma contagem.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [Python — `statistics.NormalDist`](https://docs.python.org/pt-br/3/library/statistics.html#statistics.NormalDist)
- [SciPy — `scipy.stats.norm`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html), usado nos slides.
- QUINSLER, A. P. *Probabilidade e Estatística*. Curitiba: InterSaberes, 2022 (bibliografia da disciplina).
- Materiais complementares indicados nos slides: [variáveis aleatórias (UFSC)](https://www.inf.ufsc.br/~andre.zibetti/probabilidade/variaveis_aleatorias.html) · [distribuições de probabilidade (UFMG)](https://www.est.ufmg.br/~monitoria/Material/ApostilaR/DistribuicoesProbabilidade.html) · [distribuição normal (UFSC)](https://www.inf.ufsc.br/~andre.zibetti/probabilidade/normal.html)

<br />

<p align="center"><a href="../aula08-26-05-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula10-11-08-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
