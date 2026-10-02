dados = [
    0b00111100,
    0b01100110,
    0b11000011,
    0b11000011,
    0b11111111,
    0b11000011,
    0b11000011,
    0b11000011
]

for byte in dados:

    binario = format(byte, "08b")

    for bit in binario:

        if bit == "1":
            print("██", end="")
        else:
            print("  ", end="")

    print()