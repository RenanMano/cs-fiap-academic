from machine import Pin

# bit 0 no GPIO 2 ... bit 3 no GPIO 5 (mesma ligação do material)
leds = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT)]


def mostrar_nos_leds(numero):
    for bit, led in enumerate(leds):
        led.value((numero >> bit) & 1)      # extrai o bit de posição 'bit'


while True:
    entrada = input("Digite um número de 0 a 15: ")
    try:
        numero = int(entrada)
    except ValueError:
        print("Número inválido! Digite um número inteiro entre 0 e 15.")
        continue
    if not 0 <= numero <= 15:
        print("Número inválido! Digite um número entre 0 e 15.")
        continue

    binario = "{:04b}".format(numero)
    print("Decimal:", numero, "| Binário:", binario, "| Hexadecimal:", hex(numero))
    mostrar_nos_leds(numero)
