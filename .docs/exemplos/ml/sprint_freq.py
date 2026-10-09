# Tabelas de frequência do material (Titanic, train.csv) reconstruídas a partir das contagens publicadas
import pandas as pd
pd.set_option("display.width", 200)

def tabela(fi):
    t = pd.DataFrame({"fi": fi})
    t["fri (%)"] = (t["fi"] / t["fi"].sum() * 100).round(2)
    t["Fi"] = t["fi"].cumsum()
    t["Fri (%)"] = (t["Fi"] / t["fi"].sum() * 100).round(2)   # evita somar arredondamentos
    return t

# Variável categórica ordinal: Pclass (891 passageiros)
pclass = pd.Series([1] * 216 + [2] * 184 + [3] * 491)
print(tabela(pclass.value_counts().sort_index()))
print()

# Variável contínua agrupada em faixas: Age (714 idades registradas; 177 ausentes)
faixas = pd.Series({"Criança (0-12]": 69, "Adolescente (12-18]": 55, "Adulto jovem (18-35]": 306,
                    "Adulto (35-60]": 249, "Idoso (60-100]": 35})
t = tabela(faixas)
print(t)
print("total:", t["fi"].sum(), "| ausentes:", 891 - t["fi"].sum())
