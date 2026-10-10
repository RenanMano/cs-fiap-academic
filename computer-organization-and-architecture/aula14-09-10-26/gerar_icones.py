"""Gera as imagens PNG (256x256) dos 5 estados da ChargeGrid Pixel.
Cada imagem e desenhada em grade 8x8 (branco = LED aceso) e ampliada."""
from PIL import Image

ICONES = {
 "01_disponivel": ["00111100","01000010","10000001","10000001","10000001","10000001","01000010","00111100"],
 "02_conectado":  ["00100100","00100100","01111110","01111110","01111110","00111100","00011000","00011000"],
 "03_carregando": ["00001110","00011100","00111000","01111110","00011100","00111000","01110000","00100000"],
 "04_concluido":  ["00000000","00000001","00000011","10000110","11001100","01111000","00110000","00000000"],
 "05_erro":       ["00011000","00011000","00011000","00011000","00011000","00000000","00011000","00011000"],
}
for nome, linhas in ICONES.items():
    img = Image.new("L", (8, 8))
    img.putdata([255 if c == "1" else 0 for l in linhas for c in l])
    img.resize((256, 256), Image.NEAREST).save(f"imagens/{nome}.png")
print("Imagens geradas em imagens/")
