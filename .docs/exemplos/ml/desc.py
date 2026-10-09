import pandas as pd

x = pd.Series([2, 4, 3, 4, 5, 2, 4])

print("média    :", round(x.mean(), 4))
print("mediana  :", x.median())
print("moda     :", list(x.mode()))
print("mín, máx :", x.min(), x.max(), "| amplitude:", x.max() - x.min())
print("variância:", round(x.var(), 4))
print("desvio   :", round(x.std(), 4))
print("CV (%)   :", round(x.std() / x.mean() * 100, 2))
q = x.quantile([0.25, 0.50, 0.75])
print("quartis  :", list(q))
aiq = q[0.75] - q[0.25]
print("LI, LS   :", q[0.25] - 1.5 * aiq, q[0.75] + 1.5 * aiq)
