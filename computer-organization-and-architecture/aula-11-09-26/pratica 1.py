import time
import gc 
import micropython  

print("================================")
print("      ORGANIZAÇÃO DA MEMÓRIA")
print("================================")

print()

print("RAM livre:") #retorna a quantidade aproximada de memória disponível para o gerenciamento de objetos
print(gc.mem_free(), "bytes")

print("RAM utilizada:") # informa a memória atualmente alocada para objetos gerenciados pelo garbage collector
print(gc.mem_alloc(), "bytes")

print()

print("Informações detalhadas:")
micropython.mem_info()