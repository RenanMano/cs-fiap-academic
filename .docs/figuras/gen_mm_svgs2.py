import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import *
R = os.path.join(REPO, 'modelagem-matematica-e-computacional') + '/'
xr, yr = (-2, 3), (-1, 4)
p = [text(380, 36, 'f(x) = (x² − 1)/(x − 1): o limite existe onde a função não existe', 15, FG, weight='700')]
ax, X, Y = plot_axes(80, 60, 420, 280, xr, yr, range(-2, 4), range(-1, 5))
p += ax
f = lambda x: (x*x - 1) / (x - 1)
p += curve(lambda x: None if abs(x - 1) < 1e-9 else f(x), X, Y, xr[0], xr[1], C1, n=500, yr=yr)
p += [f'<line x1="{X(1):.1f}" y1="{Y(0):.1f}" x2="{X(1):.1f}" y2="{Y(2):.1f}" stroke="{MUTED}" stroke-dasharray="4 4"/>',
      f'<line x1="{X(0):.1f}" y1="{Y(2):.1f}" x2="{X(1):.1f}" y2="{Y(2):.1f}" stroke="{MUTED}" stroke-dasharray="4 4"/>',
      f'<circle cx="{X(1):.1f}" cy="{Y(2):.1f}" r="7" fill="{BG}" stroke="{FG}" stroke-width="2.5"/>']
for k, (a, b) in enumerate([(0.9, 1.9), (0.99, 1.99), (1.01, 2.01), (1.1, 2.1)]):
    p.append(text(530, 120 + k * 22, f'f({fmt(a)}) = {fmt(b)}', 13, FG, 'start'))
p += [text(530, 90, 'perto de x = 1:', 13, MUTED, 'start'),
      text(530, 230, 'f(1) não existe', 13, C3, 'start', '700'),
      text(530, 252, '(divisão por zero)', 12, MUTED, 'start'),
      text(530, 290, 'mas  lim f(x) = 2', 13, C1, 'start', '700'),
      text(560, 306, 'x→1', 10, C1, 'start'),
      text(530, 334, 'pois f(x) = x + 1 se x ≠ 1', 12, MUTED, 'start')]
save(R + 'aula04-20-03-26/assets/limite-buraco.svg', p, 760, 380, 'Limite de (x² − 1)/(x − 1) quando x tende a 1',
     'Gráfico da reta y = x + 1 com um buraco (círculo vazio) no ponto (1, 2), porque a função original não está definida em x = 1. Os valores f(0,9) = 1,9, f(0,99) = 1,99, f(1,01) = 2,01 e f(1,1) = 2,1 se aproximam de 2, que é o limite.')
