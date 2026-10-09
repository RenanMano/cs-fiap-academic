import os, sys
from urllib.parse import quote
sys.argv = ['x']
from build import DISC, REPO, badge, aulas_of, aula_label, inject_mermaid, MERMAID_INIT

ICONS = {
    'computer-organization-and-architecture': 'Python, C, Assembly, Raspberry Pi',
    'computer-science': 'Arduino (C++), Python',
    'data-structures-and-algorithms': 'Python, JavaScript',
    'modelagem-linear-para-aprendizado-de-maquina': 'Python, pandas, NumPy',
    'modelagem-matematica-e-computacional': 'Python, NumPy',
    'pensamento-computacional-e-automacao-com-python': 'Python, Git',
    'prompt-and-artificial-intelligence': 'Python, OpenAI Agents SDK',
    'solucoes-em-energia-renovaveis-e-sustentaveis': 'Python, scikit-learn',
}
rows, total, svgs = [], 0, 0
for disc, D in DISC.items():
    aulas = aulas_of(disc)
    n = len(aulas); total += n
    s = sum(len([f for f in os.listdir(os.path.join(REPO, disc, a, 'assets'))]) for a in aulas if os.path.isdir(os.path.join(REPO, disc, a, 'assets')))
    svgs += s
    periodo = f'{aula_label(aulas[0])[1]} a {aula_label(aulas[-1])[1]}'
    rows.append(f'      <tr>\n        <td align="center"><strong>{D["curto"]}</strong></td>\n'
                f'        <td align="left"><a href="{disc}/README.md"><strong>{D["nome"]}</strong></a><br /><sub>{D["desc"]}</sub></td>\n'
                f'        <td align="center">{n}</td>\n        <td align="center"><sub>{periodo}</sub></td>\n        <td align="center"><sub>{ICONS[disc]}</sub></td>\n      </tr>\n')

lines = ['Lógica digital, arquitetura e Assembly', 'Estruturas de dados e algoritmos em Python', 'Cálculo, estatística e regressão', 'IA generativa, RAG e agentes']
out = []
out.append('<!-- Índice do repositório. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->\n')
out.append('<p align="center">\n  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=240&amp;section=header'
           f'&amp;text={quote("CS FIAP Academic", safe="")}&amp;fontSize=46&amp;fontColor=F8FAFC&amp;animation=fadeIn&amp;fontAlignY=38'
           f'&amp;desc={quote("CIÊNCIA DA COMPUTAÇÃO — FIAP — MATERIAIS E DOCUMENTAÇÃO DAS AULAS", safe="")}&amp;descSize=13&amp;descAlignY=60" width="100%" alt="CS FIAP Academic" />\n</p>\n')
out.append('<p align="center">\n  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820'
           f'&amp;lines={";".join(quote(l, safe="") for l in lines)}" alt="{". ".join(lines)}." />\n</p>\n')
out.append('<p align="center"><a href="#sobre">Sobre</a> &nbsp;·&nbsp; <a href="#disciplinas">Disciplinas</a> &nbsp;·&nbsp; <a href="#como-usar">Como usar</a> &nbsp;·&nbsp; <a href="#estrutura">Estrutura</a> &nbsp;·&nbsp; <a href="#convencoes">Convenções</a> &nbsp;·&nbsp; <a href="#observacoes">Observações</a></p>\n')
out.append('<p align="center">\n  ' + '\n  '.join([badge('Curso', 'Ciência da Computação', 'FF781F'), badge('Disciplinas', str(len(DISC)), 'FF4500'),
           badge('Aulas documentadas', str(total), 'E60000'), badge('Idioma', 'pt-BR', 'FF781F')]) + '\n</p>\n')
out.append('<p align="center">\n  <img src="https://skillicons.dev/icons?i=py,c,cpp,js,arduino,raspberrypi,sklearn,git,github&amp;theme=dark" alt="Python, C, C++, JavaScript, Arduino, Raspberry Pi, scikit-learn, Git, GitHub" />\n</p>\n')
out.append('<br />\n\n<h2 id="sobre">Sobre o repositório</h2>\n\n')
out.append('Este repositório reúne os **materiais das aulas** do curso de Ciência da Computação da FIAP: slides, apostilas, códigos, *notebooks*, conjuntos de dados e gabaritos. Cada pasta de aula tem um **README** que funciona como material de estudo autônomo:\n\n'
           '- identificação da aula e dos arquivos;\n- objetivos e pré-requisitos;\n- fundamentação teórica;\n- exemplos progressivos com saídas verificadas;\n- exercícios comentados;\n- diagramas;\n- aplicações no mercado de trabalho;\n- resumo e questões de fixação;\n- referências.\n\n')
