<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Mini%20CRM%20com%20Python&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=PENSAMENTO%20COMPUTACIONAL%20E%20AUTOMA%C3%87%C3%83O%20COM%20PYTHON%20%E2%80%94%20AULA%2011%20%E2%80%94%2009%2F09%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Modularização e Arquivos: Mini CRM de Leads" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=app.py%20%E2%86%92%20model.py%20%E2%86%92%20control.py%20%E2%86%92%20leads.json;json.dumps%20%2F%20json.loads;Path%28__file__%29.resolve%28%29.parent%20%2F%20%27data%27;CRUD%3A%20create%2C%20read%2C%20update%2C%20delete" alt="app.py → model.py → control.py → leads.json. json.dumps / json.loads. Path(__file__).resolve().parent / 'data'. CRUD: create, read, update, delete." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-PCP-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: PCP" />
  <img src="https://img.shields.io/badge/Aula-11-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 11" />
  <img src="https://img.shields.io/badge/Data-09--09--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 09-09-2026" />
  <img src="https://img.shields.io/badge/Linguagem-Python-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=python&amp;logoColor=white" alt="Linguagem: Python" />
  <img src="https://img.shields.io/badge/Arquitetura-Modulariza%C3%A7%C3%A3o-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Arquitetura: Modularização" />
  <img src="https://img.shields.io/badge/Persist%C3%AAncia-JSON%20e%20CSV-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Persistência: JSON e CSV" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Pensamento Computacional e Automação com Python](../README.md) |
| Aula | 11 — 09/09/2026 |
| Título | Modularização e Arquivos: Mini CRM de Leads |
| Tema central | Construção de um Mini CRM de leads em Python modular: separação em interface (app.py), modelagem (model.py) e persistência (control.py), menu com while True, dicionários como modelo de dados, JSON como formato de persistência, pathlib, tratamento de JSONDecodeError, busca e exportação para CSV. |
| Tecnologias e ferramentas | Python 3 (json, csv, pathlib, datetime) |
| Docente (conforme material) | Prof. Alexandre Russi Junior |
| Natureza do conteúdo | Aula prática com projeto de código |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`PCP - Aula 08 - Modularização e Arquivos - Mini CRM.pdf`](PCP%20-%20Aula%2008%20-%20Modulariza%C3%A7%C3%A3o%20e%20Arquivos%20-%20Mini%20CRM.pdf) | Slides (19 páginas): exemplo de CRM real, do código monolítico ao organizado, anatomia do sistema, imports, loop do menu, validação fail fast, dicionários, memória × disco, JSON, repositório, pathlib, tratamento de erros, listagem formatada e ciclo de vida do dado. |
| [`app.py`](app.py) | Interface do Mini CRM: menu em laço (adicionar, listar, buscar, exportar, sair) e funções que coletam dados e exibem resultados. |
| [`control.py`](control.py) | Persistência: caminho da pasta data com pathlib, leitura e gravação de leads.json (com tratamento de JSONDecodeError), busca por nome ou e-mail e exportação para CSV. |
| [`model.py`](model.py) | Modelagem: função model_lead que monta o dicionário do lead (nome, e-mail, status e data de criação). |
| [`data/leads.csv`](data/leads.csv) | Arquivo vazio (0 bytes): resultado da tentativa de exportação interrompida pelo erro descrito nesta página. |
| [`data/leads.json`](data/leads.json) | Base de dados em JSON com dois leads de teste gravados pelo programa. |

> [!NOTE]
> **Limitações da documentação.** Os slides são imagens (infográficos), lidos visualmente. O código da pasta foi lido integralmente e executado numa cópia temporária (o repositório não foi alterado), com entradas simuladas para listar, buscar e exportar. A opção de exportação falha por um erro no código original, documentado abaixo; os arquivos originais não foram corrigidos. A pasta __pycache__ (bytecode gerado) não é documentada.

<br />

<h2 id="visao-geral">Visão geral</h2>

A aula transforma *scripts* isolados num **sistema pequeno e organizado**: um **Mini CRM** (gestão de *leads*, isto é, potenciais clientes). A mensagem central dos slides é sair do **código monolítico**, um único arquivo que faz tudo, para o **código organizado**, em que cada arquivo tem **uma responsabilidade**.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart LR
    T["Terminal<br/>(usuário)"] --> A["app.py<br/>interface e fluxo"]
    A -->|"model_lead(...)"| M["model.py<br/>modelagem (dict)"]
    A -->|"create_lead / read_leads"| C["control.py<br/>persistência"]
    C -->|"json.dumps"| J[("data/leads.json")]
    J -->|"json.loads"| C
    C -->|"csv.DictWriter"| V[("data/leads.csv")]
