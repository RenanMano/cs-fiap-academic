from PIL import Image

LIMIAR = 128            # abaixo disso o pixel é considerado escuro

imagem = Image.open("imagem.png").convert("L").resize((8, 8))

linhas = []
for y in range(8):
    bits = ""
    for x in range(8):
        escuro = imagem.getpixel((x, y)) < LIMIAR
        bits += "1" if escuro else "0"       # 1 = LED aceso = parte escura do desenho
    linhas.append(int(bits, 2))

print("Pré-visualização da matriz de LEDs:")
for valor in linhas:
    print("".join("██" if b == "1" else "··" for b in format(valor, "08b")))

print("\nBINÁRIO    HEX")
for valor in linhas:
    print(format(valor, "08b"), " 0x" + format(valor, "02X"))

print("\nimagem = [" + ", ".join("0x" + format(v, "02X") for v in linhas) + "]")
