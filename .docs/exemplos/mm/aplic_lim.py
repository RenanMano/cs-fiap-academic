import math

# Lista 5 — conferência do gabarito
C = lambda x: 12 * x / (100 - x)                         # 1) custo de remover x% do óleo
print("1a)", C(25), C(50), "| 1c) C(99.9) =", round(C(99.9)))
conc = lambda t: 30 * 25 * t / (5000 + 25 * t)           # 2) sal (g/L) após t minutos
print("2) C(t) para t = 10, 1000, 1e6:", [round(conc(t), 3) for t in (10, 1000, 1e6)])
media = lambda x: (100 * x + 200_000) / x               # 3) custo médio das mesas
print("3) custo médio com 1e6 mesas:", round(media(1e6), 2))
f5 = lambda x: 120 * x**2 / (x**2 + 4)                   # 5) arrecadação (milhões)
print("5a)", f5(1), f5(2), round(f5(12), 4), "| 5b) x = 1e6:", round(f5(1e6), 4))
print("10)", round(70 * math.exp(0.04 * 3), 2), round(690 * math.exp(0.05 * 2), 2))
print("11)", round(1000 * 1.08**3, 2), round(1000 * math.exp(0.08 * 3), 2))
print("12)", round(5000 * math.exp(0.10 * 12), 2), "| 13)", round(1000 * math.exp(0.10), 2))
