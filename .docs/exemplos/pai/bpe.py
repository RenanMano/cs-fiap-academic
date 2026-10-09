# Byte Pair Encoding (BPE) em miniatura, com o corpus do slide
from collections import Counter

def passo_bpe(tokens):
    pares = Counter(zip(tokens, tokens[1:]))
    (a, b), freq = pares.most_common(1)[0]   # par mais frequente (empate: o que aparece primeiro)
    novos, i = [], 0
    while i < len(tokens):
        if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == (a, b):
            novos.append(a + b)               # funde o par num novo token
            i += 2
        else:
            novos.append(tokens[i])
            i += 1
    return novos, a + b, freq

tokens = list("AACGCACTATATA")
vocabulario = sorted(set(tokens))
print(f"0: {' '.join(tokens)}  vocab={vocabulario}")
for it in (1, 2, 3):
    tokens, novo, freq = passo_bpe(tokens)
    vocabulario.append(novo)
    print(f"{it}: {' '.join(tokens)}  +{novo} (freq {freq})  vocab={vocabulario}")
