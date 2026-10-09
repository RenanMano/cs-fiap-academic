import math, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import head, text, BG, FG, MUTED, GRID, C1, C2, C3

P, FP = 1.9231, 0.82
S = P / FP; Q = (S**2 - P**2) ** 0.5; phi = math.degrees(math.acos(FP))
W, H = 840, 400
o = head(W, H, 'Triângulo das potências',
         f'Triângulo retângulo com P = {P:.4f} kW no cateto horizontal, Q = {Q:.4f} kvar no vertical e S = {S:.4f} kVA na hipotenusa; ângulo φ de {phi:.1f} graus, fator de potência 0,82.')
o.append(text(W / 2, 40, 'Triângulo das potências — ventilação (Checkpoint 01, Questão 1)', 16, FG, weight='700'))
k = 160  # px por kW
x0, y0 = 110, 340
x1, y1 = x0 + P * k, y0
x2, y2 = x1, y0 - Q * k
o.append(f'<polygon points="{x0},{y0} {x1:.1f},{y1} {x2:.1f},{y2:.1f}" fill="#FF781F22" stroke="none"/>')
o.append(f'<line x1="{x0}" y1="{y0}" x2="{x1:.1f}" y2="{y1}" stroke="{C1}" stroke-width="4"/>')
o.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{C3}" stroke-width="4"/>')
o.append(f'<line x1="{x0}" y1="{y0}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{C2}" stroke-width="4"/>')
o.append(f'<path d="M{x1 - 14:.1f},{y1} L{x1 - 14:.1f},{y1 - 14} L{x1:.1f},{y1 - 14}" fill="none" stroke="{MUTED}"/>')
r = 60
o.append(f'<path d="M{x0 + r},{y0} A{r},{r} 0 0 0 {x0 + r * math.cos(math.radians(phi)):.1f},{y0 - r * math.sin(math.radians(phi)):.1f}" fill="none" stroke="{FG}" stroke-width="1.5"/>')
o.append(text(x0 + 78, y0 - 16, f'φ ≈ {phi:.1f}°'.replace('.', ','), 13, FG, 'start'))
o.append(text((x0 + x1) / 2, y0 + 28, f'P (ativa) = {P:.4f} kW'.replace('.', ','), 14, C1, weight='700'))
o.append(text(x1 + 12, (y1 + y2) / 2, f'Q (reativa) = {Q:.4f} kvar'.replace('.', ','), 14, C3, 'start', '700'))
o.append(text((x0 + x2) / 2 - 20, (y0 + y2) / 2 - 14, f'S (aparente) = {S:.4f} kVA'.replace('.', ','), 14, C2, 'end', '700'))
bx = 600
for i, s in enumerate(['S² = P² + Q²', 'FP = cos φ = P / S', f'FP = {FP:.2f}'.replace('.', ','), 'Se FP &lt; 0,92: multa', '(limite citado nos slides)']):
    o.append(text(bx, 92 + 24 * i, s, 13, MUTED if i > 2 else FG, 'start'))
o += ['</g>', '</svg>']
d = os.path.join(REPO, 'solucoes-em-energia-renovaveis-e-sustentaveis/aula01-19-03-26/assets')
os.makedirs(d, exist_ok=True)
open(f'{d}/triangulo-potencias.svg', 'w').write('\n'.join(o) + '\n')
print(round(S, 4), round(Q, 4), round(phi, 2))
