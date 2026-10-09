<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Git%2C%20GitHub%20e%20Python&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=PENSAMENTO%20COMPUTACIONAL%20E%20AUTOMA%C3%87%C3%83O%20COM%20PYTHON%20%E2%80%94%20AULA%2003%20%E2%80%94%2015%2F03%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Git, GitHub e Introdução ao Python: Variáveis e Operadores" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=git%20config%20--global%20user.name;print%287%20%2B%204%29%20%E2%86%92%2011%2C%20print%28%277%27%20%2B%20%274%27%29%20%E2%86%92%2074;3%20%2A%20%285%20%2B%204%29%20%2A%2A%202%20%3D%20243;Bonito%20%C3%A9%20melhor%20que%20feio%20%28Zen%20do%20Python%29" alt="git config --global user.name. print(7 + 4) → 11; print('7' + '4') → 74. 3 * (5 + 4) ** 2 = 243. Bonito é melhor que feio (Zen do Python)." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-PCP-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: PCP" />
  <img src="https://img.shields.io/badge/Aula-03-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 03" />
  <img src="https://img.shields.io/badge/Data-15--03--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 15-03-2026" />
  <img src="https://img.shields.io/badge/Linguagem-Python-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=python&amp;logoColor=white" alt="Linguagem: Python" />
  <img src="https://img.shields.io/badge/Versionamento-Git%20e%20GitHub-FF4500?style=for-the-badge&amp;labelColor=0D1117&amp;logo=git&amp;logoColor=white" alt="Versionamento: Git e GitHub" />
  <img src="https://img.shields.io/badge/IDE-PyCharm-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="IDE: PyCharm" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py,git,github,pycharm&amp;theme=dark" alt="Python, Git, GitHub, PyCharm" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Pensamento Computacional e Automação com Python](../README.md) |
| Aula | 03 — 15/03/2026 |
| Título | Git, GitHub e Introdução ao Python: Variáveis e Operadores |
| Tema central | Git × GitHub, configuração do Git; história, características e Zen do Python; linguagens de alto e baixo nível, compiladas e interpretadas; instalação do Python e do PyCharm; IDEs; primeiros comandos (print, input), tipos primitivos, operadores aritméticos, precedência, atribuição e comparação; exercícios. |
| Tecnologias e ferramentas | Git, GitHub, Python 3, PyCharm |
| Docente (conforme material) | Prof. Alexandre Russi Junior |
| Natureza do conteúdo | Aula prática com desafios e exercícios |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`PCP - Aula 02 - Git, GitHub e Introdução ao Python.pdf`](PCP%20-%20Aula%2002%20-%20Git%2C%20GitHub%20e%20Introdu%C3%A7%C3%A3o%20ao%20Python.pdf) | Slides (50 páginas): Git e GitHub (conta, repositório, instalação, configuração), história e características do Python, Zen do Python, tipos de linguagem, instalação do Python e do PyCharm, IDEs, primeiros comandos, desafios, tipos primitivos, operadores e nove exercícios. |

> [!NOTE]
> **Limitações da documentação.** Os slides trazem aviso de direitos autorais; o conteúdo é explicado com redação própria. Vários slides mostram código como imagens em blocos coloridos, lidas visualmente. Os exercícios não têm gabarito: as respostas são propostas e executadas com valores fixos no lugar de input(). Os exercícios 2 e 3 do material são idênticos.

<br />

<h2 id="visao-geral">Visão geral</h2>

A aula prepara o ambiente de trabalho e escreve as primeiras linhas de Python:

1. **Git e GitHub:** versionar o código e hospedá-lo na nuvem.
2. **Python:** origem, filosofia e funcionamento (linguagem interpretada de alto nível).
3. **Ambiente:** instalação do interpretador e do PyCharm.
4. **Primeiros programas:** `print`, `input`, variáveis, tipos e operadores.

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Diferenciar Git de GitHub e configurar a identidade no Git.
- Explicar as características do Python e a diferença entre linguagens compiladas e interpretadas.
- Instalar o Python com o `PATH` configurado e usar uma IDE.
- Usar `print` e `input`, os tipos `int`, `float`, `str`, `bool` e `list`, e os operadores.
- Aplicar a ordem de precedência dos operadores.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 02](../aula02-10-03-26/README.md): algoritmos, variáveis e operadores em pseudocódigo.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Git × GitHub

