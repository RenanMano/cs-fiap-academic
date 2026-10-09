def lcg(semente, n, a=1103515245, c=12345, m=2**31):
    """Gerador congruencial linear: estado(k+1) = (a * estado(k) + c) mod m."""
    estado = semente
    saida = []
    for _ in range(n):
        estado = (a * estado + c) % m      # atualização do estado
        saida.append(estado % 100 + 1)     # "bits aleatórios" convertidos para 1..100
    return saida

print(lcg(2026, 8))
print(lcg(2026, 8))        # determinístico: mesma semente, mesma sequência
print(lcg(2027, 8))        # semente diferente, sequência diferente
