def d(f, a, h=1e-6):
    return round((f(a + h) - f(a - h)) / (2 * h), 4)

# secantes por A(2, 4) em y = x²: a inclinação tende a f'(2) = 4
for xd in (1, 1.5, 1.9, 1.99, 1.999):
    print(f"D = ({xd}, {xd**2:.4f}): inclinação AD = {(4 - xd**2) / (2 - xd):.4f}")

# regras práticas conferidas numericamente
f1 = lambda x: x**8 + 12*x**5 + 10*x**3 - 6*x + 5      # f' = 8x⁷ + 60x⁴ + 30x² − 6
print("p.154: f'(1) numérico =", d(f1, 1), "| pela regra:", 8 + 60 + 30 - 6)
f2 = lambda x: 3*x**2 - x**3                           # y' = 6x − 3x²
m = d(f2, 1)
print(f"p.157: tangente a 3x² − x³ em (1, 2): m = {m} → y = {m:g}x − {m - 2:g}")
f3 = lambda x: x - x**0.5                              # y' = 1 − 1/(2√x)
m = d(f3, 1)
print(f"p.157: tangente a x − √x em (1, 0): m = {m} → y = {m:g}x − {m:g}")
