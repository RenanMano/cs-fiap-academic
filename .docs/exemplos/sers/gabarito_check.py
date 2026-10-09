# Conferência da consistência interna do gabarito: Q = √(S² − P²) e FP = P / S
casos = {                       # (P em kW, S em kVA, Q em kvar), valores do gabarito
    "Ventilação (atual)": (1.9231, 2.3452, 1.3423),
    "Bomba (atual)":      (2.7160, 3.2334, 1.7544),
    "Bomba (degradada)":  (2.9333, 3.7607, 2.3534),
    "Compressor":         (8.6207, 9.7962, 4.6530),
    "Motor A":            (6.4706, 7.5239, 3.8394),
    "Motor B":            (6.6265, 7.7959, 4.1067),
}
for nome, (P, S, Q) in casos.items():
    q_calc = (S**2 - P**2) ** 0.5
    print(f"{nome:<19} FP = {P / S:.2f} | Q calculado = {q_calc:.4f} | gabarito = {Q:.4f}")

# Consumo mensal do compressor: E = P × Δt, com Δt = 720 h
print(f"Consumo com manutenção: {8.6207 * 720:.2f} kWh")
