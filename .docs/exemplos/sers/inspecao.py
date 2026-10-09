# Inspeção inicial (head, shape, info, describe) com as 5 primeiras linhas de SAMPLE_ENERGY_DATA.csv
import io
import pandas as pd
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

csv = """Date,Time,Global_active_power,Global_reactive_power,Voltage,Global_intensity,Sub_metering_1,Sub_metering_2,Sub_metering_3
2008-12-01 00:00:00,2026-08-03 09:44:00,1.502,0.074,240.17,6.4,0,0,18
2006-12-17 00:00:00,2026-08-03 23:39:00,0.374,0.264,245.5,1.8,0,2,0
2009-06-03 00:00:00,2026-08-03 17:01:00,0.62,0.3,239.85,3,0,1,1
2007-05-09 00:00:00,2026-08-03 05:53:00,0.28,0.2,235.72,1.4,0,0,0
2008-12-14 00:00:00,2026-08-03 02:57:00,1.372,0.054,243.95,5.6,0,0,18
"""
dados = pd.read_csv(io.StringIO(csv))       # no notebook: pd.read_csv('/content/SAMPLE_ENERGY_DATA.csv')
print(dados.shape)
numericas = dados.select_dtypes("number").columns
print("colunas numéricas:", len(numericas), "| de texto (Date e Time):", len(dados.columns) - len(numericas))
print(dados[["Global_active_power", "Voltage", "Global_intensity"]].describe().round(3))
