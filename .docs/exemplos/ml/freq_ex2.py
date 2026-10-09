from collections import Counter
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)   # o material usa None (largura do terminal)

dados2 = [1]*2 + [2]*5 + [3]*2 + [4]*2 + [5]*5 + [6]*4

fi = pd.Series(Counter(dados2)).sort_index()
fia = fi.cumsum()
fr = 100 * fi / fi.sum()
fra = fr.cumsum()

tabela = pd.DataFrame({
    'Frequencia_Absoluta': fi,
    'Frequencia_Absoluta_Acumulada': fia,
    'Frequencia_Relativa (%)': fr.round(1),
    'Frequencia_Relativa_Acumulada (%)': fra.round(1)
})
total_row = pd.Series({
    'Frequencia_Absoluta': fi.sum(),
    'Frequencia_Absoluta_Acumulada': pd.NA,
    'Frequencia_Relativa (%)': fr.sum().round(1),
    'Frequencia_Relativa_Acumulada (%)': pd.NA
}, name='Total')
tabela = pd.concat([tabela, total_row.to_frame().T])
print(tabela)
