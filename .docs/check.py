#!/usr/bin/env python3
"""Valida os README.md gerados: links relativos, âncoras, exemplos Python com saída esperada e diagramas Mermaid."""
import os, re, subprocess, sys, tempfile
from urllib.parse import unquote

import json, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
# mermaid-cli: instale com `npm install` dentro de .docs/ (ver package.json) ou tenha `mmdc` no PATH.
MMDC = os.path.join(HERE, 'node_modules/.bin/mmdc')
if not os.path.exists(MMDC):
    MMDC = shutil.which('mmdc')
# Chromium já instalado (ambiente de nuvem do Claude Code); sem ele, o puppeteer usa o próprio navegador.
CHROMIUM = '/opt/pw-browsers/chromium'

PY_RE = re.compile(r'(<!-- norun -->\s*)?```python\n((?:(?!```).)*?)```\s*\n+\*{0,2}Saída esperada:?\*{0,2}:?\s*\n+```text\n(.*?)```', re.S)


def anchors(text):
    ids = set(re.findall(r'id="([^"]+)"', text))
    for h in re.findall(r'^#{1,6} (.+)$', text, re.M):
        ids.add(re.sub(r'[^\w\- ]', '', h.strip().lower()).replace(' ', '-'))
    return ids


def check_links(path, text):
    errs = []
    base = os.path.dirname(path)
    ids = anchors(text)
    targets = re.findall(r'\]\(([^)\s]+)\)', text) + re.findall(r'(?:href|src)="([^"]+)"', text)
    for t in targets:
        if t.startswith(('http://', 'https://', 'mailto:')):
            continue
        if t.startswith('#'):
            if t[1:] not in ids:
                errs.append(f'âncora inexistente {t}')
            continue
        p = unquote(t.split('#')[0])
        full = os.path.join(base, p)
        if not os.path.exists(full):
            errs.append(f'link quebrado {t}')
        elif '#' in t and full.endswith('.md'):
            if unquote(t.split('#')[1]) not in anchors(open(full, encoding='utf-8').read()):
                errs.append(f'âncora externa inexistente {t}')
    return errs


def check_python(text):
    errs, n = [], 0
    for m in PY_RE.finditer(text):
        if m.group(1):
            continue
        n += 1
        code, expected = m.group(2), m.group(3)
        with tempfile.TemporaryDirectory() as d:
            r = subprocess.run([sys.executable, '-I', '-c', code], capture_output=True, text=True, cwd=d, timeout=60)
        got = r.stdout
        if r.returncode != 0 or got.rstrip() != expected.rstrip():
            errs.append(f'exemplo python divergente:\n--- código\n{code}\n--- esperado\n{expected}\n--- obtido\n{got}{r.stderr}')
    return errs, n


ASM_RE = re.compile(r'(<!-- norun -->\s*)?```nasm\n((?:(?!```).)*?)```\s*\n+\*{0,2}Saída esperada:?\*{0,2}:?\s*\n+```text\n(.*?)```', re.S)


def check_asm(text):
    errs, n = [], 0
    for m in ASM_RE.finditer(text):
        if m.group(1):
            continue
        n += 1
        code, expected = m.group(2), m.group(3)
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, 'p.asm'), 'w').write(code)
            r = subprocess.run('nasm -f elf32 p.asm -o p.o && ld -m elf_i386 p.o -o p && ./p', shell=True,
                               capture_output=True, text=True, cwd=d, timeout=60)
        if r.stdout.rstrip() != expected.rstrip():
            errs.append(f'exemplo nasm divergente: esperado {expected!r}, obtido {r.stdout!r} {r.stderr}')
    return errs, n


JS_RE = re.compile(r'(<!-- norun -->\s*)?```javascript\n((?:(?!```).)*?)```\s*\n+\*{0,2}Saída esperada:?\*{0,2}:?\s*\n+```text\n(.*?)```', re.S)


def check_js(text):
    errs, n = [], 0
    for m in JS_RE.finditer(text):
        if m.group(1):
            continue
        n += 1
        code, expected = m.group(2), m.group(3)
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, 'p.js'), 'w').write(code)
            r = subprocess.run(['node', 'p.js'], capture_output=True, text=True, cwd=d, timeout=60)
        if r.returncode != 0 or r.stdout.rstrip() != expected.rstrip():
            errs.append(f'exemplo js divergente:\n--- código\n{code}\n--- esperado\n{expected}\n--- obtido\n{r.stdout}{r.stderr}')
    return errs, n


def check_mermaid(path, text):
    n = text.count('```mermaid')
    if not n:
        return [], 0
    if not MMDC:
        return [f'mermaid não verificado: mmdc não encontrado (rode `npm install` em .docs/ ou use --no-mermaid)'], n
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, 'o.md')
        cmd = [MMDC, '-i', path, '-o', out, '-q']
        if os.path.exists(CHROMIUM):
            pp = os.path.join(d, 'pp.json')
            json.dump({'executablePath': CHROMIUM, 'args': ['--no-sandbox']}, open(pp, 'w'))
            cmd[1:1] = ['-p', pp]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            return [f'mermaid: {r.stderr[-1500:]}'], n
    return [], n


def main(paths):
    total_err = 0
    for p in paths:
        text = open(p, encoding='utf-8').read()
        errs = check_links(p, text)
        e2, npy = check_python(text)
        e4, nasm = check_asm(text)
        errs += e4
        e5, njs = check_js(text)
        errs += e5
        e3, nm = check_mermaid(p, text) if '--no-mermaid' not in sys.argv else ([], 0)
        errs += e2 + e3
        ls = text.split('\n')
        for i in range(len(ls) - 1):
            if ls[i].startswith('<') and not ls[i].startswith('<!--') and ls[i + 1][:1] in ('|', '#', '-', '>', '*') and not ls[i+1].startswith('<'):
                errs.append(f'bloco HTML sem linha em branco antes de markdown (linha {i + 1})')
        if text.count('```') % 2:
            errs.append('número ímpar de cercas de código')
        if text.count('<details>') != text.count('</details>'):
            errs.append('<details> desbalanceado')
        status = 'OK ' if not errs else 'ERR'
        print(f'{status} {p}  (python={npy}, js={njs}, nasm={nasm}, mermaid={nm})')
        for e in errs:
            print('    ' + e.replace('\n', '\n    '))
        total_err += len(errs)
    sys.exit(1 if total_err else 0)


if __name__ == '__main__':
    main([a for a in sys.argv[1:] if not a.startswith('--')])