out.append(f'São **{len(DISC)} disciplinas**, **{total} aulas documentadas** e **{svgs} figuras originais** em SVG, além dos diagramas Mermaid de cada página.\n\n')
out.append('<br />\n\n<h2 id="disciplinas">Disciplinas</h2>\n\n<div align="center">\n  <table>\n    <thead>\n      <tr>\n        <th>Sigla</th>\n        <th align="left">Disciplina</th>\n        <th>Aulas</th>\n        <th>Período</th>\n        <th>Ferramentas</th>\n      </tr>\n    </thead>\n    <tbody>\n'
           + ''.join(rows) + '    </tbody>\n  </table>\n</div>\n\n')
out.append('<br />\n\n<h2 id="como-usar">Como usar esta documentação</h2>\n\n'
           '1. Escolha a disciplina na tabela acima. O índice da disciplina lista as aulas e traz um **mapa de conteúdos**.\n'
           '2. Em cada aula, comece pela **visão geral** e pelos **objetivos**. Depois estude a **teoria** e reproduza os **exemplos**.\n'
           '3. Tente os **exercícios** antes de abrir as soluções, que ficam recolhidas em blocos expansíveis.\n'
           '4. Revise com o **resumo** e as **questões de fixação**.\n'
           '5. Use a navegação no fim de cada página (aula anterior, índice e próxima aula).\n\n')
tree = '''cs-fiap-academic/
├── README.md                          ← este índice
├── <disciplina>/
│   ├── README.md                      ← índice da disciplina
│   └── aulaNN-DD-MM-AA/
│       ├── README.md                  ← documentação da aula
│       ├── assets/                    ← figuras SVG originais (quando houver)
│       └── ...                        ← materiais originais da aula
└── ...'''
out.append('<br />\n\n<h2 id="estrutura">Estrutura de pastas</h2>\n\n'
           'As pastas de aula seguem o padrão `aulaNN-DD-MM-AA`: número sequencial da aula na disciplina, seguido da data. Por exemplo, `aula03-27-03-26` é a terceira aula, de 27/03/2026.\n\n'
           f'```text\n{tree}\n```\n\n')
out.append('<br />\n\n<h2 id="convencoes">Convenções da documentação</h2>\n\n'
           '| Marcação | Significado |\n| :--- | :--- |\n'
           '| **Solução do material original** | Resolução que consta dos slides, gabaritos ou códigos da pasta |\n'
           '| **Solução proposta para estudo** | Resolução elaborada para esta documentação; **não** é gabarito oficial |\n'
           '| **Saída esperada** | Saída obtida executando o código do exemplo (verificada automaticamente) |\n'
           '| **Saída registrada / obtida** | Saída salva num *notebook* ou obtida em execução que depende de arquivos da pasta |\n'
           '| **Limitações da documentação** | O que não pôde ser lido, executado ou verificado em cada aula |\n\n'
           'Os materiais originais **não foram alterados**. Quando um código da pasta tem um erro, ele é descrito na página da aula, com a correção sugerida.\n\n')
out.append('<br />\n\n<h2 id="observacoes">Observações</h2>\n\n'
           '> [!NOTE]\n'
           '> - Vários slides trazem **aviso de direitos autorais** das instituições e dos docentes. As páginas explicam o conteúdo com redação própria e citam a origem.\n'
           '> - *Notebooks* que dependem de serviços pagos (API da OpenAI, Telegram) foram documentados a partir das saídas salvas, **sem execução**. As credenciais são lidas de variáveis de ambiente ou Secrets, e nenhuma está no repositório.\n'
           '> - Arquivos duplicados e pastas `__pycache__` versionadas são apontados nas páginas das aulas e nos índices das disciplinas.\n\n')
out.append('<br />\n\n<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>\n')
open(os.path.join(REPO, 'README.md'), 'w').write(''.join(out))
print(total, svgs)
