import random

random.seed(1)                                        # mesma semente -> mesma sequência
print(random.sample(range(1, 6), 5))                  # inteiros sem repetição
print([random.randint(1, 100) for _ in range(6)])     # inteiros com repetição
print([round(random.uniform(1, 10), 2) for _ in range(5)])  # decimais

random.seed(1)
a = [random.randint(1, 100) for _ in range(9)]
random.seed(1)
b = [random.randint(1, 100) for _ in range(9)]
print(a)
print("sequências idênticas com a mesma semente?", a == b)
