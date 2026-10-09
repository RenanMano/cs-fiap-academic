import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import *
R = os.path.join(REPO, 'modelagem-matematica-e-computacional') + '/'
xr, yr = (-1.5, 3), (-1, 6)
p = [text(380, 34, 'Atividade: secantes por A(2, 4) em y = x² tendem à tangente', 15, FG, weight='700')]
ax, X, Y = plot_axes(70, 56, 430, 290, xr, yr, [-1, 0, 1, 2, 3], range(0, 7, 2))
p += ax + curve(lambda x: x * x, X, Y, xr[0], xr[1], FG, yr=yr, width=2)
cores = ['#4FC3F7', '#F8B400', C2]
for (xd, c) in zip((1, 1.5, 1.9), cores):
    m = (4 - xd * xd) / (2 - xd)
    p += curve(lambda x, m=m: 4 + m * (x - 2), X, Y, xr[0], xr[1], c, yr=yr, width=1.5, dash='6 4')
    p.append(f'<circle cx="{X(xd):.1f}" cy="{Y(xd * xd):.1f}" r="4.5" fill="{c}"/>')
p += curve(lambda x: 4 * x - 4, X, Y, xr[0], xr[1], C3, yr=yr, width=2.5)
p.append(f'<circle cx="{X(2):.1f}" cy="{Y(4):.1f}" r="6" fill="{C3}" stroke="{FG}" stroke-width="2"/>')
p.append(text(X(2) - 10, Y(4) - 10, 'A', 13, FG, 'end', '700'))
leg = [('#4FC3F7', 'D = (1; 1): m = 3'), ('#F8B400', 'D = (1,5; 2,25): m = 3,5'), (C2, 'D = (1,9; 3,61): m = 3,9'), (C3, "tangente: m = f'(2) = 4"), (FG, 'y = x²')]
for k, (c, t) in enumerate(leg):
    y = 100 + k * 34
    p += [f'<line x1="520" y1="{y - 4}" x2="548" y2="{y - 4}" stroke="{c}" stroke-width="3"/>', text(556, y, t, 12.5, FG, 'start')]
p.append(text(520, 290, 'y − 4 = 4(x − 2)  →  y = 4x − 4', 12.5, C3, 'start', '700'))
save(R + 'aula09-11-05-26/assets/secante-tangente.svg', p, 760, 380, 'Retas secantes convergindo para a reta tangente',
     'Parábola y = x² com o ponto A(2, 4). Três retas secantes tracejadas ligam A a pontos D com x = 1, 1,5 e 1,9, com inclinações 3, 3,5 e 3,9. A reta tangente em A, y = 4x − 4, tem inclinação 4, igual à derivada em x = 2.')
