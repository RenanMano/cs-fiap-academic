import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import *
R = os.path.join(REPO, 'modelagem-matematica-e-computacional') + '/'
# aula05: g(x) do exercício 52 (p. 88)
xr, yr = (-1, 4), (-3, 3)
p = [text(380, 34, 'Limites laterais: g(x) do exercício 52 (anotações)', 15, FG, weight='700')]
ax, X, Y = plot_axes(70, 60, 400, 280, xr, yr, range(-1, 5), range(-3, 4))
p += ax
p += curve(lambda x: x, X, Y, -1, 1, C1)
p += curve(lambda x: 2 - x*x, X, Y, 1, 2, C1)
p += curve(lambda x: x - 3, X, Y, 2, 4, C1)
dot = lambda x, y, cheio: f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="6" fill="{C1 if cheio else BG}" stroke="{C1}" stroke-width="2.5"/>'
p += [dot(1, 1, False), dot(1, 3, True), dot(2, -2, True), dot(2, -1, False)]
lin = [('g(x) = x,        x &lt; 1', FG), ('g(1) = 3', FG), ('g(x) = 2 − x²,  1 &lt; x ≤ 2', FG), ('g(x) = x − 3,    x &gt; 2', FG), ('', FG),
       ('x→1⁻ e x→1⁺: 1  → lim = 1', C1), ('mas g(1) = 3 (descontínua)', MUTED), ('x→2⁻: −2   x→2⁺: −1', C1), ('→ lim x→2 g(x) não existe', C3)]
for k, (t, c) in enumerate(lin):
    p.append(text(490, 92 + k * 26, t, 12.5, c, 'start'))
save(R + 'aula05-30-03-26/assets/limites-laterais.svg', p, 760, 380, 'Limites laterais da função g do exercício 52',
     'Gráfico por partes: a reta y = x até x = 1 (círculo vazio em (1, 1)), o ponto isolado g(1) = 3, a parábola 2 − x² de 1 a 2 (ponto cheio em (2, −2)) e a reta x − 3 depois de 2 (círculo vazio em (2, −1)). Em x = 1 os limites laterais valem 1, mas g(1) = 3; em x = 2 os laterais são −2 e −1, então o limite não existe.')

# aula06: assíntotas
p = [text(380, 34, 'Assíntotas: vertical (limite infinito) e horizontal (limite no infinito)', 14, FG, weight='700')]
ax, X, Y = plot_axes(60, 60, 300, 270, (-2, 6), (-6, 6), range(-2, 7, 2), range(-6, 7, 3))
p += ax + curve(lambda x: 1 / (x - 2), X, Y, -2, 6, C1, n=800, yr=(-6, 6))
p += [f'<line x1="{X(2):.1f}" y1="60" x2="{X(2):.1f}" y2="330" stroke="{C3}" stroke-dasharray="5 5"/>',
      text(210, 368, 'f(x) = 1/(x − 2):  x→2⁺ → +∞ ;  x→2⁻ → −∞', 11.5, FG)]
ax2, X2, Y2 = plot_axes(430, 60, 300, 270, (0, 20), (-0.2, 1.2), range(0, 21, 5), [0, 0.5, 1])
p += ax2 + curve(lambda x: (x*x - 1) / (x*x + 1), X2, Y2, 0, 20, C1, n=800, yr=(-0.2, 1.2))
p += [f'<line x1="430" y1="{Y2(1):.1f}" x2="730" y2="{Y2(1):.1f}" stroke="{C3}" stroke-dasharray="5 5"/>',
      text(580, 368, 'g(x) = (x² − 1)/(x² + 1):  x→∞ → 1', 11.5, FG)]
save(R + 'aula06-02-04-26/assets/assintotas.svg', p, 760, 380, 'Assíntotas vertical e horizontal',
     'À esquerda, 1/(x − 2) com assíntota vertical tracejada em x = 2: a função vai a +∞ pela direita e a −∞ pela esquerda. À direita, (x² − 1)/(x² + 1) parte de −1 em x = 0 e se aproxima da assíntota horizontal tracejada y = 1 quando x cresce.')
