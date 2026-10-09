# while com contador (fluxograma dos slides: exibir "Produto" 3 vezes)
cp = 0
while cp < 3:
    print("Produto", cp)
    cp = cp + 1

# continue e break
for n in range(1, 10):
    if n % 2 == 0:
        continue            # pula os pares
    if n > 7:
        break               # sai do laço
    print("ímpar:", n)

# laços aninhados (tabela de rastreio dos slides: I de 0 a 3, J de 0 a 2 com passo 2)
print([(i, j) for i in range(0, 4) for j in range(0, 3, 2)])
