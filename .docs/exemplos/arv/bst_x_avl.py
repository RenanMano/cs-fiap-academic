# Etapa 13 do tutorial: inserir 1..100 numa BST comum e numa AVL e buscar o 100
class No:
    def __init__(self, dado):
        self.dado, self.esquerda, self.direita, self.altura = dado, None, None, 1

def h(no):
    return no.altura if no else 0

def atualizar(no):
    no.altura = 1 + max(h(no.esquerda), h(no.direita))

def inserir_bst(raiz, dado):                      # iterativa: evita 100 chamadas aninhadas
    novo = No(dado)
    if raiz is None:
        return novo
    atual, caminho = raiz, []
    while True:
        caminho.append(atual)
        lado = "esquerda" if dado < atual.dado else "direita"
        if getattr(atual, lado) is None:
            setattr(atual, lado, novo)
            break
        atual = getattr(atual, lado)
    for no in reversed(caminho):
        atualizar(no)
    return raiz

def rot_dir(y):
    x = y.esquerda; y.esquerda, x.direita = x.direita, y; atualizar(y); atualizar(x); return x

def rot_esq(x):
    y = x.direita; x.direita, y.esquerda = y.esquerda, x; atualizar(x); atualizar(y); return y

def inserir_avl(no, dado):
    if no is None:
        return No(dado)
    if dado < no.dado:
        no.esquerda = inserir_avl(no.esquerda, dado)
    elif dado > no.dado:
        no.direita = inserir_avl(no.direita, dado)
    else:
        return no
    atualizar(no)
    fb = h(no.esquerda) - h(no.direita)
    if fb > 1 and dado < no.esquerda.dado: return rot_dir(no)
    if fb < -1 and dado > no.direita.dado: return rot_esq(no)
    if fb > 1:
        no.esquerda = rot_esq(no.esquerda); return rot_dir(no)
    if fb < -1:
        no.direita = rot_dir(no.direita); return rot_esq(no)
    return no

def visitados(no, alvo):
    n = 0
    while no:
        n += 1
        if alvo == no.dado:
            return n
        no = no.esquerda if alvo < no.dado else no.direita
    return n

bst = avl = None
for v in range(1, 101):
    bst = inserir_bst(bst, v)
    avl = inserir_avl(avl, v)
print(f"BST: altura {bst.altura}, nós visitados para achar 100: {visitados(bst, 100)}")
print(f"AVL: altura {avl.altura}, nós visitados para achar 100: {visitados(avl, 100)}, raiz {avl.dado}")
