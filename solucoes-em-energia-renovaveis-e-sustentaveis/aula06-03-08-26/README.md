<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Orange%20%2B%20pandas&amp;fontSize=40&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=SOLU%C3%87%C3%95ES%20EM%20ENERGIAS%20RENOV%C3%81VEIS%20E%20SUSTENT%C3%81VEIS%20%E2%80%94%20AULA%2006%20%E2%80%94%2003%2F08%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Dados de Consumo Residencial: Preparação no Orange e Análise Exploratória Preliminar" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=Orange%3A%20importar%20%E2%86%92%20limpar%20%E2%86%92%20amostrar%20%E2%86%92%20salvar;40.986%20registros%20%C3%97%209%20atributos;head%20%C2%B7%20shape%20%C2%B7%20info%20%C2%B7%20describe;Pot%C3%AAncia%20ativa%20m%C3%A9dia%20%E2%89%88%201%2C1%20kW" alt="Orange: importar → limpar → amostrar → salvar. 40.986 registros × 9 atributos. head · shape · info · describe. Potência ativa média ≈ 1,1 kW." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-SERS-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: SERS" />
  <img src="https://img.shields.io/badge/Aula-06-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 06" />
  <img src="https://img.shields.io/badge/Data-03--08--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 03-08-2026" />
  <img src="https://img.shields.io/badge/Ferramenta-Orange-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Ferramenta: Orange" />
  <img src="https://img.shields.io/badge/Biblioteca-pandas-FF4500?style=for-the-badge&amp;labelColor=0D1117&amp;logo=pandas&amp;logoColor=white" alt="Biblioteca: pandas" />
  <img src="https://img.shields.io/badge/Dataset-UCI%20household%20power-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Dataset: UCI household power" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Soluções em Energias Renováveis e Sustentáveis](../README.md) |
| Aula | 06 — 03/08/2026 |
| Título | Dados de Consumo Residencial: Preparação no Orange e Análise Exploratória Preliminar |
| Tema central | Preparação do conjunto Individual Household Electric Power Consumption (UCI) no Orange Data Mining (importar, eliminar valores ausentes, amostrar 2% e salvar CSV) e primeira inspeção da amostra com pandas: head(), shape, info() e describe(); leitura das variáveis elétricas e problemas de qualidade na coluna Time. |
| Tecnologias e ferramentas | Orange Data Mining 3, Python 3, pandas (Google Colab) |
| Natureza do conteúdo | Aula prática (workflow do Orange, notebook e dataset) |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`ANÁLISE_DADOS_ENERGIA.ipynb`](AN%C3%81LISE_DADOS_ENERGIA.ipynb) | Notebook “Análise exploratória preliminar”: importa o pandas, lê SAMPLE_ENERGY_DATA.csv e mostra head(), shape (40.986 × 9), info() e describe(), com as saídas salvas. |
| [`SAMPLE_ENERGY_DATA.csv`](SAMPLE_ENERGY_DATA.csv) | Amostra de 40.986 registros e 9 colunas (Date, Time, Global_active_power, Global_reactive_power, Voltage, Global_intensity e Sub_metering_1 a 3) gerada pelo workflow do Orange; a coluna Time traz a data 2026-08-03 antes do horário em todos os registros. |
| [`Workflow_Orange.ows`](Workflow_Orange.ows) | Workflow do Orange Data Mining com 8 widgets: CSV File Import, Data Table e Data Info para os dados brutos; Preprocess para eliminar valores ausentes; Data Sampler com 2% dos registros; Data Table, Data Info e Save Data para a amostra, com anotações de cada etapa. |

> [!NOTE]
> **Limitações da documentação.** O notebook (7 células) foi lido com as saídas salvas, e o workflow do Orange (.ows) foi lido como XML; o Orange não está instalado neste ambiente e o workflow não foi aberto. O arquivo bruto RAW_ENERGY_DATA.txt, usado pelo workflow, não está no repositório (passa de 100 MB e está no .gitignore), por isso a etapa do Orange não foi reproduzida. Os cálculos complementares desta página foram executados sobre SAMPLE_ENERGY_DATA.csv. As unidades das variáveis e o tamanho do conjunto original vêm da descrição do dataset na UCI, não do material da aula. O workflow registra um caminho local de um computador do laboratório, que não é reproduzido.

