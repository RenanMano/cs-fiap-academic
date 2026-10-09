#!/usr/bin/env python3
"""Gera os README.md das aulas a partir das especificações em specs/<disciplina>/<aula>.md.

Cada especificação começa com um bloco <!--META {json} META--> seguido do corpo em Markdown.
O builder acrescenta cabeçalho, animação, menu, badges, identificação, materiais,
navegação entre aulas e rodapé no padrão visual Knowledge Atelier.
"""
import json, os, re, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)  # .docs/ fica na raiz do repositório
SPECS = os.path.join(HERE, 'specs')
EXEMPLOS = os.path.join(HERE, 'exemplos')  # arquivos usados por {{include:...}}

DISC = {
    'computer-organization-and-architecture': dict(nome='Computer Organization and Architecture', curto='COA',
        desc='Organização e arquitetura de computadores: sistemas numéricos, representação de dados, processadores, memória, Assembly e hardware embarcado.'),
    'computer-science': dict(nome='Computer Science', curto='CS',
        desc='Fundamentos de lógica digital: sistemas numéricos, portas lógicas, álgebra booleana, De Morgan, mapas de Karnaugh e microcontroladores.'),
    'data-structures-and-algorithms': dict(nome='Data Structures and Algorithms', curto='DSA',
        desc='Tipos abstratos de dados, análise assintótica, estruturas lineares, ordenação, recursividade e árvores binárias.'),
    'modelagem-linear-para-aprendizado-de-maquina': dict(nome='Modelagem Linear para Aprendizado de Máquina', curto='MLAM',
        desc='Estatística aplicada com Python: pesquisa e coleta de dados, estatística descritiva, probabilidade, inferência e regressão linear.'),
    'modelagem-matematica-e-computacional': dict(nome='Modelagem Matemática e Computacional', curto='MMC',
        desc='Cálculo diferencial e integral com apoio computacional: limites, derivadas, integrais e álgebra linear computacional.'),
    'pensamento-computacional-e-automacao-com-python': dict(nome='Pensamento Computacional e Automação com Python', curto='PCP',
        desc='Lógica de programação com Python: variáveis, condicionais, repetição, coleções, modularização, arquivos e orientação a objetos.'),
    'prompt-and-artificial-intelligence': dict(nome='Prompt and Artificial Intelligence', curto='PAI',
        desc='Inteligência artificial generativa, engenharia de prompt, agentes conversacionais e guardrails.'),
    'solucoes-em-energia-renovaveis-e-sustentaveis': dict(nome='Soluções em Energias Renováveis e Sustentáveis', curto='SERS',
        desc='Conceitos de energia, potência, consumo e demanda e análise de dados energéticos com Python.'),
}

MENU = [
    ('visao-geral', 'Visão geral'), ('fundamentacao-teorica', 'Teoria'), ('exemplos-praticos', 'Exemplos'),
    ('exercicios-resolvidos', 'Exercícios'), ('aplicacoes', 'Mercado'), ('resumo', 'Resumo'),
    ('questoes', 'Questões'), ('referencias', 'Referências'),
]

MERMAID_INIT = ("%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FF781F', 'primaryTextColor': '#0D1117', "
                "'primaryBorderColor': '#E60000', 'lineColor': '#FF4500', 'secondaryColor': '#FFD8B8', 'tertiaryColor': '#FFF1E6', "
                "'edgeLabelBackground': '#FFF1E6', 'fontFamily': 'Fira Code, monospace'}}}%%")

COLORS = ['FF781F', 'FF4500', 'E60000']


def badge(label, msg, color='FF781F', logo=None):
    esc = lambda s: quote(s.replace('-', '--').replace('_', '__'), safe='')
    url = f'https://img.shields.io/badge/{esc(label)}-{esc(msg)}-{color}?style=for-the-badge&amp;labelColor=0D1117'
    if logo:
        url += f'&amp;logo={logo}&amp;logoColor=white'
    return f'<img src="{url}" alt="{label}: {msg}" />'


def font_size(text):
    n = len(text)
    return 40 if n <= 18 else 34 if n <= 26 else 30 if n <= 34 else 26 if n <= 42 else 22


def link_path(name):
    return '/'.join(quote(p) for p in name.split('/'))


def parse_spec(path):
    raw = open(path, encoding='utf-8').read()
    m = re.match(r'\s*<!--META\s*(\{.*?\})\s*META-->\s*\n(.*)', raw, re.S)
    if not m:
        sys.exit(f'META ausente em {path}')
    return json.loads(m.group(1)), m.group(2).strip('\n')


def aulas_of(disc):
    return sorted(d for d in os.listdir(os.path.join(REPO, disc)) if d.startswith('aula') and os.path.isdir(os.path.join(REPO, disc, d)))


def aula_label(folder):
    m = re.match(r'aula(\d+)-(\d\d)-(\d\d)-(\d\d)', folder)
    return int(m.group(1)), f'{m.group(2)}/{m.group(3)}/20{m.group(4)}'