```

*Figura 1 — Ciclo de vida do dado no Mini CRM. Nos slides, os módulos se chamam `stages.py` e `repo.py`, com a nota "ou: `model.py`" e "ou: `control.py`", os nomes usados no código da pasta.*

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Dividir um programa em módulos com responsabilidades claras.
- Modelar registros como dicionários.
- Persistir dados em JSON e exportar para CSV.
- Construir caminhos de arquivo robustos com `pathlib`.
- Tratar erros de leitura (arquivo ausente ou corrompido).

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- [Aula 09](../aula09-10-08-26/README.md): dicionários.
- [Aula 04](../aula04-30-03-26/README.md): funções e módulos; [aula 05](../aula05-04-04-26/README.md): laços.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Conceitos dos slides

| Conceito | No Mini CRM |
| :--- | :--- |
| **Modularização** | `app.py` (interface), `model.py` (modelo), `control.py` (dados) |
| **Importar o próprio código** | `from model import model_lead` e `import control` |
| **`if __name__ == "__main__"`** | Evita que o menu rode ao importar `app.py` em outro módulo |
| **Loop de interação** | `while True` com `if`/`elif` por opção e `break` para sair |
| **Fail fast** | Validar a entrada logo no início; a busca vazia é rejeitada ("Consulta vazia") |
| **Memória × disco** | Na RAM, os dados somem ao fechar o programa; no disco, persistem |
| **JSON** | `json.dumps` serializa (dict → texto); `json.loads` desserializa |
| **Repositório** | `app.py` só pede "salve"; o **como** fica escondido em `control.py` |
| **`pathlib`** | `Path(__file__).resolve().parent / "data"` encontra a pasta independentemente de onde o terminal foi aberto |
| **Tratamento de erros** | `except json.JSONDecodeError: return []`: o sistema sobrevive a um arquivo corrompido |
| **CRUD** | *Create*, *Read*, *Update*, *Delete*; o projeto implementa *Create* e *Read* (com busca) |

### 2. O modelo de dados

```python
from datetime import date

def model_lead(name, email, status):
    return {"name": name, "email": email, "status": status,
            "created": date.today().isoformat()}
```

Exemplo de retorno (a data varia conforme o dia da execução):

<!-- norun -->
```text
{'name': 'Ana', 'email': 'ana@exemplo.com', 'status': 'novo', 'created': '2026-09-10'}
```

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — executando o programa da pasta

Execução de uma **cópia** do código (`app.py`, `control.py`, `model.py` e `leads.json`) com as opções 2 (listar), 3 (buscar "ren") e 4 (exportar):

<!-- norun -->
```text
Escolha uma opção: ## | Nome       | E-mail
00 | Alexandre  | a@b.com
01 | renan      | e@e.com
...
Escolha uma opção: Buscar por: ## | Nome       | E-mail
01 | renan      | e@e.com
...
Escolha uma opção: Traceback (most recent call last):
  ...
  File ".../control.py", line 52, in export_csv
    writer = csv.DictWriter(file_csv, lead[0].keys())
NameError: name 'lead' is not defined. Did you mean: 'leads'?
```

> [!WARNING]
> **Erro na exportação (`control.py`, linha 52).** O código usa `lead[0].keys()`, mas a variável se chama `leads`. Como o arquivo CSV é aberto **antes** da linha com erro, ele é criado **vazio** e o programa termina com `NameError`, que não é capturado (só `PermissionError` é). Isso explica o `data/leads.csv` de 0 bytes da pasta. A correção sugerida é usar `leads[0].keys()` e tratar a lista vazia antes de abrir o arquivo. O código original **não foi alterado**.

> [!NOTE]
> **Compatibilidade.** `app.py` usa aspas duplas dentro de *f-strings* delimitadas por aspas duplas (`f"## | {"Nome":<10} | E-mail"`). Isso só é válido a partir do **Python 3.12** (PEP 701); em versões anteriores gera `SyntaxError`. A execução acima usou Python 3.13.

### Exemplo aplicado — a lógica de `control.py` com a exportação corrigida

Demonstração autocontida numa pasta temporária, com a mesma lógica do módulo original e a exportação corrigida:

```python
import csv, json, tempfile
from pathlib import Path

# mesma lógica de control.py, apontando para uma pasta temporária
DATA_DIR = Path(tempfile.mkdtemp()) / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

def read_leads():
    if not DB_PATH.exists():
        return []
    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:                  # arquivo corrompido: recomeça com lista vazia
        return []

def create_lead(lead):
    leads = read_leads()
    leads.append(lead)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

def read_leads_search(query):
    return [(i, l) for i, l in enumerate(read_leads()) if query.lower() in f"{l['name']} {l['email']}".lower()]

