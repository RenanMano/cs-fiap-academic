# Estimador paramétrico: renda ≈ β0 + β1·escolaridade + β2·idade (mínimos quadrados)
import numpy as np

# dados fictícios: anos de estudo, idade, renda (R$ mil/mês)
escolaridade = np.array([8, 10, 11, 12, 12, 14, 15, 16, 16, 18, 20, 21])
idade        = np.array([25, 30, 22, 35, 41, 28, 45, 33, 50, 38, 42, 55])
renda        = np.array([1.9, 2.6, 2.2, 3.4, 3.9, 3.6, 5.0, 4.6, 5.9, 5.8, 6.9, 8.1])

X = np.column_stack([np.ones(len(renda)), escolaridade, idade])  # coluna de 1 para β0
beta, *_ = np.linalg.lstsq(X, renda, rcond=None)                  # minimiza o MSE
pred = X @ beta
mse = np.mean((renda - pred) ** 2)

print("β0, β1, β2 =", np.round(beta, 3))
print(f"MSE de treino = {mse:.4f}")
print(f"Previsão (16 anos de estudo, 30 anos de idade): {beta @ [1, 16, 30]:.2f}")
