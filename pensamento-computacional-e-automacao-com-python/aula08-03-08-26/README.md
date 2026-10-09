<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Revis%C3%A3o%3A%20API%20em%20Alerta&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=PENSAMENTO%20COMPUTACIONAL%20E%20AUTOMA%C3%87%C3%83O%20COM%20PYTHON%20%E2%80%94%20AULA%2008%20%E2%80%94%2003%2F08%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Retomada do 2º Semestre: Avisos do Challenge, Desafio API em Alerta e Revisão" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=Linha%20%3D%20endpoint%2C%20coluna%20%3D%20requisi%C3%A7%C3%A3o;Sucesso%3A%20c%C3%B3digo%20HTTP%20entre%20200%20e%20299;EST%C3%81VEL%20%E2%89%A5%2080%25%20%C2%B7%20INST%C3%81VEL%20%C2%B7%20CR%C3%8DTICO;Revis%C3%A3o%3A%20while%2C%20for%2C%20listas%20e%20matrizes" alt="Linha = endpoint; coluna = requisição. Sucesso: código HTTP entre 200 e 299. ESTÁVEL ≥ 80% · INSTÁVEL · CRÍTICO. Revisão: while, for, listas e matrizes." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-PCP-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: PCP" />
  <img src="https://img.shields.io/badge/Aula-08-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 08" />
  <img src="https://img.shields.io/badge/Data-03--08--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 03-08-2026" />
  <img src="https://img.shields.io/badge/Linguagem-Python-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=python&amp;logoColor=white" alt="Linguagem: Python" />
  <img src="https://img.shields.io/badge/Desafio-API%20em%20Alerta-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Desafio: API em Alerta" />
  <img src="https://img.shields.io/badge/Contexto-Challenge%20GoodWe-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Contexto: Challenge GoodWe" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Pensamento Computacional e Automação com Python](../README.md) |
| Aula | 08 — 03/08/2026 |
| Título | Retomada do 2º Semestre: Avisos do Challenge, Desafio API em Alerta e Revisão |
| Tema central | Avisos do Challenge GoodWe (mentorias, bancas, NEXT), calendário de checkpoints, sprints e Global Solution do 2º semestre; desafio de revisão “API em Alerta” com matriz de códigos HTTP; exercícios de revisão do 1º semestre. |
| Tecnologias e ferramentas | Python 3 |
| Docente (conforme material) | Prof. Alexandre Russi Junior |
| Natureza do conteúdo | Avisos, desafio de revisão e exercícios |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`PCP - Aula 06 - GoodWe avisos, Matrizes e Exercícios.pdf`](PCP%20-%20Aula%2006%20-%20GoodWe%20avisos%2C%20Matrizes%20e%20Exerc%C3%ADcios.pdf) | Slides (21 páginas): avisos do Challenge GoodWe (mentorias, bancas, NEXT), calendário de CPs, sprints e GS do 2º semestre, sugestão de estudo de APIs, desafio “API em Alerta” e oito exercícios de revisão. |

> [!NOTE]
> **Limitações da documentação.** Os slides trazem aviso de direitos autorais; o conteúdo é explicado com redação própria. Datas do calendário são as informadas nos slides, que alertam estarem sujeitas a modificação. O desafio não tem gabarito: a solução é proposta e foi executada. Os exercícios 1 a 8 repetem enunciados das aulas 05 e 07 e remetem às soluções dessas páginas.

<br />

<h2 id="visao-geral">Visão geral</h2>

A primeira aula do 2º semestre combina **organização** e **revisão**: os avisos do Challenge GoodWe e o calendário de avaliações, um desafio integrador sobre **matrizes**, o **"API em Alerta"**, e exercícios que retomam os laços e as listas do 1º semestre.

**Calendário informado nos slides** (todas as datas sujeitas a modificação):