def export_csv():
    leads = read_leads()
    if not leads:                                 # sem leads não há cabeçalho para escrever
        return None
    path_csv = DATA_DIR / "leads.csv"
    with path_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, leads[0].keys())   # o original usa lead[0] (NameError)
        writer.writeheader()
        writer.writerows(leads)
    return path_csv

print("vazio:", read_leads(), "| export:", export_csv())
create_lead({"name": "Ana", "email": "ana@exemplo.com", "status": "novo", "created": "2026-09-10"})
create_lead({"name": "Bruno", "email": "bruno@exemplo.com", "status": "contato", "created": "2026-09-10"})
print(f"## | {'Nome':<10} | E-mail")
for i, lead in enumerate(read_leads()):
    print(f"{i:02d} | {lead['name']:<10} | {lead['email']}")
print("busca 'bru':", read_leads_search("bru"))
print(export_csv().read_text(encoding="utf-8"), end="")
DB_PATH.write_text("{ isto não é JSON", encoding="utf-8")
print("JSON corrompido ->", read_leads())
```

Saída esperada:

```text
vazio: [] | export: None
## | Nome       | E-mail
00 | Ana        | ana@exemplo.com
01 | Bruno      | bruno@exemplo.com
busca 'bru': [(1, {'name': 'Bruno', 'email': 'bruno@exemplo.com', 'status': 'contato', 'created': '2026-09-10'})]
name,email,status,created
Ana,ana@exemplo.com,novo,2026-09-10
Bruno,bruno@exemplo.com,contato,2026-09-10
JSON corrompido -> []
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

O material não traz exercícios formais. **Exercício proposto para estudo:** complete o CRUD com uma função `update_status(indice, novo_status)` em `control.py`.

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

<!-- norun -->
```python
# em control.py
def update_status(indice, novo_status):
    leads = read_leads()
    if not 0 <= indice < len(leads):
        return False                      # fail fast: índice inválido
    leads[indice]["status"] = novo_status
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")
    return True
```

Em `app.py`, uma nova opção do menu pede o índice (mostrado na listagem) e o novo status, e informa se a atualização foi feita. O *Delete* segue o mesmo padrão, com `leads.pop(indice)`.

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **CRMs reais**, como o mostrado no primeiro slide, organizam *leads* em funis de vendas. O Mini CRM reproduz o núcleo: cadastrar, listar, buscar e exportar.
- **Arquitetura em camadas** (interface, regras e dados) é o padrão de sistemas *web* e de *back-end*, com *frameworks*, APIs e bancos de dados, como indica o slide final "O que realmente construímos hoje?".
- **JSON** é o formato usado por praticamente todas as APIs *web*.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Um arquivo que faz tudo | Módulos com responsabilidade única | Manutenção e testes |
| Caminhos relativos ao terminal (`"data/leads.json"`) | `Path(__file__).resolve().parent` | Funciona de qualquer diretório |
| Capturar só alguns erros e deixar o programa cair | Tratar os erros previsíveis e testar as opções do menu | O erro da exportação passaria num teste simples |
| Abrir o arquivo de saída antes de validar os dados | Validar (lista vazia?) e só então abrir | Evita arquivos vazios ou corrompidos |
| `json.dumps` sem `ensure_ascii=False` | Manter `ensure_ascii=False` | Preserva acentos legíveis no arquivo |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Mini CRM: `app.py` (menu e interface) → `model.py` (dicionário do lead) → `control.py` (JSON e CSV).
- `json.dumps`/`json.loads`; `csv.DictWriter`; `pathlib.Path`.
- `if __name__ == "__main__"`; `while True` com `break`; *fail fast*; `try`/`except`.
- Erro conhecido: `lead[0]` → `leads[0]` na exportação.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Por que separar `control.py` de `app.py`?
2. O que acontece se `leads.json` estiver corrompido?
3. Para que serve `if __name__ == "__main__":`?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. Para que a interface não precise saber como os dados são salvos: trocar JSON por um banco de dados mudaria só `control.py`.
2. `json.loads` lança `JSONDecodeError`, que é capturado; `read_leads` devolve uma lista vazia e o sistema continua.
3. Para executar `main()` apenas quando o arquivo é rodado diretamente, e não quando é importado por outro módulo.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [Python — `json`](https://docs.python.org/pt-br/3/library/json.html) · [`csv`](https://docs.python.org/pt-br/3/library/csv.html) · [`pathlib`](https://docs.python.org/pt-br/3/library/pathlib.html)
- [PEP 701 — *f-strings* sintáticas](https://peps.python.org/pep-0701/)
- Materiais da pasta: [slides](PCP%20-%20Aula%2008%20-%20Modulariza%C3%A7%C3%A3o%20e%20Arquivos%20-%20Mini%20CRM.pdf) · [app.py](app.py) · [control.py](control.py) · [model.py](model.py)

<br />

<p align="center"><a href="../aula10-16-08-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula12-23-09-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
