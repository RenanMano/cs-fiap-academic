import math

def tabela(f, xs):
    return [round(f(x), 6) for x in xs]

grandes = [10, 1_000, 1_000_000]
print("1/x                    ->", tabela(lambda x: 1 / x, grandes))
print("(x² − 1)/(x² + 1)      ->", tabela(lambda x: (x*x - 1) / (x*x + 1), [1, 10, 50, 100, 10_000]))
print("(3x + 5)/(x − 4)       ->", tabela(lambda x: (3*x + 5) / (x - 4), grandes))
print("(1 − x − x²)/(2x² − 7) ->", tabela(lambda x: (1 - x - x*x) / (2*x*x - 7), [-10, -1_000, -1_000_000]))
print("e^x                    ->", [f"{math.exp(x):.3g}" for x in (1, 10, 100)])

# limites infinitos: lados de x = 2 em 1/(x − 2) e x/(x − 2) (ex. 40, p. 80)
for h in (0.1, 0.001):
    print(f"x = 2 ± {h}: 1/(x−2) = {1 / h:+.0f} e {-1 / h:+.0f}   x/(x−2) à esquerda = {(2 - h) / (-h):+.1f}")