| Item | Data |
| :--- | :--- |
| Vídeo *pitch*/técnico (3 min), entregue como CP1 | até 28/08 |
| CP2 | semana de 31/08 e 01/09 |
| Sprint 3 | 05/09 a 30/09 |
| Banca remota (classificação para o NEXT) | semana de 28/09 |
| Sprint 4 | 01/10 a 31/10 |
| CP3 | semana de 13/10 (19/10 para algumas turmas) |
| Banca presencial (TOP 3) | semana de 19/10 |
| NEXT (feira de projetos da FIAP) | 24/10 (sábado) |
| Global Solution | 04/11 a 19/11 |

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Organizar as entregas do 2º semestre.
- Processar uma matriz linha a linha com funções.
- Aplicar regras de classificação sobre dados (porcentagens, erros consecutivos).
- Revisar laços, listas e matrizes.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 05](../aula05-04-04-26/README.md) (laços) e [aula 07](../aula07-26-04-26/README.md) (listas e matrizes).
- Noção de códigos de status HTTP (2xx sucesso, 4xx erro do cliente, 5xx erro do servidor). Os slides sugerem pesquisar APIs como estudo extra.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### O desafio "API em Alerta"

Uma API tem três *endpoints*. A matriz `status` registra os códigos HTTP das últimas requisições: **cada linha é um endpoint e cada coluna, uma requisição**.

| Endpoint | Req. 1 | Req. 2 | Req. 3 | Req. 4 | Req. 5 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `/login` | 200 | 200 | 401 | 200 | 500 |
| `/produtos` | 200 | 200 | 200 | 200 | 200 |
| `/pedidos` | 201 | 500 | 502 | 201 | 500 |

**O programa deve:**

1. calcular a porcentagem de sucesso de cada endpoint, considerando sucesso um código de 200 a 299;
2. identificar o endpoint com mais erros;
3. verificar se houve dois erros seguidos;
4. classificar cada endpoint como **ESTÁVEL** (≥ 80% de sucesso), **INSTÁVEL** (< 80%) ou **CRÍTICO** (dois erros consecutivos).

Requisitos: usar pelo menos uma **função** e funcionar com **novos endpoints ou requisições**, sem números fixos no código.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart TD
    M["Matriz status"] --> L["Para cada linha (endpoint)"]
    L --> A["analisar(códigos)"]
    A --> P["% sucesso"]
    A --> E["nº de erros"]
    A --> S["erros consecutivos?"]
    S -->|"sim"| C["CRÍTICO"]
    S -->|"não"| Q{"% ≥ 80?"}
    Q -->|"sim"| ES["ESTÁVEL"]
    Q -->|"não"| IN["INSTÁVEL"]
```

*Figura 1 — Estrutura da solução proposta. A regra CRÍTICO é testada primeiro, por ser a mais grave.*

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo — solução proposta para o desafio

```python
endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500],
]

def sucesso(codigo):
    return 200 <= codigo <= 299

def analisar(codigos):
    ok = sum(sucesso(c) for c in codigos)
    pct = 100 * ok / len(codigos)
    erros = len(codigos) - ok
    seguidos = any(not sucesso(a) and not sucesso(b) for a, b in zip(codigos, codigos[1:]))
    if seguidos:
        classe = "CRÍTICO"
    elif pct >= 80:
        classe = "ESTÁVEL"
    else:
        classe = "INSTÁVEL"
    return pct, erros, seguidos, classe

resultados = {ep: analisar(cod) for ep, cod in zip(endpoints, status)}
for ep, (pct, erros, seguidos, classe) in resultados.items():
    print(f"{ep:<10} sucesso {pct:5.1f}% | erros {erros} | dois seguidos: {seguidos} | {classe}")
