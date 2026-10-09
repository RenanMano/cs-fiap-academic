import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import *
from collections import Counter
import numpy as np
R = os.path.join(REPO, 'modelagem-linear-para-aprendizado-de-maquina') + '/'

# aula06: qualitativos
dados1 = ["Sim"] * 20 + ["Não"] * 45
c = Counter(dados1)
p = [text(380, 40, 'Respostas da entrevista (65 participantes)', 17, FG, weight='700')]
p += [text(190, 76, 'Gráfico de setores', 13, MUTED)]
p += pie(190, 210, 105, ['Não', 'Sim'], [c['Não'], c['Sim']], [C2, C1])
p += [text(560, 76, 'Gráfico de barras', 13, MUTED)]
p += bars(440, 330, 260, 230, ['Sim', 'Não'], [c['Sim'], c['Não']], 50, 10, 'Frequência')
save(R + 'aula06-27-04-26/assets/graficos-qualitativos.svg', p, 760, 380, 'Gráficos para variável qualitativa',
     'Mesmos dados (20 respostas Sim e 45 Não) em dois gráficos: setores com 69,23% para Não e 30,77% para Sim, e barras com alturas 20 e 45.')

# aula06: quantitativos
dados2 = [15, 17, 15, 15, 17, 14, 18, 15, 15, 17, 15, 12, 15, 15, 18]
cnt, edges = np.histogram(dados2, bins=3)
p = [text(380, 40, 'dados2: 15 observações entre 12 e 18', 17, FG, weight='700')]
p += [text(200, 76, 'Histograma (bins=3)', 13, MUTED)]
p += hist(90, 320, 240, 220, list(edges), list(cnt), 10, 2, 'Frequência', 'Intervalos dos dados')
p += [text(560, 76, 'Boxplot', 13, MUTED)]
bp, s = boxplot(470, 100, 60, 220, dados2, 11, 19, 1)
p += bp
save(R + 'aula06-27-04-26/assets/graficos-quantitativos.svg', p, 760, 380, 'Histograma e boxplot da variável quantitativa',
     f'Histograma com 3 classes de largura 2 (12 a 14: 1; 14 a 16: 9; 16 a 18: 5) e boxplot com mínimo 12, Q1 15, mediana 15, Q3 17 e máximo 18, sem outliers.')
print(cnt, edges, s)

# aula07: anatomia do boxplot com outlier — x dos slides + exemplo com outlier
x = [2, 4, 3, 4, 5, 2, 4]
y = [2, 4, 3, 4, 5, 2, 4, 12]
p = [text(380, 40, 'Anatomia do boxplot', 17, FG, weight='700')]
p += [text(150, 70, 'x = [2, 4, 3, 4, 5, 2, 4]', 12, MUTED)]
b1, s1 = boxplot(110, 90, 60, 250, x, 0, 13, 1)
p += b1
p += [text(530, 70, 'mesmo x com o valor 12 incluído', 12, MUTED)]
b2, s2 = boxplot(470, 90, 60, 250, y, 0, 13, 1, annotate=False)
p += b2
Yv = lambda v: 90 + 250 * (13 - v) / 13
p += [text(552, Yv(12) + 4, 'outlier: 12 &gt; LS = ' + fmt(s2['ls']), 12, C3, 'start')]
p += [text(380, 372, 'LI = Q1 − 1,5·(Q3 − Q1)    LS = Q3 + 1,5·(Q3 − Q1)', 13, FG)]
save(R + 'aula07-06-05-26/assets/boxplot-anatomia.svg', p, 760, 390, 'Anatomia do boxplot',
     f'Boxplot de x = [2, 4, 3, 4, 5, 2, 4] com Q1 = 2,5, mediana = 4, Q3 = 4, bigodes em 2 e 5; ao lado, o mesmo conjunto com o valor 12, que fica acima do limite superior {fmt(s2["ls"])} e aparece como outlier.')
print(s1, s2)