| Git | GitHub |
| :--- | :--- |
| **Versionador** de código, instalado localmente | **Plataforma** de hospedagem de repositórios Git |
| Registra o histórico de alterações | Colaboração, armazenamento remoto, portfólio |

Configuração inicial no Git Bash, com os dados da conta do GitHub:

<!-- norun -->
```text
git config --global user.name "username"
git config --global user.email "email@email.com"
```

### 2. Python

- **Criado** por Guido van Rossum no CWI (Holanda) e lançado em 1991, com inspiração na linguagem ABC. O nome homenageia o grupo **Monty Python**, e não a serpente.
- **Marcos:** financiamento da DARPA (1995, projeto CP4E) e criação da Python Software Foundation (2001).
- **Características:** propósito geral, fácil, multiplataforma, *batteries included*, código aberto, orientado a objetos.
- **Zen do Python** (`import this`): "Bonito é melhor que feio", "Simples é melhor que complexo", "Legibilidade conta", "Erros nunca devem passar silenciosamente".

| | Compilada | Interpretada |
| :--- | :--- | :--- |
| Funcionamento | Código → compilador → executável | Interpretador executa linha a linha |
| Exemplos | C, C++, Go, Rust | **Python**, JavaScript, Ruby |
| Vantagem | Execução mais rápida | Teste e depuração imediatos |
| Desvantagem | Compilação demorada; erros aparecem depois | Execução mais lenta |

**Instalação no Windows:** marque **"Add python.exe to PATH"**, clique em *Install Now*, desabilite o limite de caracteres de caminho e teste o comando `python` num novo prompt.

**IDE** (Ambiente de Desenvolvimento Integrado): editor, compilador ou interpretador, *debugger*, geração de código, testes, *deploy* e refatoração. A disciplina usa o **PyCharm**.

### 3. Tipos primitivos e operadores

| Tipo | Exemplos |
| :--- | :--- |
| `int` | `7`, `-4`, `0`, `9875` |
| `float` | `4.5`, `0.076`, `-15.223`, `7.0` |
| `bool` | `True`, `False` |
| `str` | `'Olá'`, `'7.5'`, `''` |
| `list` | `[1, 2, 3, 4]`, `['a', 'b', 'c']` |

| Aritméticos | Atribuição | Comparação |
| :--- | :--- | :--- |
| `+ - * /` | `=`, `+=`, `-=` | `>`, `<` |
| `**` potência | `*=`, `/=` | `==` igual |
| `//` divisão inteira | `%=` | `!=` diferente |
| `%` resto | | `>=`, `<=` |

**Precedência (slides):** 1) `()` · 2) `**` · 3) `*`, `/`, `//`, `%` · 4) `+`, `-`.

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — primeiros comandos e operadores

```python
print("Olá, Mundo!")
print(7 + 4)          # soma de números
print("7" + "4")      # concatenação de textos
print(type(7), type(4.5), type(True), type("7.5"))

# operadores e precedência (exemplos dos slides)
print(5 + 2, 5 - 2, 5 * 2, 5 / 2, 5 ** 2, 5 // 2, 5 % 2)
print(5 + 3 * 2, 3 * 5 + 4 ** 2, 3 * (5 + 4) ** 2)

x = 1
x += 1; x *= 10; x %= 7
print("atribuição composta:", x)
print(7 > 5, 7 == 5, 7 != 5, 5 <= 5)
```

Saída esperada:

```text
Olá, Mundo!
11
74
<class 'int'> <class 'float'> <class 'bool'> <class 'str'>
7 3 10 2.5 25 2 1
11 31 243
atribuição composta: 6
True False True True
```

`print(7 + 4)` soma números, enquanto `print('7' + '4')` **concatena** textos. Os três resultados de precedência (11, 31, 243) são os dos slides.

### Exemplo aplicado — os nove exercícios

Os enunciados usam `input()`. Aqui as entradas são fixas para que a saída seja reproduzível:

