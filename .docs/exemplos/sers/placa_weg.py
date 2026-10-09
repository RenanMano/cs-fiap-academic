# Dados lidos na placa do motor WEG W22 (pasta 09/03): 3,0 kW (4 cv), 220/380 V, 12,9/7,50 A, η = 76,0 %, FP = 0,80
from math import sqrt

P_util = 3000          # W (potência mecânica no eixo)
eta = 0.76             # rendimento
FP = 0.80              # fator de potência (cos φ)

P = P_util / eta                   # potência ativa absorvida da rede
S = P / FP                         # potência aparente
Q = sqrt(S ** 2 - P ** 2)          # potência reativa (triângulo das potências)
print(f"P = {P:7.1f} W | S = {S:7.1f} VA | Q = {Q:7.1f} VAr | perdas = {P - P_util:.1f} W")

# Conferência com a corrente de placa: S = √3 · V · I (motor trifásico)
for V, I in ((220, 12.9), (380, 7.50)):
    S_placa = sqrt(3) * V * I
    print(f"{V} V e {I} A -> √3·V·I = {S_placa:7.1f} VA (diferença de {abs(S_placa - S) / S:.1%})")

print(f"4 cv em W: {4 * 735.5:.0f} W (≈ 3,0 kW da placa)")

# Corrente de partida: a placa informa Ip/In = 5,5
for V, I in ((220, 12.9), (380, 7.50)):
    print(f"Partida direta em {V} V: Ip ≈ 5,5 × {I} = {5.5 * I:.1f} A")
