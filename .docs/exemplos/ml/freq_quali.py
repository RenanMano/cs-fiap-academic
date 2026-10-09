import pandas as pd

esportes = ["Futebol"] * 2 + ["Volei"] * 3 + ["Basquete"] * 7

fi = pd.Series(esportes).value_counts(sort=False)
fr = (100 * fi / fi.sum()).round(2)

tabela = pd.DataFrame({"fi": fi, "fr (%)": fr})
tabela.loc["Total"] = [fi.sum(), fr.sum()]
tabela["fi"] = tabela["fi"].astype(int)
print(tabela)
