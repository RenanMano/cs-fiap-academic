def lim_numerico(f, a, h=1e-6):
    """Aproxima o limite pelos dois lados: f(a − h) e f(a + h)."""
    return round(f(a - h), 4), round(f(a + h), 4)

exemplos = {
    "lim x→5  (2x² − 3x + 4)":              (lambda x: 2*x**2 - 3*x + 4, 5),
    "lim x→−2 (x³ + 2x² − 1)/(5 − 3x)":     (lambda x: (x**3 + 2*x**2 - 1) / (5 - 3*x), -2),
    "lim h→0  ((3 + h)² − 9)/h":            (lambda h: ((3 + h)**2 - 9) / h, 0),
    "lim x→2  (x² + x − 6)/(x − 2)":        (lambda x: (x**2 + x - 6) / (x - 2), 2),
    "lim x→−3 (x² + 3x)/(x² − x − 12)":     (lambda x: (x**2 + 3*x) / (x**2 - x - 12), -3),
}
for nome, (f, a) in exemplos.items():
    print(f"{nome:<36} ≈ {lim_numerico(f, a)}")
print("valores exatos: 39, −1/11 ≈", round(-1/11, 4), ", 6, 5, 3/7 ≈", round(3/7, 4))
