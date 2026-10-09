import random

def potencia_kw(tensao_v, corrente_a):
    return tensao_v * corrente_a / 1000                # P = V · I

print(f"painel do infográfico: 229 V × 32,3 A = {potencia_kw(229, 32.3):.2f} kW")

random.seed(28)
energia_kwh = 0.0
for minuto in range(1, 6):                             # 5 leituras simuladas, uma por minuto
    v = 229 + random.uniform(-2, 2)
    i = 32.3 + random.uniform(-1, 1)
    p = potencia_kw(v, i)
    energia_kwh += p * (1 / 60)                        # kW × h = kWh
    print(f"min {minuto}: {v:6.1f} V {i:5.1f} A -> {p:.2f} kW | acumulado {energia_kwh:.3f} kWh")

pontos = {"Atendimento ao desafio": 45, "Aplicabilidade": 15, "Inovação": 15, "Evolução/maturidade": 15, "Clareza do pitch": 10}
print("pontuação máxima do pitch:", sum(pontos.values()))
