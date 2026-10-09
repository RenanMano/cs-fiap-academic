# Atividade 1 (algoritmos traduzidos para Python; entradas fixas no lugar de input())
nome = "Ana"
print(f"Seja bem vindo, {nome}!")                       # A
print("Soma:", 7 + 5)                                   # B
ano_atual, ano_nascimento = 2026, 2007
print("Idade:", ano_atual - ano_nascimento)             # C
preco = 150.0
print(f"Com 27% de desconto: R$ {preco * (1 - 0.27):.2f}")   # D

# Atividade 2: desconto de 25% acima de R$ 200, senão 5%
for valor in (250.0, 200.0, 80.0):
    desconto = 0.25 if valor > 200 else 0.05
    print(f"R$ {valor:.2f} -> R$ {valor * (1 - desconto):.2f}")

# Atividade 3: somar 5 números usando só 2 variáveis
soma = 0
for numero in (2, 3, 5, 8, 10):
    soma = soma + numero
print("Soma da sequência:", soma)
