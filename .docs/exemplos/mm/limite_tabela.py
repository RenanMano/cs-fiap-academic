def f(x):
    return (x**2 - 1) / (x - 1)       # não definida em x = 1

for h in (0.1, 0.01, 0.001, 0.0001):
    print(f"x = {1 - h:<7} f(x) = {f(1 - h):.4f}    |    x = {1 + h:<7} f(x) = {f(1 + h):.4f}")

# após simplificar, (x² − 1)/(x − 1) = x + 1, e a substituição direta dá o limite
print("limite por substituição em x + 1:", 1 + 1)
