f = lambda x: -(x ** 2) / 4 + 2 * x            # mesma função do notebook da aula seguinte

def soma_riemann(f, a, b, base):
    """Soma das áreas de retângulos com altura no ponto médio de cada intervalo."""
    n = round((b - a) / base)
    return sum(f(a + (k + 0.5) * base) * base for k in range(n))

for base in (2, 1, 0.5, 0.01):
    print(f"base = {base:<5} -> área ≈ {soma_riemann(f, 0, 8, base):.6f}")

F = lambda x: -(x ** 3) / 12 + x ** 2          # primitiva: F'(x) = f(x)
print(f"Teorema Fundamental: F(8) − F(0) = {F(8) - F(0):.6f}  (= 64/3)")
