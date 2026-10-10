# MicroChallenge 2 - ChargeGrid Pixel
**Disciplina:** Computer Organization and Architecture - Prof. Dr. Marcus Grilo
**Equipe:** Gabriel Barbosa Furin - RM: 572941 
            Lucas Kiodi Moraca - RM: 571004 
            Renan Fracalossi Mano da Silva - RM: 569610

## 1. Imagem utilizada
Estado principal: **03 - Veiculo carregando** (raio). Arquivo: `imagens/03_carregando.png`.
Tambem foram criados os icones dos demais estados (01, 02, 04, 05).

## 2. Fluxo
Imagem -> Pixels -> Bits -> Bytes -> Hexadecimal -> Raspberry Pi Pico -> Memoria -> Matriz 8x8 -> Icone

## 3. Matriz binaria 8x8 (estado 03)
```
00001110   0x0E
00011100   0x1C
00111000   0x38
01111110   0x7E
00011100   0x1C
00111000   0x38
01110000   0x70
00100000   0x20
```
0 = LED apagado, 1 = LED aceso.

## 4. Valores em hexadecimal (todos os estados)
| Codigo | Estado | Bytes |
|---|---|---|
| 01 | Estacao disponivel | 3C 42 81 81 81 81 42 3C |
| 02 | Veiculo conectado | 24 24 7E 7E 7E 3C 18 18 |
| 03 | Veiculo carregando | 0E 1C 38 7E 1C 38 70 20 |
| 04 | Carga concluida | 00 01 03 86 CC 78 30 00 |
| 05 | Erro | 18 18 18 18 18 00 18 18 |

## 5. Memoria
Cada icone: 8 linhas x 8 bits = **64 bits = 8 bytes**. A imagem nao e guardada como foto, e sim como 8 numeros.
Uma foto de 256x256 em escala de cinza ocuparia 65.536 bytes; o icone usa 8 (8.192x menos).

## 6. Funcionamento
- **Python (PIL):** abre a imagem, converte para cinza, redimensiona para 8x8 (BOX), aplica limiar 128 (0/1), imprime a matriz, agrupa cada linha em um byte e mostra em hexadecimal (`chargegrid_converter.py`).
- **Raspberry Pi Pico (Wokwi):** guarda os bytes num dicionario (memoria), recebe o codigo do estado, le os 8 bytes e envia cada um via SPI ao MAX7219, que acende a linha correspondente (`wokwi/main.py`).

## 7. Arquivos da entrega
`chargegrid_converter.py`, `gerar_icones.py`, `imagens/`, `saida_terminal.txt`, `wokwi/main.py`, `wokwi/diagram.json`, `wokwi/MONTAGEM_WOKWI.md`.
**Link do Wokwi:** https://wokwi.com/projects/477444044974592001  |  **Link do video:** https://youtu.be/8njrERcRI1Y 