<br />

<h2 id="visao-geral">Visão geral</h2>

O 2º semestre de SERS começa pela **análise de dados de energia**. A turma trabalha com um conjunto público de medições elétricas de uma residência, o ***Individual Household Electric Power Consumption***, da UCI. O arquivo original é grande demais para ser manipulado com conforto em sala, então o fluxo tem duas etapas:

1. no **Orange Data Mining**, uma ferramenta visual, os dados brutos são importados, limpos e reduzidos a uma **amostra aleatória de 2%**, salva em CSV;
2. no **Python com pandas**, a amostra é carregada e inspecionada.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart LR
    RAW["RAW_ENERGY_DATA.txt<br/>(dados brutos, sep. ';')"] --> CSV["CSV File Import"]
    CSV --> DT1["Data Table<br/>Data Info"]
    CSV --> PRE["Preprocess<br/>elimina valores ausentes"]
    PRE --> DT2["Data Table (1)"]
    PRE --> SMP["Data Sampler<br/>2% aleatório"]
    SMP --> DI2["Data Info (1)"]
    SMP --> SAVE["Save Data<br/>SAMPLE_ENERGY_DATA.csv"]
    SAVE --> NB["Notebook pandas<br/>head · shape · info · describe"]
```

*Figura 1 — O workflow `Workflow_Orange.ows` e a passagem para o notebook. As anotações do workflow dizem: "carregar dados brutos", "eliminar células com valores ausentes", "gerar uma amostra aleatória de 2% dos dados originais" e "salvar um arquivo .CSV da amostra".*

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Montar no Orange um fluxo de importação, limpeza, amostragem e exportação de dados.
- Explicar por que trabalhar com uma amostra aleatória antes de usar o conjunto completo.
- Carregar um CSV no pandas e inspecioná-lo com `head()`, `shape`, `info()` e `describe()`.
- Interpretar as variáveis elétricas do conjunto e suas estatísticas.
- Identificar problemas de qualidade, como a data inserida na coluna `Time`.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- Potência ativa e reativa, tensão, corrente e fator de potência, da [aula 04](../aula04-19-03-26/README.md).
- Python básico e noções de tabelas (linhas e colunas).

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. O conjunto de dados

Segundo a descrição da UCI, o conjunto reúne medições **a cada minuto** do consumo elétrico de **uma única residência**, de dezembro de 2006 a novembro de 2010, com cerca de 2 milhões de registros e uma pequena parcela de valores ausentes. As colunas são:

| Coluna | Significado | Unidade (UCI) |
| :--- | :--- | :--- |
| `Date`, `Time` | data e hora da medição | — |
| `Global_active_power` | potência ativa média no minuto | kW |
| `Global_reactive_power` | potência reativa média no minuto | kVAr |
| `Voltage` | tensão média | V |
| `Global_intensity` | corrente média | A |
| `Sub_metering_1` | energia da cozinha | Wh |
| `Sub_metering_2` | energia da lavanderia | Wh |
| `Sub_metering_3` | energia do aquecedor de água e do ar-condicionado | Wh |

### 2. Por que o Orange e por que uma amostra

O **Orange Data Mining** monta análises ligando *widgets* com o mouse, sem programar. Isso torna visível cada etapa da preparação. A **amostra aleatória** de 2% mantém o comportamento geral dos dados com uma fração do tamanho, o que agiliza a exploração. A amostra tem 40.986 registros, compatível com 2% dos registros completos do conjunto original.

### 3. Os quatro comandos de inspeção

| Comando | O que mostra | Resultado registrado no notebook |
| :--- | :--- | :--- |
| `dados.head()` | as 5 primeiras linhas | registros de datas variadas, em ordem aleatória |
| `dados.shape` | (linhas, colunas) | `(40986, 9)` |
| `dados.info()` | tipos e contagem de não nulos | 4 colunas `float64`, 3 `int64`, 2 `object`; **nenhum valor ausente** |
| `dados.describe()` | estatísticas das colunas numéricas | contagem, média, desvio padrão, mínimo, quartis e máximo |

### 4. Lendo o `describe()` da amostra

| Variável | Média | Mediana | Máximo |
| :--- | ---: | ---: | ---: |
| `Global_active_power` (kW) | 1,098 | 0,613 | 10,290 |
| `Global_reactive_power` (kVAr) | 0,125 | 0,102 | 1,000 |
| `Voltage` (V) | 240,84 | 241,02 | 253,32 |
| `Global_intensity` (A) | 4,65 | 2,60 | 44,60 |

- A potência ativa tem **média bem maior que a mediana** (1,098 × 0,613 kW): a distribuição é assimétrica à direita. Na maior parte do tempo o consumo é baixo, com picos ocasionais de até 10,29 kW.
- A tensão varia pouco (desvio padrão de 3,2 V em torno de 241 V), como se espera de uma rede de distribuição.
- Nas submedições, a mediana de `Sub_metering_1` e `Sub_metering_2` é 0: cozinha e lavanderia ficam desligadas na maior parte dos minutos.

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo básico — os comandos de inspeção em 5 linhas

As 5 linhas abaixo são as primeiras da amostra, as mesmas do `head()` registrado no notebook:

```python
# Inspeção inicial (head, shape, info, describe) com as 5 primeiras linhas de SAMPLE_ENERGY_DATA.csv
import io
import pandas as pd
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

