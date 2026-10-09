from statistics import NormalDist      # biblioteca padrão; equivalente a scipy.stats.norm

alturas = NormalDist(mu=175, sigma=10)

a = alturas.cdf(164)                    # norm.cdf(164, 175, 10)
b = 1 - alturas.cdf(164)                # norm.sf(164, 175, 10)
c = alturas.cdf(174) - alturas.cdf(164)
print(f"a) P(X <= 164)       = {a:.4f}")
print(f"b) P(X >= 164)       = {b:.4f}")
print(f"c) P(164 <= X <= 174) = {c:.4f}")

# padronização: Z = (x - μ) / σ leva ao mesmo resultado
z = (164 - 175) / 10
print(f"z = {z}  ->  Φ(z) = {NormalDist().cdf(z):.4f}")

# quantil (inversa da acumulada), como norm.ppf: tempo de produção N(120, 15)
lote = NormalDist(120, 15)
print(f"95% dos lotes em até {lote.inv_cdf(0.95):.2f} min")
print(f"80% centrais entre {lote.inv_cdf(0.10):.2f} e {lote.inv_cdf(0.90):.2f} min")
