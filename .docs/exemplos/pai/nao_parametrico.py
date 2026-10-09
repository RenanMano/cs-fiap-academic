# Estimador não paramétrico: k vizinhos mais próximos (k-NN), sem supor a forma de f
import numpy as np

escolaridade = np.array([8, 10, 11, 12, 12, 14, 15, 16, 16, 18, 20, 21])
renda        = np.array([1.9, 2.6, 2.2, 3.4, 3.9, 3.6, 5.0, 4.6, 5.9, 5.8, 6.9, 8.1])

def knn(x, k):
    distancias = np.abs(escolaridade - x)
    vizinhos = np.argsort(distancias, kind="stable")[:k]   # índices dos k mais próximos
    return renda[vizinhos].mean()

for k in (1, 3, 12):
    pred = np.array([knn(x, k) for x in escolaridade])
    mse = np.mean((renda - pred) ** 2)
    print(f"k = {k:2d}: MSE de treino = {mse:.4f} | previsão para 17 anos = {knn(17, k):.2f}")