csv = """Date,Time,Global_active_power,Global_reactive_power,Voltage,Global_intensity,Sub_metering_1,Sub_metering_2,Sub_metering_3
2008-12-01 00:00:00,2026-08-03 09:44:00,1.502,0.074,240.17,6.4,0,0,18
2006-12-17 00:00:00,2026-08-03 23:39:00,0.374,0.264,245.5,1.8,0,2,0
2009-06-03 00:00:00,2026-08-03 17:01:00,0.62,0.3,239.85,3,0,1,1
2007-05-09 00:00:00,2026-08-03 05:53:00,0.28,0.2,235.72,1.4,0,0,0
2008-12-14 00:00:00,2026-08-03 02:57:00,1.372,0.054,243.95,5.6,0,0,18
"""
dados = pd.read_csv(io.StringIO(csv))       # no notebook: pd.read_csv('/content/SAMPLE_ENERGY_DATA.csv')
print(dados.shape)
numericas = dados.select_dtypes("number").columns
print("colunas numéricas:", len(numericas), "| de texto (Date e Time):", len(dados.columns) - len(numericas))
print(dados[["Global_active_power", "Voltage", "Global_intensity"]].describe().round(3))
```

Saída esperada:

```text
(5, 9)
colunas numéricas: 7 | de texto (Date e Time): 2
       Global_active_power  Voltage  Global_intensity
count                5.000    5.000             5.000
mean                 0.830  241.038             3.640
std                  0.570    3.835             2.251
min                  0.280  235.720             1.400
25%                  0.374  239.850             1.800
50%                  0.620  240.170             3.000
75%                  1.372  243.950             5.600
max                  1.502  245.500             6.400
```

### Exemplo aplicado — conferências sobre a amostra completa

O código abaixo foi executado na pasta desta aula, onde está o CSV. O fator de potência é estimado em cada registro pelo triângulo das potências da [aula 04](../aula04-19-03-26/README.md):

<!-- norun -->
```python
# Executado na pasta da aula 06, onde está SAMPLE_ENERGY_DATA.csv (40.986 registros)
import pandas as pd

dados = pd.read_csv("SAMPLE_ENERGY_DATA.csv")
print("Datas distintas na coluna Time:", list(dados["Time"].str[:10].unique()))
print("Período em Date:", dados["Date"].min()[:10], "a", dados["Date"].max()[:10])
print("Valores ausentes:", int(dados.isnull().sum().sum()))

PMAX = dados["Global_active_power"].max()
alto = dados[dados["Global_active_power"] > 0.7 * PMAX]
print(f"Acima de 70% de PMAX: {len(alto)} registros = {len(alto) / len(dados):.3%} da amostra")