def list_files(disc, aula):
    base = os.path.join(REPO, disc, aula)
    out = []
    for root, dirs, files in os.walk(base):
        dirs[:] = sorted(d for d in dirs if d not in ('__pycache__', '.ipynb_checkpoints'))
        for f in sorted(files):
            rel = os.path.relpath(os.path.join(root, f), base)
            if rel == 'README.md':
                continue
            out.append(rel)
    return out


def inject_mermaid(body):
    def rep(m):
        block = m.group(1)
        if '%%{init' in block:
            return m.group(0)
        return '```mermaid\n' + MERMAID_INIT + '\n' + block + '```'
    return re.sub(r'```mermaid\n(.*?)```', rep, body, flags=re.S)


def build(disc, aula):
    spec = os.path.join(SPECS, disc, aula + '.md')
    meta, body = parse_spec(spec)
    D = DISC[disc]
    num, data = aula_label(aula)
    title = meta['title']
    header = meta.get('header', title)
    fs = meta.get('font_size', font_size(header))
    desc = f'{D["nome"].upper()} — AULA {num:02d} — {data}'
    lines = ';'.join(quote(l.replace(';', ','), safe='') for l in meta['typing'])
    alt_typing = '. '.join(meta['typing']) + '.'

    ids = re.findall(r'<h2 id="([^"]+)"', body)
    menu = ' &nbsp;·&nbsp; '.join(f'<a href="#{i}">{lbl}</a>' for i, lbl in MENU if i in ids)

    badges = [badge('Disciplina', D['curto'], 'FF781F'), badge('Aula', f'{num:02d}', 'FF4500'), badge('Data', data.replace('/', '-'), 'E60000')]
    for b in meta.get('badges', []):
        badges.append(badge(b[0], b[1], b[2] if len(b) > 2 else 'FF781F', b[3] if len(b) > 3 else None))

    out = []
    out.append('<!-- Documentação acadêmica da aula. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->\n')
    out.append('<p align="center">\n  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000'
               f'&amp;height=220&amp;section=header&amp;text={quote(header, safe="")}&amp;fontSize={fs}&amp;fontColor=F8FAFC'
               f'&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc={quote(desc, safe="")}&amp;descSize=13&amp;descAlignY=60" '
               f'width="100%" alt="{title}" />\n</p>\n')
    out.append('<p align="center">\n  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18'
               f'&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines={lines}" '
               f'alt="{alt_typing}" />\n</p>\n')
    out.append(f'<p align="center">{menu}</p>\n')
    out.append('<p align="center">\n  ' + '\n  '.join(badges) + '\n</p>\n')
    if meta.get('icons'):
        out.append(f'<p align="center">\n  <img src="https://skillicons.dev/icons?i={meta["icons"]}&amp;theme=dark" alt="{meta.get("icons_alt", meta["icons"])}" />\n</p>\n')

    # Identificação
    out.append('<br />\n\n<h2 id="identificacao">Identificação da aula</h2>\n\n')
    rows = [('Disciplina', f'[{D["nome"]}](../README.md)'), ('Aula', f'{num:02d} — {data}'), ('Título', title),
            ('Tema central', meta['tema'])]
    if meta.get('tecnologias'):
        rows.append(('Tecnologias e ferramentas', meta['tecnologias']))
    if meta.get('professor'):
        rows.append(('Docente (conforme material)', meta['professor']))
    if meta.get('tipo'):
        rows.append(('Natureza do conteúdo', meta['tipo']))
    out.append('| Item | Descrição |\n| :--- | :--- |\n' + '\n'.join(f'| {a} | {b} |' for a, b in rows) + '\n')

    # Materiais
    files = list_files(disc, aula)
    fdesc = meta.get('files', {})
    missing = [f for f in files if f not in fdesc]
    if missing:
        sys.exit(f'{disc}/{aula}: arquivos sem descrição: {missing}')
    extra = [f for f in fdesc if f not in files]
    if extra:
        sys.exit(f'{disc}/{aula}: descrição para arquivos inexistentes: {extra}')
    out.append('\n### Materiais da pasta\n\n')
    out.append('| Arquivo | Conteúdo |\n| :--- | :--- |\n' + '\n'.join(f'| [`{f}`]({link_path(f)}) | {fdesc[f]} |' for f in files) + '\n')
    if meta.get('limitacoes'):
        out.append('\n> [!NOTE]\n> **Limitações da documentação.** ' + meta['limitacoes'] + '\n')

    while '{{include:' in body:
        body = re.sub(r'\{\{include:([^}]+)\}\}', lambda m: open(os.path.join(EXEMPLOS, m.group(1)), encoding='utf-8').read().rstrip('\n'), body)
    body = inject_mermaid(body)
    out.append('\n' + body + '\n')

    # Navegação
    seq = aulas_of(disc)
    i = seq.index(aula)
    nav = []
    if i > 0:
        nav.append(f'<a href="../{seq[i-1]}/README.md">← Aula anterior</a>')
    nav.append('<a href="../README.md">Índice da disciplina</a>')
    if i < len(seq) - 1:
        nav.append(f'<a href="../{seq[i+1]}/README.md">Próxima aula →</a>')
    out.append('\n<br />\n\n<p align="center">' + ' &nbsp;·&nbsp; '.join(nav) + '</p>\n')
    out.append('\n<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>\n')

    dest = os.path.join(REPO, disc, aula, 'README.md')
    open(dest, 'w', encoding='utf-8').write(''.join(out))
    return meta


