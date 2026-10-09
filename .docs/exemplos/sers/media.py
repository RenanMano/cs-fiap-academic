# Regra de avaliação dos slides de apresentação (notas de 0 a 10)
def media_semestral(checkpoints, sprints, gs):
    cps = sorted(checkpoints)[1:]                      # 3 checkpoints: a menor nota é excluída
    cp = sum(cps) / len(cps)
    sprint = sum(sprints) / len(sprints)               # 2 entregáveis do Challenge
    return 0.2 * cp + 0.2 * sprint + 0.6 * gs          # CP 20% + Sprint 20% + GS 60%

def situacao(media_final):
    if media_final >= 6.0:                             # 5,9 já é exame, então 6,0 aprova
        return "APROVADO"
    if media_final >= 4.0:
        return "EXAME"
    return "REPROVADO"

ms1 = media_semestral([7.0, 4.0, 8.0], [8.0, 9.0], 6.5)
ms2 = media_semestral([5.0, 6.0, 9.0], [7.0, 7.0], 5.0)
final = 0.4 * ms1 + 0.6 * ms2                          # MÉDIA FINAL = 0,4 x MS1 + 0,6 x MS2
print(f"MS1 = {ms1:.2f} | MS2 = {ms2:.2f} | média final = {final:.2f} -> {situacao(final)}")
for nota in (6.0, 5.9, 3.9):
    print(nota, situacao(nota))
