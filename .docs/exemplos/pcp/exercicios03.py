PI = 3.14159
print(f"1) área do círculo de raio 5: {PI * 5 ** 2:.4f}")

fahrenheit = 98.6
print(f"2/3) {fahrenheit} °F = {(fahrenheit - 32) * 5 / 9:.1f} °C")

print("4) total gasto: R$", 3 * 25 + 2 * 5)
print("5) tempo:", 150 / 60, "h")

a, b = 7.0, 8.5                                 # notas (no slide, lidas com input)
print("6) média aritmética:", (a + b) / 2)
print("7) média ponderada:", (a * 4 + b * 6) / 10)

peca1, qtd1, valor1 = "parafuso", 10, 0.75
peca2, qtd2, valor2 = "porca", 20, 0.30
print(f"8) total ({peca1} e {peca2}): R$ {qtd1 * valor1 + qtd2 * valor2:.2f}")

produto, pago = 37.40, 50.00
print(f"9) troco: R$ {pago - produto:.2f}")
