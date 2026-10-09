import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import *
R = os.path.join(REPO, 'modelagem-matematica-e-computacional') + '/'
cores = [C1, '#F8B400', '#4FC3F7', C3]
funcs = [('a) y = x² − 2x + 1', lambda x: x*x - 2*x + 1, (1, 0)), ('b) y = −x² + 3x − 3', lambda x: -x*x + 3*x - 3, (1.5, -0.75)),
         ('c) y = x² − 3x + 4', lambda x: x*x - 3*x + 4, (1.5, 1.75)), ('d) y = −x² + 10x − 25', lambda x: -x*x + 10*x - 25, (5, 0))]
xr, yr = (-2, 8), (-8, 8)
p = [text(380, 36, 'Lista 1, exercício 8: quatro parábolas e seus vértices', 16, FG, weight='700')]
ax, X, Y = plot_axes(70, 60, 470, 300, xr, yr, range(-2, 9, 2), range(-8, 9, 4))
p += ax
for (nome, f, v), c in zip(funcs, cores):
    p += curve(f, X, Y, xr[0], xr[1], c, yr=yr)
    p.append(f'<circle cx="{X(v[0]):.1f}" cy="{Y(v[1]):.1f}" r="5" fill="{c}" stroke="{BG}" stroke-width="2"/>')
for k, ((nome, f, v), c) in enumerate(zip(funcs, cores)):
    y = 90 + k * 64
    p += [f'<rect x="560" y="{y - 12}" width="14" height="14" rx="3" fill="{c}"/>', text(582, y, nome, 13, FG, 'start'),
          text(582, y + 20, f'vértice ({fmt(v[0])}; {fmt(v[1])})', 12, MUTED, 'start')]
save(R + 'aula03-13-03-26/assets/parabolas-lista1.svg', p, 760, 400, 'Parábolas do exercício 8 da Lista 1',
     'Quatro parábolas: a) x² − 2x + 1, côncava para cima com vértice (1; 0); b) −x² + 3x − 3, côncava para baixo, vértice (1,5; −0,75), sem raízes; c) x² − 3x + 4, côncava para cima, vértice (1,5; 1,75), sem raízes; d) −x² + 10x − 25, côncava para baixo, vértice (5; 0), tocando o eixo x em x = 5.')