print("mais erros:", max(resultados, key=lambda ep: resultados[ep][1]))
```

Saída esperada:

```text
/login     sucesso  60.0% | erros 2 | dois seguidos: False | INSTÁVEL
/produtos  sucesso 100.0% | erros 0 | dois seguidos: False | ESTÁVEL
/pedidos   sucesso  40.0% | erros 3 | dois seguidos: True | CRÍTICO
mais erros: /pedidos
```

**Pontos de projeto:**

- `zip(codigos, codigos[1:])` forma os pares de requisições **vizinhas**, o que torna fácil detectar dois erros seguidos.
- Nada depende do número de endpoints ou de colunas: novos dados funcionam sem alterar o código.
- Em `/login`, os erros (401 e 500) **não** são consecutivos, por isso o endpoint é INSTÁVEL, e não CRÍTICO.

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

Os oito exercícios de revisão repetem enunciados já resolvidos nesta documentação (**soluções propostas para estudo**):

| Exercício | Tema | Onde está a solução |
| :--- | :--- | :--- |
| 1 | `while` com pergunta ao usuário | [Aula 05](../aula05-04-04-26/README.md#exercicios-resolvidos) |
| 2 | Contagem de 0 a 100 de 10 em 10 | [Aula 05](../aula05-04-04-26/README.md#exemplos-praticos) |
| 3 | Soma de 1 a n com validação | [Aula 05](../aula05-04-04-26/README.md#exemplos-praticos) |
| 4 | Divisores de n | [Aula 05](../aula05-04-04-26/README.md#exemplos-praticos) |
| 5 | Primos de 2 a 2000 | [Aula 05](../aula05-04-04-26/README.md#exemplos-praticos) |
| 6 | Vetor de reais aleatórios | [Aula 07](../aula07-26-04-26/README.md#exemplos-praticos) |
| 7 | Inversão de vetor | [Aula 07](../aula07-26-04-26/README.md#exemplos-praticos) |
| 8 | Soma de matrizes | [Aula 07](../aula07-26-04-26/README.md#exemplos-praticos) |

**Exercício proposto para estudo:** estenda o desafio para informar, para cada endpoint, **qual requisição** (número da coluna) teve o primeiro erro.

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

```python
status = {"/login": [200, 200, 401, 200, 500], "/produtos": [200] * 5, "/pedidos": [201, 500, 502, 201, 500]}
for ep, cods in status.items():
    primeiro = next((i + 1 for i, c in enumerate(cods) if not 200 <= c <= 299), None)
    print(ep, "-> primeiro erro na requisição", primeiro)
```

Saída esperada:

```text
/login -> primeiro erro na requisição 3
/produtos -> primeiro erro na requisição None
/pedidos -> primeiro erro na requisição 2
```

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Observabilidade e SRE:** monitorar taxas de erro por endpoint e disparar alertas para padrões como erros consecutivos é rotina em equipes de operação (Grafana, Datadog, Prometheus).
- **Acordos de nível de serviço (SLA):** classificações como "estável ≥ 80%" se parecem com metas de disponibilidade.
- **Challenge e NEXT:** apresentar um projeto técnico em *pitch* curto é uma habilidade valorizada no mercado.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Fixar `range(3)` e `range(5)` no código | Usar `len` e iteração direta | Requisito do desafio: aceitar novos dados |
| Testar só `== 200` | Faixa `200 <= c <= 299` | 201 também é sucesso |
| Classificar sem prioridade | Testar CRÍTICO antes de ESTÁVEL | Um endpoint com ≥ 80% ainda pode ter erros seguidos |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- 2º semestre: CPs, Sprints 3 e 4, bancas, NEXT (24/10) e GS (04 a 19/11), com datas sujeitas a mudança.
- Matriz linha = entidade, coluna = observação; processe linha a linha com funções.
- Sucesso HTTP: 2xx; erros consecutivos com `zip(lista, lista[1:])`.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Qual a porcentagem de sucesso de `/pedidos`?
2. Por que `/login` não é CRÍTICO?
3. O que `zip([1, 2, 3], [2, 3])` produz?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. 40%: 2 sucessos (201 e 201) em 5 requisições.
2. Porque os erros, nas requisições 3 e 5, não são vizinhos.
3. Os pares `(1, 2)` e `(2, 3)`: os vizinhos consecutivos.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [MDN — códigos de status HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status)
- [FIAP NEXT](https://www.fiap.com.br/next/), citado nos slides.
- Material da pasta: [slides](PCP%20-%20Aula%2006%20-%20GoodWe%20avisos%2C%20Matrizes%20e%20Exerc%C3%ADcios.pdf)

<br />

<p align="center"><a href="../aula07-26-04-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula09-10-08-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
