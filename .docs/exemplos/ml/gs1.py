import pandas as pd
pd.set_option("display.width", 200)

# tempo de deslocamento (min) de 20 alunos até a faculdade — dados ilustrativos
tempos = pd.Series([12, 25, 30, 18, 45, 22, 35, 28, 15, 40,
                    33, 27, 20, 38, 24, 31, 19, 26, 90, 29])

# 1) tabela de frequências em classes de 10 min, a partir de 10
classes = pd.cut(tempos, bins=range(10, 101, 10), right=False)
fi = classes.value_counts().sort_index()
tabela = pd.DataFrame({"fi": fi, "fia": fi.cumsum(),
                       "fr (%)": 100 * fi / fi.sum(), "fra (%)": (100 * fi / fi.sum()).cumsum()})
print(tabela[tabela["fi"] > 0])

# 2) medidas
q1, q2, q3 = tempos.quantile([0.25, 0.5, 0.75])
cv = tempos.std() / tempos.mean() * 100
print(f"média {tempos.mean():.2f} | mediana {q2} | desvio {tempos.std():.2f} | CV {cv:.1f}%")
iqr = q3 - q1
print(f"Q1 {q1} | Q3 {q3} | LI {q1 - 1.5 * iqr} | LS {q3 + 1.5 * iqr}")
print("outliers:", list(tempos[(tempos < q1 - 1.5 * iqr) | (tempos > q3 + 1.5 * iqr)]))
