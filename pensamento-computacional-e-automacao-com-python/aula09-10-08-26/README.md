<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Dicion%C3%A1rios%20e%20Tuplas&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=PENSAMENTO%20COMPUTACIONAL%20E%20AUTOMA%C3%87%C3%83O%20COM%20PYTHON%20%E2%80%94%20AULA%2009%20%E2%80%94%2010%2F08%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Dicionários e Tuplas" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=eng2sp%5B%27one%27%5D%20%3D%20%27uno%27;%27uno%27%20in%20eng2sp.values%28%29;contagem%5Bc%5D%20%3D%20contagem.get%28c%2C%200%29%20%2B%201;a%2C%20b%20%3D%20b%2C%20a%20%28atribui%C3%A7%C3%A3o%20de%20tupla%29" alt="eng2sp['one'] = 'uno'. 'uno' in eng2sp.values(). contagem[c] = contagem.get(c, 0) + 1. a, b = b, a (atribuição de tupla)." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-PCP-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: PCP" />
  <img src="https://img.shields.io/badge/Aula-09-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 09" />
  <img src="https://img.shields.io/badge/Data-10--08--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 10-08-2026" />
  <img src="https://img.shields.io/badge/Linguagem-Python-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=python&amp;logoColor=white" alt="Linguagem: Python" />
  <img src="https://img.shields.io/badge/Estruturas-dict%20%C2%B7%20tuple-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Estruturas: dict · tuple" />
  <img src="https://img.shields.io/badge/Desafio-Analisador%20de%20e--mails-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Desafio: Analisador de e-mails" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Pensamento Computacional e Automação com Python](../README.md) |
| Aula | 09 — 10/08/2026 |
| Título | Dicionários e Tuplas |
| Tema central | Dicionários como mapeamentos chave-valor (dict(), inserção, operador in, values), dicionário como coleção de contadores (histograma de letras), tuplas como sequências imutáveis e atribuição de tupla, com o desafio “Analisador de e-mails da FIAP”. |
| Tecnologias e ferramentas | Python 3 |
| Docente (conforme material) | Prof. Alexandre Russi Junior |
| Natureza do conteúdo | Aula prática com desafio |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`PCP - Aula 07 - Dicionários e Tuplas.pdf`](PCP%20-%20Aula%2007%20-%20Dicion%C3%A1rios%20e%20Tuplas.pdf) | Slides (12 páginas): dicionários (criação, inserção, operador in, values), dicionário como coleção de contadores, tuplas imutáveis e o desafio “Analisador de e-mails da FIAP” com dicas. |

> [!NOTE]
> **Limitações da documentação.** Os slides trazem aviso de direitos autorais; o conteúdo é explicado com redação própria. O código aparece em imagens, lidas visualmente. O desafio não tem gabarito: a solução é proposta e executada; uma ambiguidade do enunciado é comentada.

<br />

<h2 id="visao-geral">Visão geral</h2>

Duas novas estruturas completam as coleções básicas de Python:

| Estrutura | Índices | Mutável? | Uso típico |
| :--- | :--- | :---: | :--- |
| Lista | Inteiros (0, 1, 2…) | Sim | Sequência de itens |
| **Dicionário** | **Chaves** de (quase) qualquer tipo | Sim | Mapeamento chave → valor |
| **Tupla** | Inteiros | **Não** | Registro fixo, retorno múltiplo, troca de variáveis |

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Criar dicionários, inserir e consultar pares chave-valor.
- Usar `in` com chaves e com `values()`.
- Contar ocorrências com dicionários.
- Criar tuplas, entender a imutabilidade e usar a atribuição de tupla.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 07](../aula07-26-04-26/README.md): listas e índices.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Dicionários

Um dicionário é um **mapeamento**: um conjunto de **chaves**, cada uma associada a um único **valor**. Cada associação é um **item** (par chave-valor).

| Operação | Código | Observação |
| :--- | :--- | :--- |
| Criar vazio | `dict()` ou `{}` | Evite usar `dict` como nome de variável |
| Inserir ou alterar | `d['one'] = 'uno'` | |
| Ler | `d['one']` ou `d.get('one', padrão)` | `get` não gera erro se a chave faltar |
| Testar chave | `'one' in d` | O `in` verifica **chaves**, e não valores |
| Testar valor | `'uno' in d.values()` | |

### 2. Três formas de contar letras (slides)

1. 26 variáveis, uma por letra, com condicionais encadeadas.
2. Uma lista de 26 posições, convertendo letras em índices com `ord`.
3. **Um dicionário** com as letras como chaves e os contadores como valores.

A terceira é a mais simples e só ocupa espaço com as letras que **realmente** aparecem. Mesmo cálculo, **implementações** diferentes, e algumas são melhores que outras.

### 3. Tuplas

Uma tupla é uma sequência de valores separados por vírgulas, indexada como uma lista, mas **imutável**. A **atribuição de tupla** permite trocar valores sem variável temporária: `a, b = b, a`.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart LR
    E["'joao.silva@fiap.com.br'"] -->|"split('@')"| T["('joao.silva', 'fiap.com.br')"]
    T --> U["usuário → lista → tuple"]
    T --> D["domínio → dicionário de contagem"]
