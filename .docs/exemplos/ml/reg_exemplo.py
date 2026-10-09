from math import lgamma, exp, log, sqrt

def beta_reg(a, b, x, it=200):
    """Função beta incompleta regularizada I_x(a, b), por frações contínuas (Lentz)."""
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    if x > (a + 1) / (a + b + 2):
        return 1 - beta_reg(b, a, 1 - x, it)
    frente = exp(lgamma(a + b) - lgamma(a) - lgamma(b) + a * log(x) + b * log(1 - x)) / a
    f, c, d = 1.0, 1.0, 0.0
    for i in range(it * 2 + 1):
        m = i // 2
        if i == 0: num = 1.0
        elif i % 2 == 0: num = m * (b - m) * x / ((a + 2 * m - 1) * (a + 2 * m))
        else: num = -(a + m) * (a + b + m) * x / ((a + 2 * m) * (a + 2 * m + 1))
        d = 1 + num * d; d = 1 / (d if abs(d) > 1e-30 else 1e-30)
        c = 1 + num / c if abs(c) > 1e-30 else 1 + num / 1e-30
        f *= c * d
        if abs(c * d - 1) < 1e-15: break
    return frente * (f - 1)

def p_valor_F(F, gl1, gl2):
    """P(F(gl1, gl2) > F)."""
    return beta_reg(gl2 / 2, gl1 / 2, gl2 / (gl2 + gl1 * F))

def regressao_simples(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    beta = sxy / sxx                       # coeficiente angular (inclinação)
    alfa = my - beta * mx                  # coeficiente linear (intercepto)
    sqr = sum((b - (alfa + beta * a)) ** 2 for a, b in zip(x, y))   # soma dos quadrados dos resíduos
    r2 = 1 - sqr / syy
    r2_aj = 1 - (1 - r2) * (n - 1) / (n - 1 - 1)
    F = (syy - sqr) / 1 / (sqr / (n - 2))
    return dict(cov=sxy / (n - 1), r=sxy / sqrt(sxx * syy), alfa=alfa, beta=beta,
                r2=r2, r2_aj=r2_aj, F=F, p=p_valor_F(F, 1, n - 2))


# exemplo dos slides: poluente (µg/L) x dano ecológico
x = [1, 2, 3, 4, 5, 6]
y = [3, 6, 7, 10, 10, 12]
m = regressao_simples(x, y)
print(f"covariância amostral = {m['cov']:.4f}")
print(f"correlação de Pearson r = {m['r']:.4f}")
print(f"equação: Ŷ = {m['alfa']:.4f} + {m['beta']:.4f}·X")
print(f"R² = {m['r2']:.4f} | R² ajustado = {m['r2_aj']:.4f}")
print(f"F = {m['F']:.2f} | p-valor = {m['p']:.6f}")
print(f"previsão para 9 µg/L: {m['alfa'] + m['beta'] * 9:.4f}")
