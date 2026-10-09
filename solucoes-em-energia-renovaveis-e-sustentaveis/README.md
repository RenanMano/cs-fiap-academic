<!-- Índice da disciplina. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=220&amp;section=header&amp;text=Energias%20Renov%C3%A1veis%20e%20Sustent%C3%A1veis&amp;fontSize=30&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=CS%20FIAP%20ACADEMIC%20%E2%80%94%20%C3%8DNDICE%20DA%20DISCIPLINA&amp;descSize=13&amp;descAlignY=60" width="100%" alt="Soluções em Energias Renováveis e Sustentáveis" />
</p>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines=Energia%2C%20pot%C3%AAncia%2C%20consumo%20e%20demanda;Placas%20de%20motores%3A%20P%2C%20S%20e%20Q;Orange%20%2B%20pandas%20com%20dados%20de%20energia;Checkpoint%202%3A%20classifica%C3%A7%C3%A3o%20e%20regress%C3%A3o" alt="Energia, potência, consumo e demanda. Placas de motores: P, S e Q. Orange + pandas com dados de energia. Checkpoint 2: classificação e regressão." />
</p>
<p align="center"><a href="#sobre">Sobre</a> &nbsp;·&nbsp; <a href="#aulas">Aulas</a> &nbsp;·&nbsp; <a href="#mapa">Mapa de conteúdos</a> &nbsp;·&nbsp; <a href="../README.md">Repositório</a></p>
<p align="center">
  <img src="https://img.shields.io/badge/Disciplina-SERS-FF781F?style=for-the-badge&amp;labelColor=0D1117" alt="Disciplina: SERS" />
  <img src="https://img.shields.io/badge/Aulas-10-FF4500?style=for-the-badge&amp;labelColor=0D1117" alt="Aulas: 10" />
  <img src="https://img.shields.io/badge/Docente-Prof.%20Andr%C3%A9%20Tritiack-E60000?style=for-the-badge&amp;labelColor=0D1117" alt="Docente: Prof. André Tritiack" />
  <img src="https://img.shields.io/badge/Pr%C3%A1tica-Python%20e%20ML-FF781F?style=for-the-badge&amp;labelColor=0D1117&amp;logo=python&amp;logoColor=white" alt="Prática: Python e ML" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py,sklearn&amp;theme=dark" alt="Python, scikit-learn" />
</p>
<br />

<h2 id="sobre">Sobre a disciplina</h2>

**Soluções em Energias Renováveis e Sustentáveis** une fundamentos de eletricidade e análise de dados. A aula inaugural organiza a disciplina em sete eixos, da eficiência energética à integração de soluções sustentáveis.

- **1º semestre:** apresentação da disciplina e dos critérios de avaliação; leitura de placas de motores; energia, potência, consumo, demanda, fator de potência e rendimento, com cálculos em Python; Checkpoint 01.
- **2º semestre:** análise de dados de energia com **Orange Data Mining** e **pandas** (inspeção, filtros e limiares de demanda, atividade com seis datasets públicos) e *machine learning* aplicado ao conjunto *Electrical Grid Stability* (UCI) no **Checkpoint 2**, com classificação por regressão logística e regressão linear.

**Avaliação (conforme a aula 01):** Checkpoint (20%, com descarte da menor de três notas), Challenge Sprint (20%) e Global Solution (60%); média final = 0,4 × MS1 + 0,6 × MS2.

**Docente identificado nos materiais:** Prof. André Tritiack, nos slides da aula inaugural.

> [!NOTE]
> - A pasta da aula 09 já tinha um README com o enunciado do Checkpoint 2. O texto foi **preservado integralmente** dentro da nova página.
> - O notebook da aula 10 é um roteiro **em andamento**: algumas saídas não correspondem ao código atual, e a página registra os pontos a concluir. As soluções apresentadas são propostas para estudo, executadas com NumPy, porque o scikit-learn não está instalado no ambiente desta documentação.
> - O enunciado do Checkpoint 01 não está no repositório, apenas o gabarito.
> - O PDF "Energia, Potência, Consumo e Demanda" aparece, idêntico, nas pastas das aulas 03 e 04; ele é documentado na aula 04.
> - Uma pasta enviada para esta disciplina com data de 11/05/2026 continha material de Modelagem Linear para Aprendizado de Máquina (Challenge Sprint 1) e foi movida para aquela disciplina.

