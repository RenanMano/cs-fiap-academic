import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import *
R = os.path.join(REPO, 'modelagem-linear-para-aprendizado-de-maquina') + '/'
zc = -1.96
p = [text(380, 40, 'Teste bilateral (α = 5%): peso médio da zebra', 17, FG, weight='700')]
curve, X, Y = normal_curve(60, 290, 640, 200, 0, 1, [(-4, -1.96, C3), (1.96, 4, C3)], [-3, -2, -1, 0, 1, 2, 3])
p += curve
p += [text(X(-3.1), 220, 'rejeita H₀', 13, C3, weight='700'), text(X(-3.1), 238, 'α/2 = 2,5%', 12, C3),
      text(X(3.1), 220, 'rejeita H₀', 13, C3, weight='700'), text(X(3.1), 238, 'α/2 = 2,5%', 12, C3),
      text(X(0), 160, 'aceita H₀', 13, FG, weight='700'), text(X(0), 178, '1 − α = 95%', 12, FG),
      f'<line x1="{X(-1.96):.1f}" y1="300" x2="{X(-1.96):.1f}" y2="96" stroke="{MUTED}" stroke-dasharray="4 4"/>',
      f'<line x1="{X(1.96):.1f}" y1="300" x2="{X(1.96):.1f}" y2="96" stroke="{MUTED}" stroke-dasharray="4 4"/>',
      text(X(-1.96), 90, '−Zα/2 = −1,96', 12, MUTED), text(X(1.96), 90, 'Zα/2 = 1,96', 12, MUTED),
      f'<circle cx="{X(-2.5):.1f}" cy="290" r="7" fill="{FG}"/>',
      text(380, 336, 'ponto branco: Zc = −2,5 → rejeita H₀ (o peso médio mudou)', 13, FG, weight='700')]
save(R + 'aula13-11-09-26/assets/regiao-critica-bilateral.svg', p, 760, 356, 'Região crítica de um teste bilateral',
     'Curva normal padrão com as duas caudas abaixo de −1,96 e acima de 1,96 sombreadas como regiões de rejeição de H0 (2,5% cada) e a região central de aceitação (95%). A estatística Zc = −2,5 do exemplo da zebra está na cauda esquerda, portanto H0 é rejeitada.')
