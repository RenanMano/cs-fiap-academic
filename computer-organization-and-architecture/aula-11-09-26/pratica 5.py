import time
import gc

print("Memória inicial:")

print(gc.mem_free())

dados = []

for i in range(1000):

    dados.append(i)

print()

print("Depois da lista:")

print(gc.mem_free())

dados = None

gc.collect()

print()
print("Depois de liberar a lista:")
print(gc.mem_free())