<br />

<h2 id="aulas">Aulas</h2>

<div align="center">
  <table>
    <thead>
      <tr>
        <th align="center">Aula</th>
        <th align="center">Data</th>
        <th align="left">Título e tema</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td align="center"><a href="aula01-02-03-26/README.md"><strong>01</strong></a></td>
        <td align="center">02/03/2026</td>
        <td align="left"><a href="aula01-02-03-26/README.md"><strong>Apresentação da Disciplina e Critérios de Avaliação</strong></a><br /><sub>Aula inaugural: os sete eixos da disciplina (eficiência energética, solar e eólica, armazenamento e distribuição, resiliência, gerenciamento inteligente, simulação e integração), o Energy Innovation Lab, os critérios de avaliação (Checkpoint 20%, Challenge Sprint 20% e Global Solution 60%), a média final e a organização do Challenge.</sub></td>
      </tr>
      <tr>
        <td align="center"><a href="aula02-09-03-26/README.md"><strong>02</strong></a></td>
        <td align="center">09/03/2026</td>
        <td align="left"><a href="aula02-09-03-26/README.md"><strong>Placa de Identificação de um Motor de Indução Trifásico</strong></a><br /><sub>Leitura da placa de um motor WEG W22 de 3,0 kW (4 cv): potência, tensões e correntes nominais, rotação, frequência, fator de serviço, relação Ip/In, fator de potência, rendimento, classe de isolamento, grau de proteção, regime, ligações em triângulo e estrela, rolamentos e selos; uso dos dados para calcular as potências ativa, aparente e reativa.</sub></td>
      </tr>
      <tr>
        <td align="center"><a href="aula03-16-03-26/README.md"><strong>03</strong></a></td>
        <td align="center">16/03/2026</td>
        <td align="left"><a href="aula03-16-03-26/README.md"><strong>Atividade: Potências de Motores a partir dos Dados de Placa</strong></a><br /><sub>Notebook que lê potência útil, rendimento e fator de potência de um motor de indução e calcula as potências ativa (P = PU / η), aparente (S = P / FP) e reativa (Q pelo teorema de Pitágoras); exercício com quatro placas reais (WEG W22 Premium, WEG Alto Rendimento Plus, Siemens 1LA9 e WEG W40 Premium) e conferência dos resultados com a corrente de placa.</sub></td>
      </tr>
      <tr>
        <td align="center"><a href="aula04-19-03-26/README.md"><strong>04</strong></a></td>
        <td align="center">19/03/2026</td>
        <td align="left"><a href="aula04-19-03-26/README.md"><strong>Energia, Potência, Consumo e Demanda</strong></a><br /><sub>Conceitos fundamentais e comerciais de energia elétrica: energia e consumo (kWh), potência e demanda (contratada e medida), tensão, corrente e Lei de Joule, potências ativa, reativa e aparente, triângulo das potências, fator de potência, rendimento de motores, carga indutiva, impacto do reativo alto e cálculo em Python.</sub></td>
      </tr>
      <tr>
        <td align="center"><a href="aula05-29-03-26/README.md"><strong>05</strong></a></td>
        <td align="center">29/03/2026</td>
        <td align="left"><a href="aula05-29-03-26/README.md"><strong>Checkpoint 01: Gabarito Detalhado de Consumo e Demanda</strong></a><br /><sub>Gabarito detalhado do Checkpoint 01: cálculo de potências ativa, aparente e reativa em quatro situações industriais (ventilação, bombeamento de água, compressor de ar e comparação de motores), com cenários de troca de equipamento, correção do fator de potência, carga reduzida, degradação, operação em vazio e impacto financeiro da falta de manutenção.</sub></td>
      </tr>
      <tr>
        <td align="center"><a href="aula06-03-08-26/README.md"><strong>06</strong></a></td>
        <td align="center">03/08/2026</td>
        <td align="left"><a href="aula06-03-08-26/README.md"><strong>Dados de Consumo Residencial: Preparação no Orange e Análise Exploratória Preliminar</strong></a><br /><sub>Preparação do conjunto Individual Household Electric Power Consumption (UCI) no Orange Data Mining (importar, eliminar valores ausentes, amostrar 2% e salvar CSV) e primeira inspeção da amostra com pandas: head(), shape, info() e describe(); leitura das variáveis elétricas e problemas de qualidade na coluna Time.</sub></td>
      </tr>
      <tr>
        <td align="center"><a href="aula07-10-08-26/README.md"><strong>07</strong></a></td>
        <td align="center">10/08/2026</td>
        <td align="left"><a href="aula07-10-08-26/README.md"><strong>Manipulação de Dados de Energia com pandas: Renomear, Selecionar e Filtrar</strong></a><br /><sub>Continuação da análise da amostra de consumo residencial: Series × DataFrame, renomear colunas com dicionário, remover colunas com drop, selecionar colunas por nome e por posição (iloc), calcular a demanda máxima (PMAX = 10,29 kW) e o limiar de 70% (7,20 kW) e filtrar os 23 registros acima dele.</sub></td>
      </tr>
      <tr>
        <td align="center"><a href="aula08-17-08-26/README.md"><strong>08</strong></a></td>
        <td align="center">17/08/2026</td>
        <td align="left"><a href="aula08-17-08-26/README.md"><strong>Atividade Prática com Datasets de Energia: Orange e pandas</strong></a><br /><sub>Atividade em grupo com seis datasets públicos do setor de energia (Appliances, Steel Industry, Tetouan City, Solar Power Generation, Wind & Solar e Household Power): preparação no Orange (Select Columns, verificação de ausentes, Data Sampler, exportação) e análise no pandas com limiares relativos ao máximo, filtros com duas condições, contagens e percentuais; notebook-exemplo da turma com o Dataset 1 e guia rápido de pandas.</sub></td>
      </tr>
      <tr>
        <td align="center"><a href="aula09-14-09-26/README.md"><strong>09</strong></a></td>
        <td align="center">14/09/2026</td>
        <td align="left"><a href="aula09-14-09-26/README.md"><strong>Checkpoint 2 (Parte 1): Classificação da Estabilidade da Rede Elétrica</strong></a><br /><sub>Machine learning aplicado a dados de energia: o conjunto Electrical Grid Stability Simulated Data (UCI), separação entre variáveis preditoras e alvo, divisão treino/teste, regressão logística para prever a estabilidade da rede (stable × unstable), probabilidades, previsões e acurácia; enunciado das quatro partes do Checkpoint 2.</sub></td>
      </tr>
      <tr>
        <td align="center"><a href="aula10-21-09-26/README.md"><strong>10</strong></a></td>
        <td align="center">21/09/2026</td>
        <td align="left"><a href="aula10-21-09-26/README.md"><strong>Checkpoint 2 (Parte 2): Regressão Linear com Dados de Energia</strong></a><br /><sub>Roteiro da Parte 2 do Checkpoint 2: prever o valor numérico de stab com regressão linear, análise inicial do dataset, matriz de correlação, seleção das cinco variáveis de maior correlação absoluta (com apoio do Gemini), comparação com o modelo de todas as variáveis tau e g, e avaliação comparativa por R², MAE e MSE.</sub></td>
      </tr>
    </tbody>
  </table>
</div>

<br />

<h2 id="mapa">Mapa de conteúdos</h2>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', 'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', 'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%
flowchart LR
    A["Apresentação<br/>aula 01"] --> B["Placa de motor<br/>aula 02"]
    B --> C["Atividade: potências<br/>de motores<br/>aula 03"]
    C --> D["Energia, potência,<br/>consumo e demanda<br/>aula 04"]
    D --> E["Checkpoint 01:<br/>gabarito<br/>aula 05"]
    D --> F["Orange e inspeção<br/>com pandas<br/>aula 06"]
    F --> G["Filtros e<br/>demanda máxima<br/>aula 07"]
    G --> H["Atividade com<br/>6 datasets<br/>aula 08"]
    H --> I["CP2 Parte 1:<br/>classificação<br/>aula 09"]
    I --> J["CP2 Parte 2:<br/>regressão linear<br/>aula 10"]
```

<br />

<p align="center"><a href="../README.md">← Voltar ao repositório</a></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>
