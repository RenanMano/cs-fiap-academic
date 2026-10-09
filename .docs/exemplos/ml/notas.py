def media_final(sem1, sem2):
    return 0.4 * sem1 + 0.6 * sem2

def situacao(sem1, sem2, frequencia):
    mf = media_final(sem1, sem2)
    if mf >= 60 and frequencia >= 75:
        return f"{mf:.1f} -> Aprovado"
    return f"{mf:.1f} -> Dependência (DP)"

print(situacao(70, 65, 90))
print(situacao(80, 50, 90))
print(situacao(75, 70, 60))
