import numpy as np

def classificar(A, b):
    """Teorema de Rouché-Capelli: compara posto(A), posto([A|b]) e nº de variáveis."""
    pa = np.linalg.matrix_rank(A)
    pab = np.linalg.matrix_rank(np.hstack((A, b)))
    n = A.shape[1]
    if pa < pab:
        return "SI"
    return "SPD" if pa == n else "SPI"

casos = {
    "célula 2  (SPD)": (np.array([[1, 1, 1], [1, -1, 1], [2, 1, -1]]), np.array([[6], [2], [7]])),
    "célula 17 (SPD)": (np.array([[1, 1, 1], [2, -1, 1], [1, 2, -1]]), np.array([[6], [2], [7]])),
    "célula 19 (SPI)": (np.array([[1, 1, 1], [2, 2, 2]]), np.array([[2], [4]])),
    "célula 26 (SI)":  (np.array([[1, 1, 1], [2, 2, 2]]), np.array([[2], [5]])),
}
for nome, (A, b) in casos.items():
    print(f"{nome}: {classificar(A, b)}")

print("solução célula 7 :", np.linalg.solve(*casos["célula 2  (SPD)"]).ravel())
print("solução célula 17:", np.linalg.solve(*casos["célula 17 (SPD)"]).ravel().round(6))

A = np.array([[2, 1], [3, 4]])
B = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
print("det(A) =", round(np.linalg.det(A), 6), "| det(B) =", round(np.linalg.det(B), 6))
print("A⁻¹ =", np.linalg.inv(A).round(4).tolist())
print("A·A⁻¹ = I?", np.allclose(A @ np.linalg.inv(A), np.eye(2)))
print("x = A⁻¹b =", np.linalg.inv(A) @ np.array([5, 6]), "| solve:", np.linalg.solve(A, [5, 6]))

for rotulo, acao in [("det de matriz 3×1", lambda: np.linalg.det(np.array([[6], [2], [7]]))),
                     ("inversa de [[2, 2], [3, 3]]", lambda: np.linalg.inv(np.array([[2, 2], [3, 3]]))),
                     ("solve com [[2, 2], [4, 4]]", lambda: np.linalg.solve(np.array([[2, 2], [4, 4]]), [2, 5]))]:
    try:
        acao()
    except np.linalg.LinAlgError as erro:
        print(f"{rotulo}: LinAlgError — {erro}")
