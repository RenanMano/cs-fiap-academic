# R², MAE e MSE calculados à mão para um conjunto pequeno de previsões de stab
real = [0.055, -0.006, 0.003, 0.029, 0.050]
prev = [0.040, 0.004, 0.010, 0.020, 0.035]

n = len(real)
erros = [r - p for r, p in zip(real, prev)]
mae = sum(abs(e) for e in erros) / n
mse = sum(e ** 2 for e in erros) / n
media = sum(real) / n
r2 = 1 - sum(e ** 2 for e in erros) / sum((r - media) ** 2 for r in real)
print(f"MAE = {mae:.4f}")
print(f"MSE = {mse:.6f}")
print(f"R²  = {r2:.4f}")
