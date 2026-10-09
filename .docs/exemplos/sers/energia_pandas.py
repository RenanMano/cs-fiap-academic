# Mesmas operações dos notebooks de 03/08 e 10/08, com 6 linhas no formato de SAMPLE_ENERGY_DATA.csv
import pandas as pd
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

dados = pd.DataFrame({
    "Date": ["2008-12-01", "2006-12-17", "2009-06-03", "2007-05-09", "2008-12-14", "2009-02-02"],
    "Time": ["09:44:00", "23:39:00", "17:01:00", "05:53:00", "02:57:00", "19:30:00"],
    "Global_active_power": [1.502, 0.374, 0.620, 0.280, 1.372, 8.540],
    "Global_reactive_power": [0.074, 0.264, 0.300, 0.200, 0.054, 0.238],
    "Voltage": [240.17, 245.50, 239.85, 235.72, 243.95, 236.23],
    "Global_intensity": [6.4, 1.8, 3.0, 1.4, 5.6, 36.0],
    "Sub_metering_1": [0, 0, 0, 0, 0, 38],
    "Sub_metering_2": [0, 2, 1, 0, 0, 1],
    "Sub_metering_3": [18, 0, 1, 0, 18, 17],
})
print(dados.shape, "| linhas:", dados.shape[0])

dados = dados.rename(columns={"Date": "Data", "Time": "Hora", "Global_active_power": "Potencia_Ativa",
                              "Global_reactive_power": "Potencia_Reativa", "Voltage": "Tensao",
                              "Global_intensity": "Corrente", "Sub_metering_1": "Consumo_1",
                              "Sub_metering_2": "Consumo_2", "Sub_metering_3": "Consumo_3"})
df1 = dados.drop(columns=["Data", "Hora"])          # remove colunas
df2 = dados[["Tensao", "Corrente"]]                 # seleciona colunas (DataFrame)
tensao = dados["Tensao"]                            # uma coluna (Series)
df3 = dados.iloc[:, 0:4]                            # 4 primeiras colunas por posição
print(type(df2).__name__, type(tensao).__name__, list(df1.columns)[:3], list(df3.columns))

PMAX = dados["Potencia_Ativa"].max()
P70 = 0.7 * PMAX
df4 = dados[["Tensao", "Corrente", "Potencia_Ativa", "Potencia_Reativa"]]
df5 = df4[df4["Potencia_Ativa"] > P70]
print(f"PMAX = {PMAX:.2f} kW | P70 = {P70:.2f} kW | registros acima: {df5.shape[0]}")
print(df5)