P, Q = dados["Global_active_power"], dados["Global_reactive_power"]
FP = P / (P ** 2 + Q ** 2) ** 0.5                   # cos φ = P / S, com S = √(P² + Q²)
print(f"Fator de potência estimado: mediana = {FP.median():.3f}, mínimo = {FP.min():.3f}")
```

Saída obtida:

```text
Datas distintas na coluna Time: ['2026-08-03']
Período em Date: 2006-12-16 a 2010-11-26
Valores ausentes: 0
Acima de 70% de PMAX: 23 registros = 0.056% da amostra
Fator de potência estimado: mediana = 0.993, mínimo = 0.655
```

- Todos os registros têm a **mesma data** na coluna `Time`, 2026-08-03, que é a data desta aula. O horário original está correto, mas a data foi acrescentada na preparação dos dados, provavelmente quando o Orange interpretou o horário como data e hora. Para análises por horário, use só a parte da hora.
- A amostra cobre de dezembro de 2006 a novembro de 2010 e não tem valores ausentes, como esperado depois do Preprocess.
- O fator de potência da residência é alto (mediana 0,993): o consumo é predominantemente de cargas resistivas.

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

O material não traz exercícios. **Exercícios propostos para estudo:**

1. Pela saída de `info()`, é preciso tratar valores ausentes no pandas? Por quê?
2. A média de `Global_active_power` é 1,098 kW. Quanto essa residência consumiria, em média, num mês de 30 dias?
3. Por que a amostra deve ser **aleatória**, e não, por exemplo, os primeiros 2% do arquivo?

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

1. Não: as 9 colunas têm 40.986 valores não nulos, porque o Preprocess do Orange já removeu os registros incompletos.
2. $E = P \times \Delta t \approx 1{,}098 \text{ kW} \times 24 \text{ h} \times 30 \approx 790$ kWh, supondo que a média da amostra represente o período todo.
3. Porque o arquivo está em ordem cronológica: os primeiros 2% cobririam só algumas semanas de dezembro de 2006 e não representariam as estações do ano nem os quatro anos de medição.

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Medição inteligente:** concessionárias e empresas de eficiência analisam séries de medidores para entender perfis de consumo.
- **Preparação de dados:** importar, limpar, amostrar e exportar é o início de qualquer projeto de dados; ferramentas visuais como o Orange agilizam protótipos.
- **Gestão de energia residencial:** submedições por circuito (cozinha, lavanderia, climatização) mostram onde está o consumo.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Analisar o arquivo bruto direto, sem inspeção | Começar por `head`, `shape`, `info` e `describe` | Revela tipos, ausentes e escalas antes de qualquer conta |
| Amostrar pegando as primeiras linhas | Amostra aleatória, com semente fixa para reprodutibilidade | Dados em ordem temporal geram amostras enviesadas |
| Confiar na coluna `Time` exportada | Conferir o conteúdo e extrair só a hora | A exportação inseriu a data da aula em todos os registros |
| Olhar só a média de variáveis assimétricas | Comparar média e mediana | Picos raros puxam a média para cima |
| Caminho absoluto no código (`/content/...`) | Caminho relativo ao notebook ou variável de configuração | O mesmo código roda no Colab e no computador |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Orange: CSV File Import → Preprocess (sem ausentes) → Data Sampler (2%) → Save Data.
- Amostra: 40.986 registros × 9 colunas, sem valores ausentes.
- `head()`, `shape`, `info()` e `describe()` são a primeira inspeção de qualquer DataFrame.
- Potência ativa: média 1,098 kW, mediana 0,613 kW, máximo 10,29 kW (assimétrica à direita).
- A coluna `Time` exportada tem a data 2026-08-03 em todos os registros.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Qual *widget* do Orange gerou a amostra de 2%?
2. O que `dados.shape` retorna e o que significa cada número?
3. Por que `Date` e `Time` aparecem como `object` no `info()`?
4. O que a diferença entre média e mediana da potência ativa indica?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. O **Data Sampler**, configurado com 2% e sem reposição.
2. `(40986, 9)`: 40.986 linhas (registros) e 9 colunas (atributos).
3. Porque o pandas as lê como texto; para usá-las como datas seria preciso convertê-las, por exemplo com `pd.to_datetime`.
4. Assimetria à direita: a maior parte dos minutos tem consumo baixo, e alguns picos elevam a média.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [UCI Machine Learning Repository — Individual Household Electric Power Consumption](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption)
- [Orange Data Mining](https://orangedatamining.com/)
- [pandas — `DataFrame.describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
- Materiais da pasta: [notebook](AN%C3%81LISE_DADOS_ENERGIA.ipynb) · [amostra CSV](SAMPLE_ENERGY_DATA.csv) · [workflow do Orange](Workflow_Orange.ows)

<br />

<p align="center"><a href="../aula05-29-03-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula07-10-08-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
