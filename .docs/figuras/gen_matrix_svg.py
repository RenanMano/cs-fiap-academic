import sys
dados = [0x18, 0x3C, 0x66, 0x66, 0x7E, 0x66, 0x66, 0x00]
cel, ox, oy = 34, 40, 70
W, H = 760, oy + 8 * cel + 50
out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">',
       '<title id="t">Letra A em uma matriz 8×8</title>',
       '<desc id="d">Matriz de 8 por 8 pixels formando a letra A. Ao lado de cada linha aparecem os 8 bits da linha e o valor hexadecimal correspondente: 18, 3C, 66, 66, 7E, 66, 66 e 00.</desc>',
       '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF781F"/><stop offset=".5" stop-color="#FF4500"/><stop offset="1" stop-color="#E60000"/></linearGradient></defs>',
       f'<rect width="{W}" height="{H}" rx="18" fill="#0D1117"/>', f'<rect width="{W}" height="6" rx="3" fill="url(#g)"/>',
       '<g font-family="Fira Code, Consolas, monospace">',
       f'<text x="{ox}" y="40" font-size="18" font-weight="700" fill="#F8FAFC">Imagem → binário → hexadecimal</text>',
       f'<text x="{ox + 8*cel + 40}" y="{oy - 12}" font-size="13" fill="#CBD5E1">linha</text>',
       f'<text x="{ox + 8*cel + 95}" y="{oy - 12}" font-size="13" fill="#CBD5E1">binário</text>',
       f'<text x="{ox + 8*cel + 225}" y="{oy - 12}" font-size="13" fill="#CBD5E1">hex</text>']
for y, v in enumerate(dados):
    bits = format(v, '08b')
    for x, b in enumerate(bits):
        fill = 'url(#g)' if b == '1' else '#161B22'
        out.append(f'<rect x="{ox + x*cel + 2}" y="{oy + y*cel + 2}" width="{cel-4}" height="{cel-4}" rx="6" fill="{fill}" stroke="#30363D"/>')
    ty = oy + y * cel + cel / 2 + 5
    out.append(f'<text x="{ox + 8*cel + 40}" y="{ty}" font-size="15" fill="#CBD5E1">{y}</text>')
    out.append(f'<text x="{ox + 8*cel + 95}" y="{ty}" font-size="15" fill="#F8FAFC">{bits}</text>')
    out.append(f'<text x="{ox + 8*cel + 225}" y="{ty}" font-size="15" fill="#FF781F" font-weight="700">0x{v:02X}</text>')
out.append(f'<text x="{ox}" y="{H - 18}" font-size="12" fill="#CBD5E1">1 = LED aceso · 0 = LED apagado · 8 linhas × 8 bits = 64 bits = 8 bytes</text>')
out.append('</g></svg>')
open(sys.argv[1], 'w').write('\n'.join(out) + '\n')
