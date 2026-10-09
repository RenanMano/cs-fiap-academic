import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
from stat_svg import *
import random
from statistics import mean
import numpy as np
R = os.path.join(REPO, 'modelagem-linear-para-aprendizado-de-maquina') + '/'

random.seed(42)
populacao = [random.expovariate(1 / 10) for _ in range(100_000)]
m2 = [mean(random.sample(populacao, 2)) for _ in range(2_000)]
m30 = [mean(random.sample(populacao, 30)) for _ in range(2_000)]
pc, pe = np.histogram(populacao, bins=10, range=(0, 50))
c2, e2 = np.histogram(m2, bins=10, range=(0, 30))
c30, e30 = np.histogram(m30, bins=10, range=(5, 15))

p = [text(570, 40, 'Teorema Central do Limite: população exponencial (média 10)', 16, FG, weight='700')]
panels = [(60, 'População (100 mil valores)', pc / pc.sum() * 100, pe), (420, 'Médias de amostras n = 2', c2 / 20, e2), (780, 'Médias de amostras n = 30', c30 / 20, e30)]
for x0, title, cnt, edges in panels:
    p.append(text(x0 + 150, 76, title, 13, MUTED))
    p += hist(x0 + 20, 300, 280, 200, [float(e) for e in edges], [round(float(c)) for c in cnt], 60 if cnt.max() > 40 else 40, 10, '%', '')
save(R + 'aula10-11-08-26/assets/tcl-simulacao.svg', p, 1140, 350, 'Simulação do Teorema Central do Limite',
     'Três histogramas em porcentagem: a população exponencial é muito assimétrica, concentrada perto de zero; as médias de amostras de tamanho 2 ainda são assimétricas; as médias de amostras de tamanho 30 formam um sino aproximadamente simétrico em torno de 10.')
print(pc, c2, c30)
