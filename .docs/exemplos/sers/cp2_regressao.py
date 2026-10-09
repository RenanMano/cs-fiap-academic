import numpy as np
import pandas as pd

df = pd.read_csv("Data_for_UCI_named.csv")
y = df["stab"]

# Modelo 1: as cinco maiores correlações absolutas com stab
corr = df.corr(numeric_only=True)["stab"].drop("stab")
top5 = corr.abs().sort_values(ascending=False).index[:5].tolist()
# Modelo 2: todas as colunas que começam com tau ou g
tau_g = [c for c in df.columns if c.startswith(("tau", "g"))]

# Mesma divisão de train_test_split(test_size=0.2, random_state=42)
perm = np.random.RandomState(42).permutation(len(df))
teste, treino = perm[:2000], perm[2000:]

def avaliar(colunas):
    X = np.column_stack([np.ones(len(df)), df[colunas].to_numpy()])   # intercepto + variáveis
    beta, *_ = np.linalg.lstsq(X[treino], y.to_numpy()[treino], rcond=None)
    real, prev = y.to_numpy()[teste], X[teste] @ beta
    mse = np.mean((real - prev) ** 2)
    mae = np.mean(np.abs(real - prev))
    r2 = 1 - np.sum((real - prev) ** 2) / np.sum((real - real.mean()) ** 2)
    return r2, mae, mse

print("Top 5:", top5)
print("tau/g:", tau_g)
linhas = [("Modelo 1", *avaliar(top5)), ("Modelo 2", *avaliar(tau_g))]
print(pd.DataFrame(linhas, columns=["Modelo", "R²", "MAE", "MSE"]).round(6).to_string(index=False))
