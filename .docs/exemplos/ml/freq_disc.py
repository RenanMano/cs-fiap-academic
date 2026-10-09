from collections import Counter
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)   # o material usa None (largura do terminal)

dados = [14]*6 + [15]*12 + [16]*9 + [17]*3

fi = pd.Series(Counter(dados)).sort_index()
fia = fi.cumsum()
fr = 100 * fi / fi.sum()
fra = fr.cumsum()

tabela = pd.DataFrame({
    'Frequencia_Absoluta': fi,
    'Frequencia_Absoluta_Acumulada': fia,
    'Frequencia_Relativa': fr,
    'Frequencia_Relativa_Acumulada': fra
})
total_row = pd.Series({
    'Frequencia_Absoluta': fi.sum(),
    'Frequencia_Absoluta_Acumulada': '',
    'Frequencia_Relativa': fr.sum(),
    'Frequencia_Relativa_Acumulada': ''
}, name='Total')
tabela = pd.concat([tabela, total_row.to_frame().T])
print(tabela)