def build_disc(disc):
    D = DISC[disc]
    rows = []
    for aula in aulas_of(disc):
        spec = os.path.join(SPECS, disc, aula + '.md')
        if not os.path.exists(spec):
            rows.append((aula, None))
            continue
        meta = build(disc, aula)
        rows.append((aula, meta))
    return rows




def build_index(disc):
    """Gera o README.md da disciplina a partir de specs/<disc>/_index.md e dos METAs das aulas."""
    D = DISC[disc]
    spec = os.path.join(SPECS, disc, '_index.md')
    meta, body = parse_spec(spec)
    lines = ';'.join(quote(l.replace(';', ','), safe='') for l in meta['typing'])
    header = D['nome']
    out = ['<!-- Índice da disciplina. Padrão visual: Knowledge Atelier (github.com/RenanMano). -->\n']
    out.append('<p align="center">\n  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000'
               f'&amp;height=220&amp;section=header&amp;text={quote(meta.get("header", header), safe="")}&amp;fontSize={meta.get("font_size", font_size(meta.get("header", header)))}&amp;fontColor=F8FAFC'
               f'&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc={quote("CS FIAP ACADEMIC — ÍNDICE DA DISCIPLINA", safe="")}&amp;descSize=13&amp;descAlignY=60" '
               f'width="100%" alt="{D["nome"]}" />\n</p>\n')
    out.append('<p align="center">\n  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=18'
               f'&amp;duration=3200&amp;pause=1100&amp;color=FF781F&amp;center=true&amp;vCenter=true&amp;width=820&amp;lines={lines}" '
               f'alt="{". ".join(meta["typing"])}." />\n</p>\n')
    out.append('<p align="center"><a href="#sobre">Sobre</a> &nbsp;·&nbsp; <a href="#aulas">Aulas</a> &nbsp;·&nbsp; <a href="#mapa">Mapa de conteúdos</a> &nbsp;·&nbsp; <a href="../README.md">Repositório</a></p>\n')
    aulas = aulas_of(disc)
    badges = [badge('Disciplina', D['curto'], 'FF781F'), badge('Aulas', str(len(aulas)), 'FF4500')]
    for b in meta.get('badges', []):
        badges.append(badge(b[0], b[1], b[2] if len(b) > 2 else 'FF781F', b[3] if len(b) > 3 else None))
    out.append('<p align="center">\n  ' + '\n  '.join(badges) + '\n</p>\n')
    if meta.get('icons'):
        out.append(f'<p align="center">\n  <img src="https://skillicons.dev/icons?i={meta["icons"]}&amp;theme=dark" alt="{meta.get("icons_alt", meta["icons"])}" />\n</p>\n')
    out.append('<br />\n\n<h2 id="sobre">Sobre a disciplina</h2>\n\n' + body.strip() + '\n')
    out.append('\n<br />\n\n<h2 id="aulas">Aulas</h2>\n\n<div align="center">\n  <table>\n    <thead>\n      <tr>\n'
               '        <th align="center">Aula</th>\n        <th align="center">Data</th>\n        <th align="left">Título e tema</th>\n      </tr>\n    </thead>\n    <tbody>\n')
    for a in aulas:
        num, data = aula_label(a)
        am, _ = parse_spec(os.path.join(SPECS, disc, a + '.md'))
        out.append(f'      <tr>\n        <td align="center"><a href="{a}/README.md"><strong>{num:02d}</strong></a></td>\n'
                   f'        <td align="center">{data}</td>\n'
                   f'        <td align="left"><a href="{a}/README.md"><strong>{am["title"]}</strong></a><br /><sub>{am["tema"]}</sub></td>\n      </tr>\n')
    out.append('    </tbody>\n  </table>\n</div>\n')
    if meta.get('mapa'):
        out.append('\n<br />\n\n<h2 id="mapa">Mapa de conteúdos</h2>\n\n```mermaid\n' + MERMAID_INIT + '\n' + meta['mapa'].strip() + '\n```\n')
    out.append('\n<br />\n\n<p align="center"><a href="../README.md">← Voltar ao repositório</a></p>\n')
    out.append('\n<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:FF781F,50:FF4500,100:E60000&amp;height=110&amp;section=footer" width="100%" alt="" /></p>\n')
    open(os.path.join(REPO, disc, 'README.md'), 'w', encoding='utf-8').write(''.join(out))


if __name__ == '__main__':
    targets = sys.argv[1:] or list(DISC)
    for t in targets:
        if '/' in t:
            d, a = t.split('/')
            build(d, a)
            print('ok', t)
        else:
            for aula, meta in build_disc(t):
                print('ok' if meta else '--', t, aula)
            if os.path.exists(os.path.join(SPECS, t, '_index.md')):
                build_index(t)
                print('ok', t, 'índice')

