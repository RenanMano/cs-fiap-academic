from machine import Pin
import time

# LED 1 -> FETCH, LED 2 -> DECODE, LED 3 -> EXECUTE
led_fetch = Pin(2, Pin.OUT)
led_decode = Pin(3, Pin.OUT)
led_execute = Pin(4, Pin.OUT)
LEDS = {"FETCH": led_fetch, "DECODE": led_decode, "EXECUTE": led_execute}

programa = [
    "LOAD R0 10",
    "LOAD R1 2",
    "SUB R0 R1",      # R0 = 8
    "LOAD R1 3",
    "MUL R0 R1",      # R0 = 24
    "STORE R0 R2",
]

registradores = {"R0": 0, "R1": 0, "R2": 0}
pc = 0
CLOCK = 1             # segundos por etapa (analogia didática, não é o clock real)


def etapa(nome):
    for chave, led in LEDS.items():
        led.value(1 if chave == nome else 0)   # só o LED da etapa atual acende
    print()
    print(nome)


while pc < len(programa):
    print("==============================")

    etapa("FETCH")
    instrucao = programa[pc]
    print("PC =", pc, "| Instrucao:", instrucao)
    time.sleep(CLOCK)

    etapa("DECODE")
    partes = instrucao.split()
    comando = partes[0]
    print("Comando:", comando)
    time.sleep(CLOCK)

    etapa("EXECUTE")
    if comando == "LOAD":
        registradores[partes[1]] = int(partes[2])
        print("Carregando", partes[2], "em", partes[1])
    elif comando == "ADD":
        registradores[partes[1]] += registradores[partes[2]]
        print(partes[1], "+", partes[2])
    elif comando == "SUB":
        registradores[partes[1]] -= registradores[partes[2]]
        print(partes[1], "-", partes[2])
    elif comando == "MUL":
        registradores[partes[1]] *= registradores[partes[2]]
        print(partes[1], "*", partes[2])
    elif comando == "STORE":
        registradores[partes[2]] = registradores[partes[1]]
        print("Copiando", partes[1], "para", partes[2])
    else:
        print("Instrucao desconhecida:", comando)
    print("R0 =", registradores["R0"], "| R1 =", registradores["R1"], "| R2 =", registradores["R2"])
    time.sleep(CLOCK)

    pc += 1

etapa("FIM")          # nenhum LED corresponde a "FIM": todos apagam
