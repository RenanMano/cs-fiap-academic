from PIL import Image

# Abrir a imagem
imagem = Image.open("imagem.png")

# Converter para escala de cinza
imagem = imagem.convert("L")

# Redimensionar para 8 x 8
imagem = imagem.resize((8, 8))

print("Matriz 8 x 8\n")

# Percorrer as 8 linhas
for y in range(8):

    binario = ""

    for x in range(8):

        pixel = imagem.getpixel((x, y))

        # Branco = 1
        # Preto = 0
        if pixel >= 128:
            binario += "1"
        else:
            binario += "0"

    # Converter os 8 bits para um número
    valor = int(binario, 2)

    # Converter para hexadecimal
    hexadecimal = format(valor, "02X")

    print(binario, " = 0x" + hexadecimal)