# Itens 3 a 7 da Etapa B do Dataset 1 (Appliances) — solução proposta para estudo, com 8 linhas fictícias
import pandas as pd
pd.set_option("display.width", 200)

df1 = pd.DataFrame({
    "Appliances": [40, 90, 50, 770, 60, 560, 600, 100],
    "lights": [0, 10, 0, 30, 0, 20, 0, 0],
    "T1": [20.89, 21.89, 21.39, 23.50, 19.96, 21.10, 22.60, 21.60],
    "RH_1": [35.40, 53.10, 35.50, 44.20, 35.13, 40.00, 41.00, 39.60],
})
df1 = df1.rename(columns={"Appliances": "Consumo_Eletrodomesticos", "T1": "Temperatura_1", "RH_1": "Umidade_1"})

maximo = df1["Consumo_Eletrodomesticos"].max()                          # item 3
limiar = 0.70 * maximo                                                  # item 4
alto = df1[df1["Consumo_Eletrodomesticos"] > limiar]
pct = len(alto) / len(df1) * 100                                        # item 5
print(f"Máximo = {maximo} Wh | limiar 70% = {limiar:.1f} Wh | {len(alto)} registros ({pct:.1f}%)")

t_media = df1["Temperatura_1"].mean()                                   # item 6
alto_quente = df1[(df1["Consumo_Eletrodomesticos"] > limiar) & (df1["Temperatura_1"] > t_media)]
print(f"T1 média = {t_media:.2f} °C | consumo alto E T1 acima da média: {len(alto_quente)} registros")
print(alto_quente)                                                      # item 7: compare com 'alto'
