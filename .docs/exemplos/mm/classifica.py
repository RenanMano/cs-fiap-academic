import numpy as np

def classificar(A, b):
    A, b = np.array(A, float), np.array(b, float).reshape(-1, 1)
    pa, pab, n = np.linalg.matrix_rank(A), np.linalg.matrix_rank(np.hstack([A, b])), A.shape[1]
    if pa < pab:
        return f"posto(A) = {pa} < posto([A|b]) = {pab}: SI (impossível)"
    return f"pivôs = {pa}, variáveis = {n}: " + ("SPD (única solução)" if pa == n else "SPI (infinitas soluções)")

print("Ex. 1  (3 eq., 2 var.):", classificar([[1, 1], [1, -1], [2, 0]], [2, 0, 2]))
print("Exerc. 1 (3 eq., 3 var.):", classificar([[1, 1, 1], [1, -1, 1], [2, 1, -1]], [6, 2, 7]))
print("Ex. 2  (2 eq., 3 var.):", classificar([[1, 1, 1], [1, -1, 1]], [1, 2]))
print("Exerc. 2 (4 eq., 3 var.):", classificar([[1, 1, 1], [1, -1, 1], [2, 0, 2], [3, -1, 3]], [6, 2, 8, 10]))
print("Notebook aula 14 (SI?):", classificar([[1, 1, 1], [2, 2, 2]], [2, 5]))
print("solução do exercício 1:", np.linalg.solve([[1, 1, 1], [1, -1, 1], [2, 1, -1]], [6, 2, 7]))
