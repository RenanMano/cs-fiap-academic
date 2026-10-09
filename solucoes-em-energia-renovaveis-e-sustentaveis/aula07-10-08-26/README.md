<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=pandas%3A%20Filtros%20e%20Demanda&amp;fontSize=34&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=SOLU%C3%87%C3%95ES%20EM%20ENERGIAS%20RENOV%C3%81VEIS%20E%20SUSTENT%C3%81VEIS%20%E2%80%94%20AULA%2007%20%E2%80%94%2010%2F08%2F2026&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Manipulação de Dados de Energia com pandas: Renomear, Selecionar e Filtrar" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=dados.rename%28%7B...%7D%2C%20axis%3D1%29;drop%20%C2%B7%20%5B%5B%27col%27%5D%5D%20%C2%B7%20iloc%5B%3A%2C%200%3A4%5D;PMAX%20%3D%2010%2C29%20kW%20%C2%B7%20P70%20%3D%207%2C20%20kW;23%20registros%20acima%20de%2070%25" alt="dados.rename({...}, axis=1). drop · [['col']] · iloc[:, 0:4]. PMAX = 10,29 kW · P70 = 7,20 kW. 23 registros acima de 70%." />
</p>
<p align="center"><a href="#visao-geral">Visão geral</a> &nbsp;·&nbsp; <a href="#fundamentacao-teorica">Teoria</a> &nbsp;·&nbsp; <a href="#exemplos-praticos">Exemplos</a> &nbsp;·&nbsp; <a href="#exercicios-resolvidos">Exercícios</a> &nbsp;·&nbsp; <a href="#aplicacoes">Mercado</a> &nbsp;·&nbsp; <a href="#resumo">Resumo</a> &nbsp;·&nbsp; <a href="#questoes">Questões</a> &nbsp;·&nbsp; <a href="#referencias">Referências</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-SERS-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: SERS" />
  <img src="https://img.shields.io/badge/Aula-07-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aula: 07" />
  <img src="https://img.shields.io/badge/Data-10--08--2026-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Data: 10-08-2026" />
  <img src="https://img.shields.io/badge/Biblioteca-pandas-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=pandas&amp;logoColor=white" alt="Biblioteca: pandas" />
  <img src="https://img.shields.io/badge/Opera%C3%A7%C3%A3o-Filtro%20booleano-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Operação: Filtro booleano" />
  <img src="https://img.shields.io/badge/Indicador-Demanda%20m%C3%A1xima-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Indicador: Demanda máxima" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py&amp;theme=dark" alt="Python" />
</p>
<br />

<h2 id="identificacao">Identificação da aula</h2>

| Item | Descrição |
| :--- | :--- |
| Disciplina | [Soluções em Energias Renováveis e Sustentáveis](../README.md) |
| Aula | 07 — 10/08/2026 |
| Título | Manipulação de Dados de Energia com pandas: Renomear, Selecionar e Filtrar |
| Tema central | Continuação da análise da amostra de consumo residencial: Series × DataFrame, renomear colunas com dicionário, remover colunas com drop, selecionar colunas por nome e por posição (iloc), calcular a demanda máxima (PMAX = 10,29 kW) e o limiar de 70% (7,20 kW) e filtrar os 23 registros acima dele. |
| Tecnologias e ferramentas | Python 3, pandas (Google Colab) |
| Natureza do conteúdo | Aula prática (notebook) |

### Materiais da pasta

| Arquivo | Conteúdo |
| :--- | :--- |
| [`AULA_02_ANÁLISE_DADOS_ENERGIA.ipynb`](AULA_02_AN%C3%81LISE_DADOS_ENERGIA.ipynb) | Notebook com a análise exploratória preliminar da amostra e a continuação da aula: type(), rename() com dicionário, drop(), seleção de uma e de várias colunas, iloc, demanda máxima (10,29 kW), limiar de 70% (7,20 kW) e o filtro que encontra 23 registros acima dele. |

> [!NOTE]
> **Limitações da documentação.** O notebook (30 células) foi lido com as saídas salvas; a célula que exibe a Series tensao não tem saída registrada e uma célula está vazia. O CSV que o notebook lê é o da aula 06 (SAMPLE_ENERGY_DATA.csv), que não está nesta pasta. O exemplo executável desta página usa seis linhas no formato da amostra: as cinco primeiras são reais, e a sexta reúne os valores elétricos do registro 3132 com data, hora e submedições fictícias.

