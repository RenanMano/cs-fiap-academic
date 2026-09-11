import time
import gc

print("RAM inicial:")
print(gc.mem_free())

dados = []

for i in range(1000):

    dados.append(i)


print()
print("Depois de criar 1000 elementos:")
print(gc.mem_free())