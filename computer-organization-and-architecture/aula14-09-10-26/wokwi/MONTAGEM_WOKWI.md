# Passo a passo - Wokwi (Raspberry Pi Pico + matriz 8x8)

1. Acesse https://wokwi.com e faca login (opcional, mas permite salvar o link).
2. Clique em **New Project** > **Raspberry Pi Pico** > **MicroPython**.
3. Clique no **+** (Add a new part) e adicione **MAX7219 LED Matrix** (matriz 8x8, 1 modulo).
4. Ligue os fios (Pico -> Matriz):

| Pico | Matriz MAX7219 | Cor sugerida |
|------|----------------|--------------|
| GP19 (SPI0 TX) | DIN | verde |
| GP17 | CS | laranja |
| GP18 (SPI0 SCK) | CLK | azul |
| 3V3(OUT) | V+ (VCC) | vermelho |
| GND | GND | preto |

5. Abra o arquivo **main.py**, apague o conteudo e cole o `main.py` desta pasta.
6. (Atalho) Abra **diagram.json**, apague e cole o `diagram.json` desta pasta - ja monta a ligacao.
   Se a matriz nao aparecer ligada, confira os nomes dos pinos manualmente (tabela acima).
7. Clique em **Start the simulation** (botao verde). A matriz mostra cada icone por 3 s
   (codigos 01 a 05) e o terminal exibe matriz binaria, hexadecimal e memoria.
8. Clique em **Save** e copie o link do projeto para a entrega.

Observacao: se a imagem aparecer espelhada, troque `dados[linha]` por
`int('{:08b}'.format(dados[linha])[::-1], 2)` na funcao `desenhar`.
