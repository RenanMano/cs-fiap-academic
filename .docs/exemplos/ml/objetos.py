import io
import pandas

lista = [2, 3, 6, 9, 8, 5, 10]
tupla = (1, "Python", True, 3.14)
dicionario = {"nome": "Notebook", "marca": "Dell", "preco": 4299.90}
conjunto = set([1, 2, 3, 2, 1])

print(lista[2], lista[2:5], lista[10:12])    # índice, fatia, fatia fora do intervalo
print(tupla[1], dicionario["preco"], conjunto)
print({1, 2, 3} | {3, 4, 5}, {1, 2, 3} & {3, 4, 5}, {1, 2, 3} - {3, 4, 5})
print([type(o).__name__ for o in (lista, tupla, dicionario, conjunto)])

# mesmo conteúdo do arquivo DadosAula(2).txt desta pasta (colunas separadas por espaço)
texto = "Nome Idade\nMaria 25\nJoão 26\nGabriel 30\nDaniela 22"
dados1 = pandas.read_csv(io.StringIO(texto), sep=" ", header=0)
print(dados1)
print("Idade média:", dados1["Idade"].mean())
