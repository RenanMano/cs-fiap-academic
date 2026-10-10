"""ChargeGrid Pixel - Parte 1 e 2: Imagem -> Pixels -> Bits -> Bytes -> Hexadecimal"""
import sys, glob, os
from PIL import Image

ESTADOS = {"01": "ESTACAO DISPONIVEL", "02": "VEICULO CONECTADO",
           "03": "VEICULO CARREGANDO", "04": "CARGA CONCLUIDA", "05": "ERRO"}

def imagem_para_matriz(caminho, limiar=128):
    img = Image.open(caminho).convert("L")          # escala de cinza
    img = img.resize((8, 8), Image.BOX)             # redimensiona para 8x8
    # preto e branco -> 0 e 1 (claro = LED aceso)
    return [[1 if img.getpixel((x, y)) >= limiar else 0 for x in range(8)] for y in range(8)]

def linha_para_byte(linha):
    valor = 0
    for bit in linha:
        valor = (valor << 1) | bit
    return valor

def mostrar(caminho):
    codigo = os.path.basename(caminho)[:2]
    matriz = imagem_para_matriz(caminho)
    bytes_ = [linha_para_byte(l) for l in matriz]
    print("=" * 32); print(" CHARGEGRID PIXEL"); print("=" * 32)
    print(f"Estado: {ESTADOS.get(codigo, 'DESCONHECIDO')}\nCodigo: {codigo}")
    print("\nMATRIZ BINARIA:")
    for l in matriz: print("".join(map(str, l)).replace("1", "1").replace("0", "0"))
    print("\nIMAGEM (visual):")
    for l in matriz: print("".join("##" if b else "  " for b in l))
    print("\nREPRESENTACAO HEXADECIMAL:")
    for b in bytes_: print(f"0x{b:02X}")
    print(f"\nMEMORIA UTILIZADA:\n{len(bytes_)*8} bits\n{len(bytes_)} bytes")
    print("=" * 32)
    return codigo, bytes_

if __name__ == "__main__":
    arquivos = sys.argv[1:] or sorted(glob.glob("imagens/*.png"))
    resultado = {}
    for a in arquivos:
        c, b = mostrar(a); resultado[c] = b
        print()
    print("# Cole no main.py do Raspberry (Wokwi):")
    print("ICONES = {")
    for c, b in resultado.items():
        print(f'    "{c}": [{", ".join(f"0x{x:02X}" for x in b)}],')
    print("}")
