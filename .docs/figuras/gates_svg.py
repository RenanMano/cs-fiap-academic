"""Gera um SVG com os símbolos ANSI das portas lógicas e suas tabelas-verdade (paleta Knowledge Atelier)."""
import sys

GATES = {
    'AND': dict(expr='Y = A · B', f=lambda a, b: a & b, n=2),
    'OR': dict(expr='Y = A + B', f=lambda a, b: a | b, n=2),
    'NOT': dict(expr="Y = A'", f=lambda a: 1 - a, n=1),
    'NAND': dict(expr="Y = (A · B)'", f=lambda a, b: 1 - (a & b), n=2),
    'NOR': dict(expr="Y = (A + B)'", f=lambda a, b: 1 - (a | b), n=2),
    'XOR': dict(expr='Y = A ⊕ B', f=lambda a, b: a ^ b, n=2),
    'XNOR': dict(expr="Y = (A ⊕ B)'", f=lambda a, b: 1 - (a ^ b), n=2),
}


def shape(kind, x, y):
    """Desenha o corpo da porta com canto superior esquerdo em (x, y); corpo 70x50."""
    s = 'fill="#161B22" stroke="url(#g)" stroke-width="3"'
    out = []
    base = kind.replace('N', '', 1) if kind in ('NAND', 'NOR') else ('XOR' if kind == 'XNOR' else kind)
    if base == 'AND':
        out.append(f'<path d="M{x} {y} H{x+35} A25 25 0 0 1 {x+35} {y+50} H{x} Z" {s}/>')
        tip = x + 60
    elif base in ('OR', 'XOR'):
        out.append(f'<path d="M{x} {y} Q{x+45} {y} {x+65} {y+25} Q{x+45} {y+50} {x} {y+50} Q{x+15} {y+25} {x} {y} Z" {s}/>')
        if base == 'XOR':
            out.append(f'<path d="M{x-9} {y} Q{x+6} {y+25} {x-9} {y+50}" fill="none" stroke="url(#g)" stroke-width="3"/>')
        tip = x + 65
    else:  # NOT
        out.append(f'<path d="M{x} {y} L{x+50} {y+25} L{x} {y+50} Z" {s}/>')
        tip = x + 50
    if kind in ('NAND', 'NOR', 'NOT', 'XNOR'):
        out.append(f'<circle cx="{tip+6}" cy="{y+25}" r="6" fill="#0D1117" stroke="#FF781F" stroke-width="3"/>')
        tip += 12
    return out, tip


def build(kinds, path):
    cw, ch = 250, 250
    cols = len(kinds)
    W, H = cw * cols + 20, ch + 20
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">',
         f'<title id="t">Portas lógicas {", ".join(kinds)}</title>',
         '<desc id="d">Símbolos ANSI das portas lógicas com a expressão booleana e a tabela-verdade de cada uma.</desc>',
         '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF781F"/><stop offset=".5" stop-color="#FF4500"/><stop offset="1" stop-color="#E60000"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="18" fill="#0D1117"/>', f'<rect width="{W}" height="6" rx="3" fill="url(#g)"/>',
         '<g font-family="Fira Code, Consolas, monospace">']
    for i, k in enumerate(kinds):
        g = GATES[k]
        ox = 10 + i * cw
        o.append(f'<text x="{ox + cw/2}" y="36" font-size="18" font-weight="700" fill="#F8FAFC" text-anchor="middle">{k}</text>')
        gx, gy = ox + 85, 55
        body, tip = shape(k, gx, gy)
        if g['n'] == 2:
            o += [f'<line x1="{ox+40}" y1="{gy+14}" x2="{gx+6}" y2="{gy+14}" stroke="#CBD5E1" stroke-width="2"/>',
                  f'<line x1="{ox+40}" y1="{gy+36}" x2="{gx+6}" y2="{gy+36}" stroke="#CBD5E1" stroke-width="2"/>',
                  f'<text x="{ox+30}" y="{gy+19}" font-size="13" fill="#CBD5E1" text-anchor="end">A</text>',
                  f'<text x="{ox+30}" y="{gy+41}" font-size="13" fill="#CBD5E1" text-anchor="end">B</text>']
        else:
            o += [f'<line x1="{ox+40}" y1="{gy+25}" x2="{gx}" y2="{gy+25}" stroke="#CBD5E1" stroke-width="2"/>',
                  f'<text x="{ox+30}" y="{gy+30}" font-size="13" fill="#CBD5E1" text-anchor="end">A</text>']
        o += body
        o += [f'<line x1="{tip}" y1="{gy+25}" x2="{ox+cw-25}" y2="{gy+25}" stroke="#CBD5E1" stroke-width="2"/>',
              f'<text x="{ox+cw-18}" y="{gy+30}" font-size="13" fill="#CBD5E1">Y</text>',
              f'<text x="{ox + cw/2}" y="{gy+78}" font-size="13" fill="#FF781F" text-anchor="middle">{g["expr"]}</text>']
        rows = [(a, b) for a in (0, 1) for b in (0, 1)] if g['n'] == 2 else [(a,) for a in (0, 1)]
        ty = gy + 104
        hdr = 'A  B  Y' if g['n'] == 2 else 'A  Y'
        o.append(f'<text x="{ox + cw/2}" y="{ty}" font-size="13" fill="#CBD5E1" text-anchor="middle" xml:space="preserve">{hdr}</text>')
        for j, r in enumerate(rows):
            y = g['f'](*r)
            txt = '  '.join(map(str, r)) + '  ' + str(y)
            col = '#F8FAFC' if y else '#8B949E'
            o.append(f'<text x="{ox + cw/2}" y="{ty + 20*(j+1)}" font-size="14" fill="{col}" text-anchor="middle" xml:space="preserve">{txt}</text>')
    o.append('</g></svg>')
    open(path, 'w').write('\n'.join(o) + '\n')


if __name__ == '__main__':
    build(sys.argv[2].split(','), sys.argv[1])
