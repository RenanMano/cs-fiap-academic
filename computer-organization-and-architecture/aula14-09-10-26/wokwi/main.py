# ChargeGrid Pixel - Raspberry Pi Pico (MicroPython) + matriz LED 8x8 MAX7219
from machine import Pin, SPI
import time

# ---- Memoria/Dados: 8 bytes por icone (gerados pelo chargegrid_converter.py) ----
ICONES = {
    "01": [0x3C, 0x42, 0x81, 0x81, 0x81, 0x81, 0x42, 0x3C],
    "02": [0x24, 0x24, 0x7E, 0x7E, 0x7E, 0x3C, 0x18, 0x18],
    "03": [0x0E, 0x1C, 0x38, 0x7E, 0x1C, 0x38, 0x70, 0x20],
    "04": [0x00, 0x01, 0x03, 0x86, 0xCC, 0x78, 0x30, 0x00],
    "05": [0x18, 0x18, 0x18, 0x18, 0x18, 0x00, 0x18, 0x18],
}
ESTADOS = {"01": "ESTACAO DISPONIVEL", "02": "VEICULO CONECTADO",
           "03": "VEICULO CARREGANDO", "04": "CARGA CONCLUIDA", "05": "ERRO"}

# ---- Driver MAX7219 (SPI0: SCK=GP18, MOSI=GP19, CS=GP17) ----
spi = SPI(0, baudrate=10_000_000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19))
cs = Pin(17, Pin.OUT, value=1)

def escrever(reg, valor):
    cs.value(0)
    spi.write(bytearray([reg, valor]))
    cs.value(1)

def iniciar():
    for reg, val in ((0x09, 0x00), (0x0A, 0x08), (0x0B, 0x07), (0x0C, 0x01), (0x0F, 0x00)):
        escrever(reg, val)   # sem decode, brilho, 8 linhas, ligado, sem teste

def desenhar(dados):
    for linha in range(8):           # processa cada byte -> 1 linha de LEDs
        escrever(linha + 1, dados[linha])

def mostrar_terminal(codigo):
    dados = ICONES[codigo]
    print("=" * 32); print(" CHARGEGRID PIXEL"); print("=" * 32)
    print("Estado:", ESTADOS[codigo]); print("Codigo:", codigo)
    print("\nMATRIZ BINARIA:")
    for b in dados: print("{:08b}".format(b))
    print("\nREPRESENTACAO HEXADECIMAL:")
    for b in dados: print("0x{:02X}".format(b))
    print("\nMEMORIA UTILIZADA:\n{} bits\n{} bytes".format(len(dados) * 8, len(dados)))
    print("=" * 32)

iniciar()
sequencia = ["01", "02", "03", "04", "05"]   # codigos recebidos pela estacao
while True:
    for codigo in sequencia:
        mostrar_terminal(codigo)
        desenhar(ICONES[codigo])
        time.sleep(3)
