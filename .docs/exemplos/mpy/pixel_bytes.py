# O ícone de exemplo do enunciado: 8 linhas de 8 bits -> 8 bytes -> de volta à imagem
linhas = ["00111100", "01111110", "11011011", "11111111",
          "11111111", "01111110", "00111100", "00011000"]

imagem = [int(bits, 2) for bits in linhas]               # cada linha de 8 bits é 1 byte
print("bytes:", [f"0x{b:02X}" for b in imagem])

print("reconstrução a partir dos bytes:")
for b in imagem:
    print("".join("█" if (b >> (7 - col)) & 1 else "·" for col in range(8)))

bits = 8 * len(imagem)
print(f"memória: {bits} bits = {bits // 8} bytes")

ESTADOS = {1: "ESTAÇÃO DISPONÍVEL", 2: "VEÍCULO CONECTADO", 3: "CARREGANDO",
           4: "CARGA CONCLUÍDA", 5: "ERRO"}
codigo = 3
print(f"código {codigo:02d} = {ESTADOS[codigo]}")