<br />

<h2 id="visao-geral">Visão geral</h2>

O *notebook* desta aula, intitulado "Aula 02", começa repetindo a inspeção da [aula 06](../aula06-03-08-26/README.md) (`head`, `shape`, `info` e `describe`) sobre a mesma amostra de 40.986 registros e avança para a **manipulação** do DataFrame. A pergunta de negócio que fecha a aula é:

> Quantos registros de consumo estão com **demanda acima de 70% da demanda máxima**?

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart LR
    A["dados<br/>(40.986 × 9)"] --> R["rename<br/>nomes em português"]
    R --> D["drop<br/>df1 sem Data e Hora"]
    R --> S["[['Tensao', 'Corrente']]<br/>df2"]
    R --> I["iloc[:, 0:4]<br/>df3"]
    R --> M["PMAX = max()<br/>P70 = 0,7 × PMAX"]
    M --> F["df5 = df4[df4['Potencia_Ativa'] > P70]<br/>23 registros"]
```

*Figura 1 — As operações do notebook, na ordem em que aparecem.*

<br />

<h2 id="objetivos">Objetivos de aprendizagem</h2>

- Diferenciar `Series` (uma coluna) de `DataFrame` (tabela).
- Renomear colunas com um dicionário em `rename()`.
- Criar DataFrames derivados removendo (`drop`) ou selecionando colunas por nome e por posição (`iloc`).
- Calcular a demanda máxima e um limiar relativo a ela.
- Filtrar registros com uma condição booleana e contá-los com `shape[0]`.

<br />

<h2 id="pre-requisitos">Pré-requisitos</h2>

- Inspeção da amostra com pandas, da [aula 06](../aula06-03-08-26/README.md).
- Demanda e potência ativa, da [aula 04](../aula04-19-03-26/README.md).
- Python: dicionários e listas.

<br />

<h2 id="fundamentacao-teorica">Fundamentação teórica</h2>

### 1. Series × DataFrame

`type(dados)` retorna `DataFrame`; `type(dados['Tensao'])` retorna `Series`. Um **DataFrame** é uma tabela com várias colunas; uma **Series** é uma única coluna, com índice. Selecionar com **um** nome (`dados['Tensao']`) dá uma Series; com uma **lista** de nomes (`dados[['Tensao', 'Corrente']]`), dá um DataFrame.

### 2. Renomear colunas

O *notebook* cria um dicionário em que as **chaves** são os nomes atuais e os **valores**, os desejados:

| Original | Novo nome |
| :--- | :--- |
| `Date`, `Time` | `Data`, `Hora` |
| `Global_active_power` | `Potencia_Ativa` |
| `Global_reactive_power` | `Potencia_Reativa` |
| `Voltage` | `Tensao` |
| `Global_intensity` | `Corrente` |
| `Sub_metering_1` a `3` | `Consumo_1` a `Consumo_3` |

A chamada é `dados.rename({...}, axis=1, inplace=True)`: `axis=1` indica que o dicionário se aplica às **colunas**, e `inplace=True` altera o próprio `dados`.

### 3. Criar DataFrames derivados

| DataFrame | Comando | Resultado |
| :--- | :--- | :--- |
| `df1` | `dados.drop(columns=['Data', 'Hora'])` | só as 7 colunas numéricas |
| `df2` | `dados[['Tensao', 'Corrente']]` | tensão e corrente |
| `df3` | `dados.iloc[:, 0:4]` | as colunas de posição 0 a 3 (o fim do intervalo não entra) |
| `df4` | `dados[['Tensao', 'Corrente', 'Potencia_Ativa', 'Potencia_Reativa']]` | grandezas elétricas |

`iloc` seleciona por **posição** (`[linhas, colunas]`); `:` significa "todas as linhas".

### 4. Demanda máxima e limiar de 70%

Como a potência ativa de cada registro é a média de um minuto, o maior valor da coluna é a maior **demanda** observada na amostra:

$$P_{\text{MAX}} = 10{,}29 \text{ kW} \qquad P_{70} = 0{,}7 \times P_{\text{MAX}} = 7{,}20 \text{ kW}$$

O filtro `df4[df4['Potencia_Ativa'] > P70]` cria uma **máscara booleana** (verdadeiro ou falso para cada linha) e mantém só as linhas verdadeiras. O resultado registrado foi `df5.shape[0] = 23`.

> [!NOTE]
> O *notebook* imprime "Foram encontrados 23 **consumidores** com demanda energética acima de 70% de PMAX". O conjunto, porém, é de **uma única residência**: cada linha é **uma medição de um minuto**, e não um consumidor. A leitura correta é "23 minutos (registros) com demanda acima de 70% do máximo", o equivalente a 0,056% da amostra.

<br />

<h2 id="exemplos-praticos">Exemplos práticos</h2>

### Exemplo aplicado — todas as operações do notebook, em pequena escala

Seis linhas no formato da amostra, as cinco primeiras iguais às do `head()` registrado:

```python
# Mesmas operações dos notebooks de 03/08 e 10/08, com 6 linhas no formato de SAMPLE_ENERGY_DATA.csv
import pandas as pd
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

