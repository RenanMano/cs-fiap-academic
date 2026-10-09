import random

def jogar(trocar):
    portas = [1, 2, 3]
    carro = random.choice(portas)
    escolha = random.choice(portas)
    # o apresentador abre uma porta que não é a escolhida e não tem o carro
    aberta = random.choice([p for p in portas if p != escolha and p != carro])
    if trocar:
        escolha = next(p for p in portas if p != escolha and p != aberta)
    return escolha == carro

random.seed(447)
n = 100_000
fica = sum(jogar(False) for _ in range(n)) / n
troca = sum(jogar(True) for _ in range(n)) / n
print(f"permanecer: {fica:.3f}   (teoria 1/3 = 0.333)")
print(f"trocar:     {troca:.3f}   (teoria 2/3 = 0.667)")
