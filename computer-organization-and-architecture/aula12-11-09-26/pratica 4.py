import gc
import time

def mostrar_memoria():

    print("-------------------------")

    print("RAM utilizada:", gc.mem_alloc())

    print("RAM livre:", gc.mem_free())

    print("-------------------------")

print("Memória inicial")

mostrar_memoria()


dados = []


for i in range(0, 1000):

    dados.append(i)

    if i % 100 == 0:

        print("Elementos:", i)
        mostrar_memoria()
        time.sleep(1)