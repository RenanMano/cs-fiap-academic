from PIL import Image

# Abrir imagem
imagem = Image.open("C:\\Users\\labsfiap\\Desktop\\cs-fiap-academic\\computer-organization-and-architecture\\aula05-02-10-26\\imagem.png")

# Converter para preto e branco
imagem = imagem.convert("L")

# Redimensionar para 8 x 8
imagem = imagem.resize((8, 8))

print("\nMATRIZ 8 x 8\n")

# Percorrer as linhas
for y in range(8):

    binario = ""

    # Criar a sequência binária da linha
    for x in range(8):

        pixel = imagem.getpixel((x, y))

        if pixel >= 128:
            binario += "1"
        else:
            binario += "0"

    # Mostrar a matriz usando blocos
    for bit in binario:

        if bit == "1":
            print("██", end="")
        else:
            print("  ", end="")

    print()


print("\nBINÁRIO          HEXADECIMAL")
print("--------------------------------")

# Mostrar binário e hexadecimal
for y in range(8):

    binario = ""

    for x in range(8):

        pixel = imagem.getpixel((x, y))

        if pixel >= 128:
            binario += "1"
        else:
            binario += "0"

    valor = int(binario, 2)

    hexadecimal = format(valor, "02X")

    print(f"{binario}          0x{hexadecimal}")