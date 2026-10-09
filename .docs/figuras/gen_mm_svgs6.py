import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import *
R = os.path.join(REPO, 'modelagem-matematica-e-computacional') + '/'
f = lambda x: -(x ** 2) / 4 + 2 * x
p = [text(380, 34, 'Área sob f(x) = −x²/4 + 2x em [0, 8]: retângulos → integral', 15, FG, weight='700')]
paineis = [(60, 1, 'base = 1: 21,5'), (420, 0.25, 'base = 0,25: 21,34')]
for x0, base, rot in paineis:
    ax, X, Y = plot_axes(x0, 64, 300, 250, (0, 8), (0, 4.5), range(0, 9, 2), range(0, 5))
    p += ax
    n = round(8 / base)
    for k in range(n):
        a = k * base; hgt = f(a + base / 2)
        p.append(f'<rect x="{X(a):.1f}" y="{Y(hgt):.1f}" width="{X(a + base) - X(a):.1f}" height="{Y(0) - Y(hgt):.1f}" fill="{C1}" fill-opacity=".45" stroke="{C1}" stroke-width="{1 if base == 1 else 0.4}"/>')
    p += curve(f, X, Y, 0, 8, FG, width=2)
    p.append(text(x0 + 150, 350, rot, 13, FG, weight='700'))
p.append(text(380, 376, 'valor exato (Teorema Fundamental do Cálculo): 64/3 ≈ 21,333', 12.5, C1))
save(R + 'aula10-20-08-26/assets/soma-riemann.svg', p, 760, 392, 'Soma de Riemann convergindo para a integral',
     'Dois gráficos da parábola −x²/4 + 2x entre 0 e 8, com altura máxima 4 em x = 4, preenchida por retângulos: com base 1, a soma das áreas é 21,5; com base 0,25, é cerca de 21,34. O valor exato da integral é 64/3, aproximadamente 21,333.')

L = lambda x: 0.7604 * x ** 2.0926
p = [text(380, 34, 'Curva de Lorenz ajustada (Brasil, quintis) e Índice de Gini', 15, FG, weight='700')]
ax, X, Y = plot_axes(80, 60, 300, 300, (0, 1), (0, 1), [0, 0.2, 0.4, 0.6, 0.8, 1], [0, 0.2, 0.4, 0.6, 0.8, 1])
p += ax
pts = ' '.join(f'{X(k / 100):.1f},{Y(k / 100):.1f}' for k in range(101)) + ' ' + ' '.join(f'{X(k / 100):.1f},{Y(L(k / 100)):.1f}' for k in range(100, -1, -1))
p.append(f'<polygon points="{pts}" fill="{C1}" fill-opacity=".35"/>')
p += curve(lambda x: x, X, Y, 0, 1, MUTED, width=2, dash='6 4') + curve(L, X, Y, 0, 1, C1, width=2.5)
for xi, yi in [(0, 0), (0.2, 0.03), (0.4, 0.1), (0.6, 0.22), (0.8, 0.42), (1, 1)]:
    p.append(f'<circle cx="{X(xi):.1f}" cy="{Y(yi):.1f}" r="4.5" fill="{FG}"/>')
lin = [('— — y = x (igualdade perfeita)', MUTED), ('—— L(x) = 0,7604·x^2,0926', C1), ('●  dados da Tabela 1 (PNAD)', FG), ('', FG),
       ('área sombreada = ∫₀¹ (x − L(x)) dx', FG), ('                ≈ 0,2541', FG), ('Gini = 2 × área ≈ 0,508', C1), ('→ desigualdade extrema (> 0,50)', C3)]
for k, (t, c) in enumerate(lin):
    p.append(text(410, 100 + k * 28, t, 12.5, c, 'start', '700' if 'Gini' in t else '400'))
save(R + 'aula10-20-08-26/assets/curva-lorenz-gini.svg', p, 760, 400, 'Curva de Lorenz e Índice de Gini',
     'Gráfico de 0 a 1 nos dois eixos com a reta de igualdade y = x tracejada, a curva de Lorenz ajustada L(x) = 0,7604·x elevado a 2,0926 abaixo dela e os seis pontos da tabela de renda acumulada (0; 0,03; 0,1; 0,22; 0,42; 1). A área entre as curvas, sombreada, vale cerca de 0,2541, e o Índice de Gini, o dobro, cerca de 0,508.')
