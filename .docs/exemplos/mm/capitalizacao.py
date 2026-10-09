import math

br = lambda v: f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")   # formato brasileiro

C, i = 100_000, 0.10                                      # capital e taxa anual (1 ano)
periodos = {"anual": 1, "semestral": 2, "mensal": 12, "semanal": 52,
            "diária": 365, "horária": 365 * 24}
for nome, n in periodos.items():
    print(f"{nome:<10} n = {n:>5}: M = R$ {br(C * (1 + i / n) ** n)}")
print(f"{'contínua':<10} n → ∞  : M = R$ {br(C * math.exp(i))}   (M = C·e^(i·t))")
