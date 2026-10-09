from machine import Pin

led_verde = Pin(15, Pin.OUT)
led_vermelho = Pin(14, Pin.OUT)

ENERGIA_KW = 8

COMANDOS = {
    "0001": "START",
    "0010": "STOP",
    "0011": "STATUS",
    "0100": "ENERGY",
    "0101": "ERROR",
    "0110": "RESET",
    "0111": "LOCK",
    "1000": "UNLOCK",
}

estado = "DISPONIVEL"           # memória: estado atual da estação


def leds(verde, vermelho):
    led_verde.value(verde)
    led_vermelho.value(vermelho)


def menu():
    print("=" * 32)
    print("      CHARGEGRID PROTOCOL")
    print("=" * 32)
    print("Estacao pronta.")
    print("Digite um comando:")
    for codigo, nome in COMANDOS.items():
        print(codigo, "-", nome)


def executar(codigo):
    global estado
    nome = COMANDOS.get(codigo)
    print("Comando recebido:", codigo)

    if nome is None:
        led_vermelho.value(1)          # sinaliza o erro sem alterar o estado
        print("ERROR")
        print("COMANDO INVALIDO")
        return

    print("Comando:", nome)

    if nome == "START":
        if estado in ("BLOQUEADA", "ERRO"):
            print("Recusado: estacao", estado)
            return
        estado = "CARREGANDO"
        leds(1, 0)
        print("Estado da estacao: INICIAR CARREGAMENTO")
    elif nome == "STOP":
        if estado == "CARREGANDO":
            estado = "DISPONIVEL"
        led_verde.value(0)
        print("Estado da estacao: PARAR O CARREGAMENTO")
    elif nome == "STATUS":
        print("Estado atual:", estado)
    elif nome == "ENERGY":
        print("Energia disponivel:", ENERGIA_KW, "kW")
        print("Decimal:", ENERGIA_KW)
        print("Binario:", "{:b}".format(ENERGIA_KW))
    elif nome == "ERROR":
        estado = "ERRO"
        leds(0, 1)
        print("Estado da estacao: ERRO")
    elif nome == "RESET":
        estado = "DISPONIVEL"
        leds(0, 0)
        print("Estado da estacao: DISPONIVEL (reiniciada)")
    elif nome == "LOCK":
        estado = "BLOQUEADA"
        leds(0, 1)
        print("Estado da estacao: BLOQUEADA")
    elif nome == "UNLOCK":
        estado = "DISPONIVEL"
        leds(0, 0)
        print("Estado da estacao: DISPONIVEL")


menu()
while True:
    codigo = input("Comando: ").strip()
    executar(codigo)
    print("-" * 32)
