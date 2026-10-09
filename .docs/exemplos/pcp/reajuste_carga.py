def reajuste(salario):
    if salario <= 280:
        pct = 20
    elif salario < 700:
        pct = 15
    elif salario < 1500:
        pct = 10
    else:
        pct = 5
    aumento = salario * pct / 100
    return f"antes R$ {br(salario)} | {pct}% | aumento R$ {br(aumento)} | novo R$ {br(salario + aumento)}"

br = lambda v: f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

IMPOSTO = {1: 0.35, 2: 0.25, 3: 0.15, 4: 0.05, 5: 0.0}       # estado de origem → imposto

def preco_kg(codigo):
    if 10 <= codigo <= 20: return 100.00
    if 21 <= codigo <= 30: return 250.00
    return 340.00                                            # 31 a 40

def carga(estado, toneladas, codigo):
    kg = toneladas * 1000
    preco = kg * preco_kg(codigo)
    imposto = preco * IMPOSTO[estado]
    return f"{kg:.0f} kg | preço R$ {br(preco)} | imposto R$ {br(imposto)} | total R$ {br(preco + imposto)}"

def triangulo(*lados):
    a, b, c = sorted(lados, reverse=True)
    if a >= b + c:
        return "NAO FORMA TRIANGULO"
    tipos = []
    if a**2 == b**2 + c**2:  tipos.append("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2: tipos.append("TRIANGULO OBTUSANGULO")
    else:                    tipos.append("TRIANGULO ACUTANGULO")
    if a == b == c:          tipos.append("TRIANGULO EQUILATERO")
    elif a == b or b == c:   tipos.append("TRIANGULO ISOSCELES")
    return ", ".join(tipos)

for s in (250, 500, 1000, 2000):
    print(reajuste(s))
print(carga(1, 2.5, 15))
print(carga(5, 1, 35))
for lados in [(7, 5, 7), (6, 6, 10), (6, 6, 6), (5, 7, 2), (3, 4, 5)]:
    print(lados, "->", triangulo(*lados))
