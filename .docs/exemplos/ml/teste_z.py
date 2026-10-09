from math import sqrt
from statistics import NormalDist

Z = NormalDist()      # normal padrão; Z.inv_cdf equivale a norm.ppf

def teste_z(zc, alfa, h1):
    """h1: 'menor' (unilateral à esquerda), 'maior' (à direita) ou 'diferente' (bilateral)."""
    if h1 == "menor":
        critico, rejeita = Z.inv_cdf(alfa), zc < Z.inv_cdf(alfa)
        p = Z.cdf(zc)
    elif h1 == "maior":
        critico, rejeita = Z.inv_cdf(1 - alfa), zc > Z.inv_cdf(1 - alfa)
        p = 1 - Z.cdf(zc)
    else:
        critico, rejeita = Z.inv_cdf(alfa / 2), abs(zc) > -Z.inv_cdf(alfa / 2)
        p = 2 * (1 - Z.cdf(abs(zc)))
    decisao = "Rejeita H0" if rejeita else "Não rejeita H0"
    return f"Zc = {zc:7.4f} | crítico = {critico:7.4f} | p-valor = {p:.4f} | {decisao}"

# uma média: Zc = (x̄ - μ0) / (σ / √n)
print("Tijolos   ", teste_z((195 - 200) / (10 / sqrt(100)), 0.05, "menor"))
print("Zebras    ", teste_z((395 - 400) / (20 / sqrt(100)), 0.05, "diferente"))
print("Contadores", teste_z((43500 - 45000) / (5200 / sqrt(30)), 0.05, "menor"))
zc = (9.1 - 8) / (2 / sqrt(10))
print("Reação 6% ", teste_z(zc, 0.06, "diferente"))
print("Reação 10%", teste_z(zc, 0.10, "diferente"))

# diferença de médias: Zc = (x̄1 - x̄2 - d0) / √(σ1²/n1 + σ2²/n2)
print("Laminados ", teste_z((55 - 53) / sqrt(7.5 / 5 + 5 / 5), 0.05, "diferente"))
print("Zarcão    ", teste_z((121 - 112) / sqrt(8**2 / 10 + 8**2 / 10), 0.05, "maior"))
print("Trajetos  ", teste_z((57 - 54) / sqrt(8**2 / 45 + 6**2 / 30), 0.01, "diferente"))
