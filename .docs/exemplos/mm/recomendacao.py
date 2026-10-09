import numpy as np

# avaliações (0 a 5) dos filmes F1, F2, F3 — vetores reduzidos da atividade
u = {"U1": [5, 1, 4], "U2": [4, 1, 5], "U3": [1, 5, 2], "U4": [1, 4, 1]}
u5 = np.array([4, 2, 3])

for nome, vet in u.items():
    v = np.array(vet)
    escalar = u5 @ v
    cosseno = escalar / (np.linalg.norm(u5) * np.linalg.norm(v))
    print(f"u5 · {nome.lower()} = {escalar:>2}   |   cosseno = {cosseno:.3f}")

# limitação do produto escalar: depende da escala das notas, não só do gosto
exigente = np.array([2, 1, 1.5])        # mesmas proporções de u5, mas notas baixas
print("u5 · (2, 1, 1.5) =", u5 @ exigente, "← parece pouco parecido")
print("cosseno          =", round(float(u5 @ exigente / (np.linalg.norm(u5) * np.linalg.norm(exigente))), 3), "← mesmo gosto")
