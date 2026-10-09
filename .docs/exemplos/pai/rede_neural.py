# Tentar → errar → corrigir: modelo linear × rede neural com 1 camada oculta (NumPy)
import numpy as np

rng = np.random.default_rng(7)
# Dados sintéticos: 2 atributos padronizados (compras e valor gasto); "churn" = 1 longe do centro
X = rng.normal(0, 1, size=(400, 2))
y = ((X ** 2).sum(axis=1) > 1.4).astype(float).reshape(-1, 1)   # fronteira circular (não linear)

def sigmoide(z):
    return 1 / (1 + np.exp(-z))

def treinar(ocultos, epocas=3000, taxa=0.5):
    r = np.random.default_rng(1)
    if ocultos == 0:                                    # modelo linear (regressão logística)
        W = [r.normal(0, 0.5, (2, 1))]; b = [np.zeros((1, 1))]
    else:
        W = [r.normal(0, 0.5, (2, ocultos)), r.normal(0, 0.5, (ocultos, 1))]
        b = [np.zeros((1, ocultos)), np.zeros((1, 1))]
    for epoca in range(1, epocas + 1):
        # feedforward (tentar)
        ativ = [X]
        for k in range(len(W)):
            z = ativ[-1] @ W[k] + b[k]
            ativ.append(sigmoide(z) if k == len(W) - 1 else np.tanh(z))
        p = ativ[-1]
        perda = -np.mean(y * np.log(p + 1e-12) + (1 - y) * np.log(1 - p + 1e-12))  # errar
        # backward (corrigir): gradiente da perda, camada por camada
        delta = (p - y) / len(X)
        for k in reversed(range(len(W))):
            gW, gb = ativ[k].T @ delta, delta.sum(axis=0, keepdims=True)
            if k > 0:
                delta = (delta @ W[k].T) * (1 - ativ[k] ** 2)            # derivada da tanh
            W[k] -= taxa * gW
            b[k] -= taxa * gb
        if epoca in (1, 300, 3000):
            acc = np.mean((p >= 0.5) == y)
            print(f"  época {epoca:4d}: perda = {perda:.3f}  acurácia = {acc:.1%}")

print(f"proporção de churn nos dados: {y.mean():.1%}")
print("Modelo linear (sem camada oculta):")
treinar(0)
print("Rede neural (8 neurônios ocultos):")
treinar(8)
