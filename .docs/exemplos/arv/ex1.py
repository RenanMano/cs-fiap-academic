class No:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

def pre_ordem(no):
    if no is None:
        return []
    return [no.valor] + pre_ordem(no.esquerda) + pre_ordem(no.direita)

def em_ordem(no):
    if no is None:
        return []
    return em_ordem(no.esquerda) + [no.valor] + em_ordem(no.direita)

def pos_ordem(no):
    if no is None:
        return []
    return pos_ordem(no.esquerda) + pos_ordem(no.direita) + [no.valor]

# árvore de 8 + 4 * 2: o "*" fica mais fundo porque é calculado antes
raiz = No("+", No("8"), No("*", No("4"), No("2")))

print("pré-ordem :", " ".join(pre_ordem(raiz)))
print("em ordem  :", " ".join(em_ordem(raiz)))
print("pós-ordem :", " ".join(pos_ordem(raiz)))
