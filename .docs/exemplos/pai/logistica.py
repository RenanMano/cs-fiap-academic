# Regressão logística treinada por gradiente descendente (dados de churn dos slides da aula 01)
import math

# (compras em 3 meses, valor gasto em 3 meses em R$, churn: 1 = sim, 0 = não)
dados = [(45, 30, 0), (122, 150, 0), (1, 47, 1), (7, 200, 1),
         (10, 50, 0), (20, 100, 0), (1, 50, 1)]

def sigmoide(z):
    return 1 / (1 + math.exp(-z))

def prever(w, x1, x2):
    return sigmoide(w[0] + w[1] * x1 / 100 + w[2] * x2 / 100)   # escala /100 ajuda a convergir

w = [0.0, 0.0, 0.0]
taxa = 0.5
for epoca in range(1, 5001):
    grad = [0.0, 0.0, 0.0]
    perda = 0.0
    for x1, x2, y in dados:
        p = prever(w, x1, x2)
        erro = p - y                       # derivada da log-loss em relação a z
        grad[0] += erro
        grad[1] += erro * x1 / 100
        grad[2] += erro * x2 / 100
        perda -= y * math.log(p) + (1 - y) * math.log(1 - p)
    w = [wi - taxa * gi / len(dados) for wi, gi in zip(w, grad)]  # um passo "morro abaixo"
    if epoca in (1, 100, 1000, 5000):
        print(f"época {epoca:4d}: perda média = {perda / len(dados):.4f}")

for x1, x2, y in dados:
    p = prever(w, x1, x2)
    print(f"compras={x1:3d} valor={x2:3d} -> p(churn)={p:.2f} previsto={'Sim' if p >= 0.5 else 'Não'} real={'Sim' if y else 'Não'}")
