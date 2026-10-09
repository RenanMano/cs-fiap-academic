import numpy as np

A = np.array([[1, 2, 3]])                       # 1×3
B = np.array([[-1], [1], [2]])                  # 3×1
C = np.array([[1, 2], [0, -1], [1, 0]])         # 3×2
print("AB =", A @ B, "| AC =", A @ C)
try:
    C @ A                                       # (3×2)(1×3): colunas de C ≠ linhas de A
except ValueError:
    print("CA: multiplicação impossível (3×2 por 1×3)")

Q = np.array([[1, 2, 3], [-1, 0, 1]])
P = np.array([[1, -1, 1], [2, 0, 1], [0, 4, -1]])
print("QP =\n", Q @ P)
print("PI = P?", np.array_equal(P @ np.eye(3, dtype=int), P))
print("transposta de [[1, 2], [3, 4]] =", np.array([[1, 2], [3, 4]]).T.tolist())
