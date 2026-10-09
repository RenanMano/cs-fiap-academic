def media_semestre(cps, sprints, gs):
    cps = sorted(cps)[1:]                        # o menor CP é desconsiderado
    pcc = sum(cps + sprints) / 4                 # 2 CPs + 2 Sprints (10% cada de 40%)
    return 0.4 * pcc + 0.6 * gs

def situacao(ma):
    if ma < 4:
        return "Reprovado"
    if ma < 6:
        return f"Exame (precisa de {12 - ma:.1f})"
    return "Aprovado"

ms1 = media_semestre([5.0, 8.0, 7.0], [9.0, 6.0], 6.5)
ms2 = media_semestre([6.0, 4.0, 7.5], [8.0, 7.0], 5.0)
ma = 0.4 * ms1 + 0.6 * ms2
print(f"MS1 = {ms1:.2f} | MS2 = {ms2:.2f} | MA = {ma:.2f} -> {situacao(ma)}")
print(situacao(4.5))
