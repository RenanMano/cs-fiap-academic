def preco(km):                      # P = 4,10 + 2,30·x (Lista 1, exercício 1)
    return 4.10 + 2.30 * km

print([round(preco(x), 2) for x in (0, 0.5, 1.0, 1.5, 2.0)])
km = (22.10 - 4.10) / 2.30          # função inversa: x = (P − 4,10) / 2,30
print(f"R$ 22,10 -> {km:.4f} km")

def analisar(a, b, c):
    """Concavidade, raízes reais, intercepto em y e vértice de y = ax² + bx + c."""
    delta = b * b - 4 * a * c
    raizes = sorted({(-b - delta ** 0.5) / (2 * a), (-b + delta ** 0.5) / (2 * a)}) if delta >= 0 else []
    xv, yv = -b / (2 * a), -delta / (4 * a) + 0.0   # + 0.0 evita exibir "-0.0"
    tipo = "mínimo" if a > 0 else "máximo"
    return ("p/ cima" if a > 0 else "p/ baixo", raizes, c, (xv, yv), tipo)

for rotulo, coef in {"a": (1, -2, 1), "b": (-1, 3, -3), "c": (1, -3, 4), "d": (-1, 10, -25)}.items():
    print(rotulo, analisar(*coef))