dados = pd.DataFrame({
    "Date": ["2008-12-01", "2006-12-17", "2009-06-03", "2007-05-09", "2008-12-14", "2009-02-02"],
    "Time": ["09:44:00", "23:39:00", "17:01:00", "05:53:00", "02:57:00", "19:30:00"],
    "Global_active_power": [1.502, 0.374, 0.620, 0.280, 1.372, 8.540],
    "Global_reactive_power": [0.074, 0.264, 0.300, 0.200, 0.054, 0.238],
    "Voltage": [240.17, 245.50, 239.85, 235.72, 243.95, 236.23],
    "Global_intensity": [6.4, 1.8, 3.0, 1.4, 5.6, 36.0],
    "Sub_metering_1": [0, 0, 0, 0, 0, 38],
    "Sub_metering_2": [0, 2, 1, 0, 0, 1],
    "Sub_metering_3": [18, 0, 1, 0, 18, 17],
})
print(dados.shape, "| linhas:", dados.shape[0])

dados = dados.rename(columns={"Date": "Data", "Time": "Hora", "Global_active_power": "Potencia_Ativa",
                              "Global_reactive_power": "Potencia_Reativa", "Voltage": "Tensao",
                              "Global_intensity": "Corrente", "Sub_metering_1": "Consumo_1",
                              "Sub_metering_2": "Consumo_2", "Sub_metering_3": "Consumo_3"})
df1 = dados.drop(columns=["Data", "Hora"])          # remove colunas
df2 = dados[["Tensao", "Corrente"]]                 # seleciona colunas (DataFrame)
tensao = dados["Tensao"]                            # uma coluna (Series)
df3 = dados.iloc[:, 0:4]                            # 4 primeiras colunas por posição
print(type(df2).__name__, type(tensao).__name__, list(df1.columns)[:3], list(df3.columns))

PMAX = dados["Potencia_Ativa"].max()
P70 = 0.7 * PMAX
df4 = dados[["Tensao", "Corrente", "Potencia_Ativa", "Potencia_Reativa"]]
df5 = df4[df4["Potencia_Ativa"] > P70]
print(f"PMAX = {PMAX:.2f} kW | P70 = {P70:.2f} kW | registros acima: {df5.shape[0]}")
print(df5)
```

Saída esperada:

```text
(6, 9) | linhas: 6
DataFrame Series ['Potencia_Ativa', 'Potencia_Reativa', 'Tensao'] ['Data', 'Hora', 'Potencia_Ativa', 'Potencia_Reativa']
PMAX = 8.54 kW | P70 = 5.98 kW | registros acima: 1
   Tensao  Corrente  Potencia_Ativa  Potencia_Reativa
