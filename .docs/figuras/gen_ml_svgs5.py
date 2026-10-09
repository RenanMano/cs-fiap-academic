import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI); sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'exemplos', 'ml'))
from stat_svg import *
from regressao import regressao_simples
R = os.path.join(REPO, 'modelagem-linear-para-aprendizado-de-maquina') + '/'
x = [1, 2, 3, 4, 5, 6]; y = [3, 6, 7, 10, 10, 12]
m = regressao_simples(x, y)
x0, y0, w, h = 90, 320, 600, 240
X = lambda v: x0 + w * v / 10
Y = lambda v: y0 - h * v / 20
p = [text(380, 40, 'Poluente × dano ecológico (exemplo dos slides)', 17, FG, weight='700')]
for k in range(0, 21, 5):
    p += [f'<line x1="{x0}" y1="{Y(k):.1f}" x2="{x0 + w}" y2="{Y(k):.1f}" stroke="{GRID}"/>', text(x0 - 8, Y(k) + 4, str(k), 11, MUTED, 'end')]
for k in range(0, 11, 1):
    p += [text(X(k), y0 + 18, str(k), 11, MUTED)]
p += [f'<line x1="{x0}" y1="{y0}" x2="{x0 + w}" y2="{y0}" stroke="{MUTED}"/>',
      text(x0 + w / 2, y0 + 40, 'Quantidade de poluente (µg/L)', 12, MUTED),
      f'<text x="{x0 - 40}" y="{y0 - h / 2}" font-size="12" fill="{MUTED}" text-anchor="middle" transform="rotate(-90 {x0 - 40} {y0 - h / 2})">Dano ecológico</text>']
a, b = m['alfa'], m['beta']
p.append(f'<line x1="{X(0):.1f}" y1="{Y(a):.1f}" x2="{X(9.5):.1f}" y2="{Y(a + b * 9.5):.1f}" stroke="{C1}" stroke-width="2.5"/>')
p.append(f'<line x1="{X(6):.1f}" y1="{Y(a + b * 6):.1f}" x2="{X(9.5):.1f}" y2="{Y(a + b * 9.5):.1f}" stroke="{BG}" stroke-width="3" stroke-dasharray="6 6"/>')
for xi, yi in zip(x, y):
    p.append(f'<line x1="{X(xi):.1f}" y1="{Y(yi):.1f}" x2="{X(xi):.1f}" y2="{Y(a + b * xi):.1f}" stroke="{MUTED}" stroke-dasharray="2 3"/>')
    p.append(f'<circle cx="{X(xi):.1f}" cy="{Y(yi):.1f}" r="6" fill="{FG}"/>')
p.append(f'<circle cx="{X(9):.1f}" cy="{Y(a + b * 9):.1f}" r="7" fill="none" stroke="{C3}" stroke-width="2.5"/>')
p.append(text(X(9) - 10, Y(a + b * 9) - 14, f'previsão p/ 9: {a + b * 9:.2f}'.replace('.', ','), 12, C3, 'end', '700'))
p.append(text(X(0.3), Y(18.5), f'Ŷ = {a:.2f} + {b:.4f}·X'.replace('.', ','), 14, FG, 'start', '700'))
p.append(text(X(0.3), Y(16.8), f'r = {m["r"]:.4f}   R² = {m["r2"]:.4f}'.replace('.', ','), 12, MUTED, 'start'))
save(R + 'aula15-28-09-26/assets/regressao-poluente.svg', p, 760, 380, 'Regressão linear simples: poluente e dano ecológico',
     f'Gráfico de dispersão com seis pontos (1,3), (2,6), (3,7), (4,10), (5,10), (6,12) e a reta de mínimos quadrados Y = 2 + 1,7143X, com resíduos verticais tracejados. A reta é estendida até X = 9, onde a previsão vale cerca de 17,43, fora da faixa observada (extrapolação).')
