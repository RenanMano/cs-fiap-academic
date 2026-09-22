# Checkpoint 2 – Aplicações de Machine Learning para dados de energia

Este repositório será utilizado para o desenvolvimento do **Checkpoint 2**, composto por quatro partes relacionadas à aplicação de técnicas de Machine Learning em dados de estabilidade de redes elétricas.

As atividades utilizarão como referência o conjunto de dados **Electrical Grid Stability Simulated Data**, disponibilizado pela UCI Machine Learning Repository.

Fonte dos dados: [Electrical Grid Stability Simulated Data – UCI](https://archive.ics.uci.edu/dataset/471/electrical+grid+stability+simulated+data)

## Organização do Checkpoint

O Checkpoint será distribuído em quatro partes:

### Parte 1 – Classificação (Aula 06)

Desenvolvimento de um modelo de classificação utilizando **Regressão Logística** para prever a condição da rede elétrica.

- variável target: `stabf`;
- classes previstas: estável ou instável;
- separação dos dados em treino e teste;
- treinamento do modelo;
- geração das previsões;
- avaliação dos resultados por meio de métricas de classificação e matriz de confusão.

O notebook da aula anterior poderá ser utilizado como referência para o desenvolvimento desta parte.

### Parte 2 – Regressão (Aula 07)

Desenvolvimento de modelos de **Regressão Linear** para prever o valor numérico da variável `stab`.

Nesta etapa, deverão ser treinados e comparados dois modelos:

1. modelo utilizando as cinco variáveis com maior correlação absoluta com `stab`;
2. modelo utilizando todas as variáveis cujos nomes começam com `tau` ou `g`.

Os modelos deverão ser avaliados comparativamente por meio das métricas:

- R²;
- MAE;
- MSE.

A análise deverá considerar os resultados dos dois modelos, identificando o efeito da seleção das variáveis sobre o desempenho das previsões.

### Parte 3 – Clustering

Aplicação de uma técnica de **aprendizado não supervisionado** para identificar agrupamentos entre os registros do dataset.

Nesta parte, serão realizadas a preparação das variáveis, a criação dos grupos e a análise das características observadas em cada agrupamento.

As orientações específicas e os critérios para interpretação dos clusters serão apresentados no respectivo roteiro da atividade.

### Parte 4 – Desafio final e apresentação

Desenvolvimento de um desafio final que reunirá os conhecimentos trabalhados nas etapas anteriores.

O grupo deverá analisar os resultados obtidos, justificar as decisões tomadas durante o desenvolvimento e preparar uma apresentação do trabalho.

As orientações do desafio final, os itens obrigatórios e o formato da apresentação serão divulgados na etapa correspondente.

## Orientações gerais

- Desenvolva as atividades em notebooks Python no Google Colab.
- Utilize células Markdown para organizar as etapas, registrar explicações e responder às questões propostas.
- Mantenha os códigos executados e os resultados visíveis.
- Identifique os integrantes do grupo com nome completo e RM.
- Revise os notebooks antes de fazer o upload.
- Mantenha todos os arquivos do Checkpoint organizados neste repositório.
- Não substitua os arquivos das etapas anteriores; cada parte deverá permanecer disponível para consulta e avaliação.

## Organização sugerida do repositório

```text
checkpoint2-ML-SERS-1CCPO/
├── README.md
├── dados/
│   └── Data_for_UCI_named.csv
├── parte_1_classificacao/
│   └── classificacao_estabilidade.ipynb
├── parte_2_regressao/
│   └── regressao_estabilidade.ipynb
├── parte_3_clustering/
│   └── clustering_estabilidade.ipynb
└── parte_4_desafio_final/
    ├── desafio_final.ipynb
    └── apresentacao.pdf
```

Os nomes das pastas e dos arquivos poderão ser ajustados conforme as orientações fornecidas em cada etapa.

## Entrega

Cada parte deverá ser adicionada ao repositório conforme o andamento do Checkpoint. Antes da entrega final, confirme se os notebooks estão organizados, executados e acessíveis.

O repositório deverá reunir as quatro partes do trabalho: **classificação, regressão, clustering e desafio final com apresentação**.
