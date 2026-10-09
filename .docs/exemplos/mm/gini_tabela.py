import numpy as np

pop = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0])      # população acumulada (Tabela 1)
renda = np.array([0, 0.03, 0.10, 0.22, 0.42, 1.0])  # renda acumulada

area_lorenz = np.trapezoid(renda, pop)              # área sob a poligonal de Lorenz
print(f"área sob a curva (trapézios) = {area_lorenz:.3f}")
print(f"Gini direto dos dados = 1 − 2·área = {1 - 2 * area_lorenz:.3f}")
print(f"ajuste do material em x = 1: L(1) = {0.7604 * 1 ** 2.0926}  (uma curva de Lorenz deveria valer 1)")
