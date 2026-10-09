eng2sp = dict()
eng2sp["one"] = "uno"
eng2sp.update({"two": "dos", "three": "tres"})
print(eng2sp, len(eng2sp))
print("one" in eng2sp, "uno" in eng2sp, "uno" in eng2sp.values())

def histograma(texto):
    contagem = {}
    for c in texto:
        contagem[c] = contagem.get(c, 0) + 1
    return contagem

print(histograma("brontossauro"))

t = ("a", "b", "c")
try:
    t[0] = "z"
except TypeError as erro:
    print("tupla é imutável:", erro)
x, y = 1, 2
x, y = y, x                                      # troca por atribuição de tupla
print(x, y)
