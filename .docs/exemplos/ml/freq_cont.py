import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)   # o material usa None (largura do terminal)

dados = [
    48, 48.2, 48.7, 49.1, 49.5, 49.8, 50.2, 50.3, 50.4, 50.6, 50.9, 50.6,
    50.8, 50.4, 50.6, 51.2, 51.3, 51.2, 51.9, 51.8, 51.6, 52.8, 52.6, 52.8,
    53, 53, 53, 53, 53, 53
]
bins = [48, 49, 50, 51, 52, 53, 54]
classes = pd.cut(dados, bins=bins, right=False)

fi = classes.value_counts().sort_index()
fia = fi.cumsum()
fr = (100 * fi / fi.sum()).round(2)
fra = fr.cumsum()

total = pd.Series({
    'Frequencia_Absoluta': fi.sum(),
    'Frequencia_Absoluta_Acumulada': pd.NA,
    'Frequencia_Relativa': fr.sum().round(2),
    'Frequencia_Relativa_Acumulada': pd.NA
}, name='Total')
tabela = pd.DataFrame({
    'Frequencia_Absoluta': fi,
    'Frequencia_Absoluta_Acumulada': fia,
    'Frequencia_Relativa': fr,
    'Frequencia_Relativa_Acumulada': fra
})
tabela = pd.concat([tabela, total.to_frame().T])
print(tabela)
