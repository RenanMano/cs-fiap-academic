import os, sys, math
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import *
R = os.path.join(REPO, 'modelagem-matematica-e-computacional') + '/'
C, i = 100_000, 0.10
pts = [('anual', 1), ('semestral', 2), ('mensal', 12), ('semanal', 52), ('diária', 365), ('horária', 8760)]
x0, y0, w, h = 90, 70, 600, 250
lo, hi = 109_900, 110_600
X = lambda n: x0 + 30 + (w - 60) * math.log10(n) / math.log10(8760)
Y = lambda v: y0 + h - h * (v - lo) / (hi - lo)
p = [text(380, 36, 'R$ 100.000 a 10% a.a. por 1 ano: capitalizar mais vezes → limite contínuo', 14, FG, weight='700')]
for v in range(110_000, 110_601, 200):
    p += [f'<line x1="{x0}" y1="{Y(v):.1f}" x2="{x0 + w}" y2="{Y(v):.1f}" stroke="{GRID}"/>', text(x0 - 8, Y(v) + 4, f'{v:,}'.replace(',', '.'), 11, MUTED, 'end')]
lim = C * math.exp(i)
p += [f'<line x1="{x0}" y1="{Y(lim):.1f}" x2="{x0 + w}" y2="{Y(lim):.1f}" stroke="{C3}" stroke-dasharray="6 5" stroke-width="2"/>',
      text(x0 + 6, Y(lim) - 8, f'limite: C·e^0,1 = {lim:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'), 12, C3, 'start', '700')]
prev = None
for nome, n in pts:
    v = C * (1 + i / n) ** n
    if prev: p.append(f'<line x1="{prev[0]:.1f}" y1="{prev[1]:.1f}" x2="{X(n):.1f}" y2="{Y(v):.1f}" stroke="{C1}" stroke-width="2"/>')
    prev = (X(n), Y(v))
for k, (nome, n) in enumerate(pts):
    v = C * (1 + i / n) ** n
    dy = 28 if k == 1 else 0
    p += [f'<circle cx="{X(n):.1f}" cy="{Y(v):.1f}" r="6" fill="{C1}" stroke="{BG}" stroke-width="2"/>', text(X(n), y0 + h + 18 + dy, nome, 11, MUTED),
          text(X(n), y0 + h + 31 + dy, f'n = {n}', 10, MUTED)]
p.append(text(x0 + w / 2, y0 + h + 70, 'número de capitalizações por ano (escala logarítmica)', 12, MUTED))
save(R + 'aula07-15-04-26/assets/capitalizacao-continua.svg', p, 760, 412, 'Montante com capitalizações cada vez mais frequentes',
     'Montantes de R$ 100.000 a 10% ao ano por um ano: 110.000 (anual), 110.250 (semestral), 110.471,31 (mensal), 110.506,48 (semanal), 110.515,58 (diária) e 110.517,03 (horária), aproximando-se da linha tracejada do limite contínuo 110.517,09.')
