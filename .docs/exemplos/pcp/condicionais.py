import math                                   # módulo da biblioteca padrão

def par_ou_impar(n):
    return "par" if n % 2 == 0 else "ímpar"

def maior(a, b):
    if a == b:
        return "iguais"
    return max(a, b)

def situacao(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        return f"{media:.2f} Aprovado"
    elif media >= 5:
        return f"{media:.2f} Em recuperação"
    return f"{media:.2f} Reprovado"

def multiplos(a, b):
    return "São Múltiplos" if a % b == 0 or b % a == 0 else "Não são Múltiplos"

def calcular(a, b, op):
    match op:                                 # o "switch/case" do Python (3.10+)
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "/": return a / b if b != 0 else "divisão por zero"
        case _:   return "operação inválida"

def voto(ano_nascimento, ano_atual=2026):
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f"{idade} anos: proibido"
    if 16 <= idade < 18 or idade > 70:
        return f"{idade} anos: opcional"
    return f"{idade} anos: obrigatório"

print(par_ou_impar(7), par_ou_impar(10))
print(maior(3, 9), maior(4, 4))
print(situacao([8, 7, 6, 9]), "|", situacao([5, 6, 4, 7]), "|", situacao([3, 4, 5, 2]))
print(multiplos(3, 12), "|", multiplos(5, 7))
print(calcular(5, 6, "*"), calcular(9, 0, "/"))
print(voto(2012), "|", voto(2009), "|", voto(1990), "|", voto(1950))
print("raiz de 2 (módulo math):", round(math.sqrt(2), 4))
