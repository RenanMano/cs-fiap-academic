import numpy as np
import pandas as pd

dados2 = [15, 17, 15, 15, 17, 14, 18, 15, 15, 17, 15, 12, 15, 15, 18]

contagens, limites = np.histogram(dados2, bins=3)   # mesma divisão de plt.hist(bins=3)
for i, (a, b, c) in enumerate(zip(limites[:-1], limites[1:], contagens)):
    fecha = "]" if i == len(contagens) - 1 else ")"    # a última classe inclui o máximo
    print(f"[{a:.0f}, {b:.0f}{fecha} -> {c} {'#' * c}")

print(pd.Series(dados2).describe()[["min", "25%", "50%", "75%", "max"]].to_dict())