```

*Figura 1 — O desafio combina `split`, tuplas e dicionários.*

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — dicionários, histograma e tuplas

```python
eng2sp = dict()
eng2sp["one"] = "uno"
eng2sp.update({"two": "dos", "three": "tres"})
print(eng2sp, len(eng2sp))
print("one" in eng2sp, "uno" in eng2sp, "uno" in eng2sp.values())

def histograma(texto):
    contagem = {}
    for c in texto:
        contagem[c] = contagem.get(c, 0) + 1
    return contagem

print(histograma("brontossauro"))

t = ("a", "b", "c")
try:
    t[0] = "z"
except TypeError as erro:
    print("tupla é imutável:", erro)
x, y = 1, 2
x, y = y, x                                      # troca por atribuição de tupla
print(x, y)
```

Saída esperada:

```text
{'one': 'uno', 'two': 'dos', 'three': 'tres'} 3
True False True
{'b': 1, 'r': 2, 'o': 3, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 1}
tupla é imutável: 'tuple' object does not support item assignment
2 1
```

### Exemplo aplicado — "Analisador de e-mails da FIAP"

Solução proposta, com a entrada de exemplo do slide fixada no código:

```python
entrada = "joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br"

usuarios, por_dominio = [], {}
for email in entrada.split(","):
    usuario, dominio = email.strip().split("@")
    usuarios.append(usuario)
    por_dominio[dominio] = por_dominio.get(dominio, 0) + 1

usuarios = tuple(sorted(usuarios))              # o exemplo do slide mostra os nomes em ordem alfabética
print("Primeiro:", usuarios[0], "| Último:", usuarios[-1])

lista = list(usuarios)                          # tuplas são imutáveis: troca feita numa lista
lista[0], lista[-1] = lista[-1], lista[0]       # atribuição de tupla, sem variável temporária
trocada = tuple(lista)

print("Relatório:")
print("Quantidade de e-mails por domínio:")
for dominio, qtd in por_dominio.items():
    print(f"  {dominio}: {qtd}")
print("Lista de usuários:", usuarios)
print("Após troca de posições:", trocada)
```

Saída esperada:

```text
Primeiro: ana.paula | Último: maria.souza
Relatório:
Quantidade de e-mails por domínio:
  fiap.com.br: 3
Lista de usuários: ('ana.paula', 'joao.silva', 'maria.souza')
Após troca de posições: ('maria.souza', 'joao.silva', 'ana.paula')
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

A solução acima é **proposta para estudo**: o material traz a saída esperada, mas não o código.

> [!NOTE]
> **Dois detalhes do enunciado.**
>
> - O relatório de exemplo mostra os usuários em **ordem alfabética**, embora a entrada esteja em outra ordem. A solução ordena com `sorted` para reproduzir o exemplo.
> - O enunciado pede para "trocar a ordem do primeiro e do último" na **tupla**, mas tuplas são **imutáveis**: `t[0] = ...` gera `TypeError`. A troca é feita numa lista com atribuição de tupla (`lista[0], lista[-1] = lista[-1], lista[0]`), convertida depois em uma nova tupla.

**Exercício proposto para estudo:** conte quantas palavras de uma frase começam com cada letra.

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

```python
frase = "Python para pessoas que programam pela primeira vez"
iniciais = {}
for palavra in frase.lower().split():
    iniciais[palavra[0]] = iniciais.get(palavra[0], 0) + 1
print(iniciais)
```

Saída esperada:

```text
{'p': 6, 'q': 1, 'v': 1}
```

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **JSON e APIs:** respostas de APIs viram dicionários em Python; o Mini CRM da [aula 11](../aula11-09-09-26/README.md) grava leads em JSON.
- **Contagens e agregações:** frequência de palavras, e-mails por domínio, vendas por produto.
- **Tuplas:** retorno de múltiplos valores por funções e chaves compostas em dicionários.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| `d[chave] += 1` sem a chave existir | `d.get(chave, 0) + 1` | Evita `KeyError` |
| `valor in d` para procurar um valor | `valor in d.values()` | `in` testa chaves |
| Nomear uma variável `dict` | Nomes como `contagem` ou `eng2sp` | Esconde a função integrada |
| Tentar alterar uma tupla | Criar uma nova tupla ou usar lista | Tuplas são imutáveis |
| Dividir e-mails sem `strip()` | `email.strip().split("@")` | A entrada separada por ", " deixa espaços |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- `dict`: chave → valor; `in` testa chaves; `.get`, `.values()`, `.items()`.
- Contagem: `d[k] = d.get(k, 0) + 1`.
- `tuple`: sequência imutável; `a, b = b, a` troca valores.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. O que `{"a": 1, "b": 2}.get("c", 0)` devolve?
2. `(1, 2, 3)[1] = 5` funciona?
3. Como percorrer chaves e valores de um dicionário ao mesmo tempo?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. `0`, o valor padrão, pois a chave `"c"` não existe.
2. Não: gera `TypeError`, porque tuplas são imutáveis.
3. `for chave, valor in d.items():`.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [Python — dicionários](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries) · [tuplas](https://docs.python.org/pt-br/3/tutorial/datastructures.html#tuples-and-sequences)
- Material da pasta: [slides](PCP%20-%20Aula%2007%20-%20Dicion%C3%A1rios%20e%20Tuplas.pdf)

<br />

<p align="center"><a href="../aula08-03-08-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula10-16-08-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
