from fractions import Fraction as Fr

def escalonar(M):
    """Eliminação de Gauss com retrossubstituição, imprimindo cada operação."""
    M = [[Fr(x) for x in linha] for linha in M]
    n = len(M)
    for i in range(n):
        if M[i][i] == 0:                                       # troca de linhas
            k = next(k for k in range(i + 1, n) if M[k][i] != 0)
            M[i], M[k] = M[k], M[i]
            print(f"L{i+1} ↔ L{k+1}")
        for k in range(i + 1, n):
            fator = M[k][i] / M[i][i]
            M[k] = [a - fator * b for a, b in zip(M[k], M[i])]
            print(f"L{k+1} ← L{k+1} − ({fator})·L{i+1}:", [str(x) for x in M[k]])
    x = [Fr(0)] * n
    for i in reversed(range(n)):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return [str(v) for v in x]

print("2x + y = 1, −x − y = 4  →", escalonar([[2, 1, 1], [-1, -1, 4]]))
print("2x + y = 7,  x + y = 5  →", escalonar([[2, 1, 7], [1, 1, 5]]))
