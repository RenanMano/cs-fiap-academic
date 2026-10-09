freq = {1: 24, 2: 33, 3: 42, 4: 30, 5: 21}     # nível de estresse x: frequência (150 funcionários)
n = sum(freq.values())

dist = {x: f / n for x, f in freq.items()}
for x, p in dist.items():
    print(f"P(X = {x}) = {freq[x]}/{n} = {p:.2f}")
print("soma das probabilidades:", round(sum(dist.values()), 10))

acumulada = 0
for x, p in dist.items():
    acumulada += p
    print(f"F({x}) = P(X <= {x}) = {acumulada:.2f}")
