# Limites do boxplot a partir do resumo de 5 números de Age publicado no material (Titanic)
minimo, q1, mediana, q3, maximo = 0.42, 20, 28, 38, 80
iqr = q3 - q1
lim_inf, lim_sup = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print(f"IQR = {iqr} anos | limites: [{lim_inf}, {lim_sup}]")
print("mínimo é outlier?", minimo < lim_inf, "| máximo é outlier?", maximo > lim_sup)
print("Os bigodes vão até o valor mais extremo DENTRO dos limites; o 80 aparece como ponto isolado.")
