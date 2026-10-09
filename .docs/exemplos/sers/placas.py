# Exercício da Atividade - Motores (16/03): P, S e Q das placas da pasta (solução proposta para estudo)
from math import sqrt

def potencias(PU, n, FP):
    """Mesma lógica do notebook Aula_02_SERS.ipynb, sem input(): PU em W, n e FP entre 0 e 1."""
    P = PU / n
    S = P / FP
    Q = (S ** 2 - P ** 2) ** 0.5
    return P, S, Q

# (placa, PU em W, rendimento, FP, tensão de referência em V, corrente de placa em A)
placas = [
    ("motor1 WEG W22 Premium 0,75 kW", 750, 0.830, 0.82, 220, 2.89),
    ("motor2 WEG Alto Rendimento Plus 7,5 kW", 7500, 0.910, 0.82, 220, 26.4),
    ("motor3 Siemens 11 kW (50 Hz)", 11000, 0.85, 0.88, 400, 20.5),
    ("motor4 WEG W40 Premium 300 kW", 300000, 0.958, 0.89, 380, 535),
]
print(f"{'placa':40} {'P (W)':>10} {'S (VA)':>10} {'Q (VAr)':>10} {'√3·V·I (VA)':>12}")
for nome, PU, n, FP, V, I in placas:
    P, S, Q = potencias(PU, n, FP)
    print(f"{nome:40} {P:10.0f} {S:10.0f} {Q:10.0f} {sqrt(3) * V * I:12.0f}")

# Exemplo do próprio notebook (placa WEG W22 de 3 kW): saída registrada 3947 W, 4934 VA e 2960 VAr
P, S, Q = potencias(3000, 0.76, 0.80)
print(f"Notebook: P = {int(P)} W, S = {int(S)} VA, Q = {int(Q)} VAr")
