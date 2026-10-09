# Exemplo do slide "Motor trifásico", reorganizado como função (sem input) para ser testável
def potencias_motor(potencia_util, rendimento_pct, fator_potencia):
    potencia_ativa = potencia_util / (rendimento_pct / 100)          # P = P_útil / η
    potencia_aparente = potencia_ativa / fator_potencia               # S = P / FP
    potencia_reativa = (potencia_aparente ** 2 - potencia_ativa ** 2) ** 0.5   # Q = √(S² − P²)
    return potencia_ativa, potencia_aparente, potencia_reativa

for util, eta, fp in [(1.5, 78, 0.82), (1.5, 78, 0.96)]:
    P, S, Q = potencias_motor(util, eta, fp)
    print(f"P_útil={util} kW, η={eta}%, FP={fp}:")
    print(f"  P (Ativa): {P:.2f} kW | Q (Reativa): {Q:.2f} kVAr | S (Aparente): {S:.2f} kVA")

# Energia: E = P × Δt (8 h por dia, 22 dias)
P, _, _ = potencias_motor(1.5, 78, 0.82)
print(f"Consumo mensal: {P * 8 * 22:.1f} kWh")
