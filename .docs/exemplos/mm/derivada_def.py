S = lambda t: t ** 2                               # função horária S(t) = t²

print("velocidade média entre 2,5 s e 10 s:", (S(10) - S(2.5)) / (10 - 2.5), "m/s")
for h in (1, 0.1, 0.001, 0.00001):                 # intervalo encolhendo: h → 0
    print(f"h = {h:<8} taxa média em [2,5; 2,5 + h] = {(S(2.5 + h) - S(2.5)) / h:.5f}")

def derivada(f, a, h=1e-6):
    """f'(a) ≈ [f(a + h) − f(a − h)] / 2h (diferença central)."""
    return round((f(a + h) - f(a - h)) / (2 * h), 4)

f = lambda x: x ** 3 - 3 * x
print("f(x) = x² : f'(1) =", derivada(lambda x: x ** 2, 1), "| f'(−2) =", derivada(lambda x: x ** 2, -2))
print("f(x) = x³ − 3x : f'(1) =", derivada(f, 1), "| f'(0) =", derivada(f, 0))
