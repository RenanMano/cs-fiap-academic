# AVL montada a partir das etapas do tutorial (altura em nós: folha = 1, vazio = 0)
class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.altura = 1


class AVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        return 0 if no is None else no.altura

    def atualizar_altura(self, no):
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def fator_balanceamento(self, no):
        return 0 if no is None else self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, y):
        x, temp = y.esquerda, y.esquerda.direita
        x.direita, y.esquerda = y, temp
        self.atualizar_altura(y)                    # primeiro o nó que desceu
        self.atualizar_altura(x)
        return x

    def rotacao_esquerda(self, x):
        y, temp = x.direita, x.direita.esquerda
        y.esquerda, x.direita = x, temp
        self.atualizar_altura(x)
        self.atualizar_altura(y)
        return y

    def inserir_recursivo(self, no, dado):
        if no is None:
            return No(dado)
        if dado < no.dado:
            no.esquerda = self.inserir_recursivo(no.esquerda, dado)
        elif dado > no.dado:
            no.direita = self.inserir_recursivo(no.direita, dado)
        else:
            return no                               # duplicatas não entram
        self.atualizar_altura(no)
        fb = self.fator_balanceamento(no)
        if fb > 1 and dado < no.esquerda.dado:      # LL
            return self.rotacao_direita(no)
        if fb < -1 and dado > no.direita.dado:      # RR
            return self.rotacao_esquerda(no)
        if fb > 1 and dado > no.esquerda.dado:      # LR
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
        if fb < -1 and dado < no.direita.dado:      # RL
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)
        return no

    def inserir(self, dado):
        self.raiz = self.inserir_recursivo(self.raiz, dado)   # a raiz pode mudar

    def em_ordem(self, no, saida):
        if no:
            self.em_ordem(no.esquerda, saida)
            saida.append(no.dado)
            self.em_ordem(no.direita, saida)
        return saida

    def mostrar(self, no, nivel=0):
        if no is None:
            return
        self.mostrar(no.direita, nivel + 1)
        print("    " * nivel + f"{no.dado} (h={no.altura}, FB={self.fator_balanceamento(no)})")
        self.mostrar(no.esquerda, nivel + 1)


for caso, seq in (("LL", [30, 20, 10]), ("RR", [10, 20, 30]), ("LR", [30, 10, 20]), ("RL", [10, 30, 20])):
    a = AVL()
    for v in seq:
        a.inserir(v)
    print(caso, seq, "-> raiz", a.raiz.dado, "| em ordem:", a.em_ordem(a.raiz, []))

a = AVL()
for v in [10, 20, 30, 40, 50, 25]:
    a.inserir(v)
a.mostrar(a.raiz)
print("raiz:", a.raiz.dado, "| altura:", a.raiz.altura, "| em ordem:", a.em_ordem(a.raiz, []))
