import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import *
from statistics import NormalDist
R = os.path.join(REPO, 'modelagem-linear-para-aprendizado-de-maquina') + '/'

# aula09: alturas N(175, 10)
nd = NormalDist(175, 10)
pa, pc = nd.cdf(164), nd.cdf(174) - nd.cdf(164)
p = [text(380, 40, 'Alturas ~ N(μ = 175 cm, σ = 10 cm)', 17, FG, weight='700')]
curve, X, Y = normal_curve(60, 300, 640, 220, 175, 10, [(130, 164, C3), (164, 174, C1)], [145, 155, 164, 174, 185, 195, 205])
p += curve
p += [text(X(146), 196, f'P(X ≤ 164)', 13, C3), text(X(146), 214, f'≈ {pa:.4f}'.replace('.', ','), 13, C3, weight='700'),
      text(X(169), 170, f'P(164 ≤ X ≤ 174)', 13, FG), text(X(169), 188, f'≈ {pc:.4f}'.replace('.', ','), 13, FG, weight='700'),
      text(X(200), 140, f'P(X ≥ 164) = 1 − P(X ≤ 164)', 12, MUTED), text(X(200), 158, f'≈ {1 - pa:.4f}'.replace('.', ','), 12, MUTED),
      text(380, 350, 'área total sob a curva = 1 · probabilidade = área', 13, MUTED)]
save(R + 'aula09-03-08-26/assets/normal-alturas.svg', p, 760, 372, 'Probabilidades na distribuição normal das alturas',
     f'Curva normal de média 175 e desvio padrão 10. A área à esquerda de 164, sombreada em vermelho, vale aproximadamente {pa:.4f}; a área entre 164 e 174, em laranja, vale aproximadamente {pc:.4f}; a área à direita de 164 vale aproximadamente {1 - pa:.4f}.')

# aula09: regra empírica
z = NormalDist()
p = [text(380, 40, 'Regra empírica (68 – 95 – 99,7)', 17, FG, weight='700')]
curve, X, Y = normal_curve(60, 300, 640, 210, 0, 1, [(-3, 3, '#7A1F00'), (-2, 2, C2), (-1, 1, C1)], [-3, -2, -1, 0, 1, 2, 3],
                           label_fmt=lambda t: 'μ' if t == 0 else f'μ{"+" if t > 0 else "−"}{abs(t)}σ')
p += curve
for k, y in ((1, 338), (2, 358), (3, 378)):
    v = z.cdf(k) - z.cdf(-k)
    p += [f'<line x1="{X(-k):.1f}" y1="{y - 4}" x2="{X(k):.1f}" y2="{y - 4}" stroke="{MUTED}"/>',
          text(X(k) + 8, y, f'{v * 100:.2f}%'.replace('.', ','), 12, FG, 'start', weight='700')]
save(R + 'aula09-03-08-26/assets/regra-empirica.svg', p, 760, 396, 'Regra empírica da distribuição normal',
     'Curva normal com faixas sombreadas: entre μ−σ e μ+σ estão cerca de 68,27% dos valores; entre μ−2σ e μ+2σ, 95,45%; entre μ−3σ e μ+3σ, 99,73%.')
