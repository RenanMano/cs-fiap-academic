"""Gera um mapa de Karnaugh de 4 variáveis em SVG com agrupamentos (paleta Knowledge Atelier)."""
import sys
GRAY = ['00', '01', '11', '10']

def build(path, ones, groups, titulo, expr):
    cel, ox, oy = 64, 120, 110
    W, H = 760, oy + 4 * cel + 90
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">',
         f'<title id="t">{titulo}</title>',
         f'<desc id="d">Mapa de Karnaugh de 4 variáveis (linhas AB e colunas CD em código Gray) com os agrupamentos que resultam em {expr}.</desc>',
         '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF781F"/><stop offset=".5" stop-color="#FF4500"/><stop offset="1" stop-color="#E60000"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="18" fill="#0D1117"/>', f'<rect width="{W}" height="6" rx="3" fill="url(#g)"/>',
         '<g font-family="Fira Code, Consolas, monospace">',
         f'<text x="30" y="40" font-size="18" font-weight="700" fill="#F8FAFC">{titulo}</text>',
         f'<text x="{ox - 46}" y="{oy - 14}" font-size="14" fill="#CBD5E1">AB\\CD</text>']
    for j, c in enumerate(GRAY):
        o.append(f'<text x="{ox + j*cel + cel/2}" y="{oy - 14}" font-size="15" fill="#CBD5E1" text-anchor="middle">{c}</text>')
    for i, r in enumerate(GRAY):
        o.append(f'<text x="{ox - 22}" y="{oy + i*cel + cel/2 + 5}" font-size="15" fill="#CBD5E1" text-anchor="middle">{r}</text>')
        for j, c in enumerate(GRAY):
            v = 1 if (r + c) in ones else 0
            o.append(f'<rect x="{ox + j*cel}" y="{oy + i*cel}" width="{cel}" height="{cel}" fill="#161B22" stroke="#30363D"/>')
            o.append(f'<text x="{ox + j*cel + cel/2}" y="{oy + i*cel + cel/2 + 6}" font-size="18" text-anchor="middle" fill="{"#F8FAFC" if v else "#6E7681"}">{v}</text>')
    legend_y = oy
    for k, (rects, cor, nome) in enumerate(groups):
        for (r0, c0, nr, nc) in rects:
            pad = 5 + 4 * k
            o.append(f'<rect x="{ox + c0*cel + pad}" y="{oy + r0*cel + pad}" width="{nc*cel - 2*pad}" height="{nr*cel - 2*pad}" rx="14" fill="none" stroke="{cor}" stroke-width="3"/>')
        o.append(f'<rect x="{ox + 4*cel + 50}" y="{legend_y + k*40}" width="22" height="22" rx="6" fill="none" stroke="{cor}" stroke-width="3"/>')
        o.append(f'<text x="{ox + 4*cel + 84}" y="{legend_y + k*40 + 17}" font-size="16" fill="#F8FAFC">{nome}</text>')
    o.append(f'<text x="{ox + 4*cel + 50}" y="{legend_y + len(groups)*40 + 30}" font-size="17" font-weight="700" fill="#FF781F">S = {expr}</text>')
    o.append(f'<text x="30" y="{H - 24}" font-size="12" fill="#CBD5E1">Linhas e colunas em código Gray: vizinhos diferem em 1 bit. As bordas opostas também são vizinhas.</text>')
    o.append('</g></svg>')
    open(path, 'w').write('\n'.join(o) + '\n')

if __name__ == '__main__':
    ones = {'0000', '0010', '0100', '0101', '0110', '1100', '1101', '1110', '1000', '1011', '1010'}
    groups = [
        ([(0, 0, 4, 1), (0, 3, 4, 1)], '#FF781F', "D' (colunas 00 e 10)"),
        ([(1, 0, 2, 2)], '#E60000', "BC'"),
        ([(3, 2, 1, 2)], '#4493F8', "AB'C"),
    ]
    build(sys.argv[1], ones, groups, 'Mapa K: exemplo dos slides', "D' + BC' + AB'C")