```python
PI = 3.14159
print(f"1) área do círculo de raio 5: {PI * 5 ** 2:.4f}")

fahrenheit = 98.6
print(f"2/3) {fahrenheit} °F = {(fahrenheit - 32) * 5 / 9:.1f} °C")

print("4) total gasto: R$", 3 * 25 + 2 * 5)
print("5) tempo:", 150 / 60, "h")

a, b = 7.0, 8.5                                 # notas (no slide, lidas com input)
print("6) média aritmética:", (a + b) / 2)
print("7) média ponderada:", (a * 4 + b * 6) / 10)

peca1, qtd1, valor1 = "parafuso", 10, 0.75
peca2, qtd2, valor2 = "porca", 20, 0.30
print(f"8) total ({peca1} e {peca2}): R$ {qtd1 * valor1 + qtd2 * valor2:.2f}")

produto, pago = 37.40, 50.00
print(f"9) troco: R$ {pago - produto:.2f}")
```

Saída esperada:

```text
1) área do círculo de raio 5: 78.5397
2/3) 98.6 °F = 37.0 °C
4) total gasto: R$ 85
5) tempo: 2.5 h
6) média aritmética: 7.75
7) média ponderada: 7.9
8) total (parafuso e porca): R$ 13.50
9) troco: R$ 12.60
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

As soluções acima são **propostas para estudo** (o material não traz gabarito). Para os desafios interativos da aula:

<details>
<summary><strong>Solução proposta para estudo</strong> — Desafios 01 a 03</summary>

<!-- norun -->
```python
# Desafio 01: boas-vindas
nome = input("Qual é o seu nome? ")
print(f"Seja bem-vindo(a), {nome}!")

# Desafio 02: data de nascimento formatada
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
print(f"Você nasceu em {dia:02d}/{mes:02d}/{ano}")

# Desafio 03: soma de dois números
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
print("Soma:", a + b)
```

`input()` sempre devolve **texto** (`str`). Sem `int()` ou `float()`, `"2" + "3"` daria `"23"`.

</details>

**Observação:** os exercícios 2 e 3 do material têm o mesmo enunciado (conversão de Fahrenheit para Celsius), provavelmente uma duplicação.

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Git e GitHub** são padrão em praticamente todas as equipes de software: versionamento, revisão de código e portfólio.
- **Python** domina ciência de dados, IA, automação e *back-end*; também roda em Raspberry Pi para projetos de IoT, como citado nos slides.
- **IDEs** aumentam a produtividade com depuração, refatoração e testes automatizados.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Instalar o Python sem "Add to PATH" | Marcar a opção na instalação | Senão o comando `python` não é reconhecido |
| Somar entradas de `input()` diretamente | Converter com `int()` ou `float()` | `input` devolve `str` |
| Usar `/` esperando um inteiro | `//` para divisão inteira | `5 / 2 = 2.5`, `5 // 2 = 2` |
| Confiar na memória para a precedência | Usar parênteses para deixar a intenção clara | "Explícito é melhor que implícito" |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Git versiona; GitHub hospeda.
- Python: alto nível, interpretado, multiplataforma, criado por Guido van Rossum.
- Tipos: `int`, `float`, `str`, `bool`, `list`.
- Operadores: `+ - * / ** // %`; precedência `()` > `**` > `* / // %` > `+ -`.
- `input()` → `str`; converta antes de calcular.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Qual o resultado de `2 + 3 * 4 ** 2`?
2. O que `print("3" * 3)` exibe?
3. Qual a diferença entre `=` e `==`?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. $4^2 = 16$; $3 \times 16 = 48$; $2 + 48 = 50$.
2. `333`, porque multiplicar uma `str` por um inteiro a repete.
3. `=` atribui um valor; `==` compara dois valores e devolve `True` ou `False`.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [Git — downloads](https://git-scm.com/downloads) · [GitHub](https://github.com/)
- [Python — downloads](https://www.python.org/downloads/) · [PEP 20 — Zen do Python](https://peps.python.org/pep-0020/)
- [PyCharm — download](https://www.jetbrains.com/pycharm/download/)
- Material da pasta: [slides](PCP%20-%20Aula%2002%20-%20Git%2C%20GitHub%20e%20Introdu%C3%A7%C3%A3o%20ao%20Python.pdf)

<br />

<p align="center"><a href="../aula02-10-03-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula04-30-03-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
