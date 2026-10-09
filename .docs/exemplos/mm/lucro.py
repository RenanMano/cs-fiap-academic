# Atividade "Lucro Ótimo": (R$ 280 → 50 pessoas) e (R$ 240 → 60 pessoas)
a = (60 - 50) / (240 - 280)                 # inclinação da reta participantes × preço
b = 50 - a * 280
participantes = lambda p: a * p + b
custo_fixo, custo_unit = 1_000 + 10_000, 60
lucro = lambda p: (p - custo_unit) * participantes(p) - custo_fixo

print(f"n(p) = {a}p + {b:g}")
# L(p) = (p − 60)(−0,25p + 120) − 11000  →  L'(p) = −0,5p + 135 = 0
p_otimo = (b + (-a) * custo_unit) / (2 * -a)
print(f"preço ótimo = R$ {p_otimo:.2f} | participantes = {participantes(p_otimo):.1f} | lucro máximo = R$ {lucro(p_otimo):.2f}")
print(f"lucro a R$ 250 (preço atual): R$ {lucro(250):.2f}")
h = 1e-6
print("L'(p ótimo) ≈", round((lucro(p_otimo + h) - lucro(p_otimo - h)) / (2 * h), 6))
