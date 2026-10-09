# Executado na pasta da aula 06, onde está SAMPLE_ENERGY_DATA.csv (40.986 registros)
import pandas as pd

dados = pd.read_csv("SAMPLE_ENERGY_DATA.csv")
print("Datas distintas na coluna Time:", list(dados["Time"].str[:10].unique()))
print("Período em Date:", dados["Date"].min()[:10], "a", dados["Date"].max()[:10])
print("Valores ausentes:", int(dados.isnull().sum().sum()))

PMAX = dados["Global_active_power"].max()
alto = dados[dados["Global_active_power"] > 0.7 * PMAX]
print(f"Acima de 70% de PMAX: {len(alto)} registros = {len(alto) / len(dados):.3%} da amostra")

P, Q = dados["Global_active_power"], dados["Global_reactive_power"]
FP = P / (P ** 2 + Q ** 2) ** 0.5                   # cos φ = P / S, com S = √(P² + Q²)
print(f"Fator de potência estimado: mediana = {FP.median():.3f}, mínimo = {FP.min():.3f}")