5  236.23      36.0            8.54             0.238
```

Com só seis linhas, o máximo e o limiar são outros (8,54 kW e 5,98 kW), mas a sequência é a mesma do *notebook*. Na amostra completa, o primeiro dos 23 registros acima do limiar (índice 3132) tem exatamente os valores da sexta linha: 236,23 V, 36,0 A, 8,540 kW e 0,238 kVAr.

### Saída registrada no notebook

<!-- norun -->
```text
A demanda máxima de potência é 10.29 kW
O limiar de 70% da demanda máxima é 7.20 kW
Foram encontrados 23 consumidores com demanda energética acima de 70% de PMAX
```

<br />

<h2 id="exercicios-resolvidos">Exercícios e resoluções comentadas</h2>

O *notebook* propõe a pergunta "quantos consumidores estão com demanda acima de 70%?" e a responde nas células finais; essa resposta é a **solução do material original** (23 registros), com a ressalva de interpretação da teoria. **Exercícios propostos para estudo:**

1. Calcule o percentual que os 23 registros representam na amostra.
2. Escreva o filtro para registros com potência acima de 70% do máximo **e** tensão abaixo de 235 V.
3. Por que `df4 = dados[[...]]` seguido de alterações em `df4` pode gerar um aviso do pandas? Como evitá-lo?

<details>
<summary><strong>Solução proposta para estudo</strong></summary>

1. $23 / 40\,986 \times 100 \approx 0{,}056\%$.
2. `dados[(dados['Potencia_Ativa'] > P70) & (dados['Tensao'] < 235)]`. Cada condição fica entre parênteses e o "e" é `&`, e não `and`.
3. Porque `df4` pode ser uma "visão" de `dados`, e o pandas avisa que a alteração talvez não se propague como esperado. Usar `df4 = dados[[...]].copy()` deixa claro que se trata de uma cópia independente.

</details>

<br />

<h2 id="aplicacoes">Aplicações no mercado de trabalho</h2>

- **Gestão de demanda:** identificar os períodos em que o consumo se aproxima do pico orienta o deslocamento de cargas e a escolha da demanda contratada.
- **Alertas automáticos:** filtros como `Potencia_Ativa > P70` são a base de alarmes em sistemas de monitoramento de energia.
- **Padronização de dados:** renomear colunas para nomes claros e consistentes facilita o trabalho em equipe e a integração com outras bases.

<br />

<h2 id="boas-praticas">Boas práticas e erros comuns</h2>

| Problemático | Recomendado | Motivo |
| :--- | :--- | :--- |
| Chamar cada linha de "consumidor" | Descrever o que a linha representa (uma medição de 1 minuto) | Evita conclusões erradas sobre o conjunto |
| `rename({...})` sem `axis=1` ou `columns=` | `rename(columns={...})` | Sem isso, o dicionário é aplicado ao índice das linhas |
| `and`/`or` em filtros do pandas | `&`/`\|` com parênteses em cada condição | `and` não funciona elemento a elemento |
| Esquecer que o fim do intervalo do `iloc` não entra | Lembrar que `0:4` pega as posições 0, 1, 2 e 3 | Evita pegar uma coluna a menos |
| Modificar um recorte sem `.copy()` | Usar `.copy()` ao criar DataFrames derivados | Evita avisos e efeitos colaterais |

<br />

<h2 id="resumo">Resumo para revisão</h2>

- Uma coluna é `Series`; várias colunas são `DataFrame`.
- `rename(dicionário, axis=1)` renomeia colunas; `drop(columns=[...])` remove; `iloc[:, 0:4]` seleciona por posição.
- Demanda máxima da amostra: 10,29 kW; limiar de 70%: 7,20 kW.
- Filtro booleano: `df[df['col'] > valor]`; `shape[0]` conta as linhas.
- Os 23 registros acima do limiar são minutos de uma mesma residência, não consumidores.

<br />

<h2 id="questoes">Questões de fixação</h2>

1. Qual é o tipo de `dados['Tensao']`? E de `dados[['Tensao']]`?
2. Quais colunas `dados.iloc[:, 0:4]` seleciona depois da renomeação?
3. Qual é o limiar de 75% da demanda máxima da amostra?
4. Por que a frase "23 consumidores" não descreve corretamente o resultado?

<details>
<summary><strong>Respostas comentadas</strong></summary>

1. `Series` e `DataFrame` (com uma coluna), respectivamente.
2. `Data`, `Hora`, `Potencia_Ativa` e `Potencia_Reativa`.
3. $0{,}75 \times 10{,}29 \approx 7{,}72$ kW.
4. Porque o conjunto mede uma única residência; cada linha é um minuto de medição.

</details>

<br />

<h2 id="referencias">Referências e materiais complementares</h2>

- [pandas — `DataFrame.rename`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)
- [pandas — indexação e seleção (`loc`, `iloc`, máscaras booleanas)](https://pandas.pydata.org/docs/user_guide/indexing.html)
- Dataset e inspeção inicial: [aula 06](../aula06-03-08-26/README.md)
- Material da pasta: [notebook](AULA_02_AN%C3%81LISE_DADOS_ENERGIA.ipynb)

<br />

<p align="center"><a href="../aula06-03-08-26/README.md">← Aula anterior</a> &nbsp;·&nbsp; <a href="../README.md">Índice da disciplina</a> &nbsp;·&nbsp; <a href="../aula08-17-08-26/README.md">Próxima aula →</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
