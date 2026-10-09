# =====================================================================
# CALCULADORA DE EXPRESSÕES COM ÁRVORE BINÁRIA (DSA)
# =====================================================================
# Caminho do programa (igual ao fluxograma do PDF):
#
#   texto digitado -> tokenizar -> para_posfixa -> construir_arvore
#                                                      |
#                                    percursos / gerar_expressao / calcular
#
# O arquivo segue a ORDEM DAS SEÇÕES DO PDF. Dica de estudo: leia o
# enunciado de uma função, tente escrevê-la sozinho e só depois compare.
# =====================================================================

OPERADORES = ("+", "-", "*", "/")


# ---------------------------------------------------------------------
# SEÇÃO 4: O NÓ DA ÁRVORE
# ---------------------------------------------------------------------
# Cada nó guarda um valor (número ou operador) e referências para os
# filhos. Número = folha (sem filhos). Operador = nó interno (2 filhos).
# O valor fica guardado como TEXTO (ex.: "12.5"); só viramos número
# na hora de calcular.
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def eh_folha(no):
    # folha = nó sem nenhum filho
    return no.esquerda is None and no.direita is None


# ---------------------------------------------------------------------
# SEÇÃO 5: TOKENIZAÇÃO
# ---------------------------------------------------------------------
# Objetivo: "(15 + 3) * 2" -> ['(', '15', '+', '3', ')', '*', '2']
# Percorremos o texto caractere por caractere. Quando achamos um
# dígito (ou ponto), vamos juntando em "numero_atual" até acabar o
# número; só então guardamos o número inteiro como UM token.
def tokenizar(expressao):
    tokens = []
    numero_atual = ""  # acumula os caracteres do número que está sendo lido

    for c in expressao:
        if c.isdigit() or c == ".":
            numero_atual += c  # continua montando o número ("1" depois "15")
        else:
            # O caractere NÃO faz parte de um número: se havia um número
            # sendo montado, ele terminou aqui. Guardamos e zeramos.
            if numero_atual != "":
                validar_numero(numero_atual)
                tokens.append(numero_atual)
                numero_atual = ""

            if c == " ":
                continue  # espaços são opcionais: simplesmente ignoramos
            elif c in OPERADORES or c in "()":
                tokens.append(c)
            else:
                raise ValueError(f"caractere não aceito: '{c}'")

    # Se a expressão terminou com um número ("8 + 4"), ele ainda está
    # no acumulador e precisa ser guardado.
    if numero_atual != "":
        validar_numero(numero_atual)
        tokens.append(numero_atual)

    return tokens


def validar_numero(texto):
    # Impede números malformados como "1.2.3" ou "." sozinho.
    if texto.count(".") > 1 or texto == ".":
        raise ValueError(f"número inválido: '{texto}'")


# ---------------------------------------------------------------------
# SEÇÃO 6 e 7: PRECEDÊNCIA E INFIXA -> PÓS-FIXA
# ---------------------------------------------------------------------
# Quanto maior o número, maior a prioridade.
def precedencia(operador):
    if operador in ("*", "/"):
        return 2
    if operador in ("+", "-"):
        return 1
    return 0  # "(" nunca deve ser "desempilhado" por um operador


# Algoritmo (as 5 regras do PDF):
#   1) Número            -> vai direto para a saída.
#   2) "("               -> entra na pilha.
#   3) ")"               -> desempilha operadores para a saída até achar "(".
#   4) Operador          -> antes de empilhar, desempilha os operadores do
#                           topo que têm prioridade MAIOR OU IGUAL à dele.
#                           (o "igual" faz 8-4-2 virar (8-4)-2, da esquerda
#                           para a direita)
#   5) Fim dos tokens    -> desempilha tudo que sobrou.
def para_posfixa(tokens):
    saida = []
    pilha = []  # em Python, uma lista com append/pop funciona como pilha

    for t in tokens:
        if t == "(":
            pilha.append(t)

        elif t == ")":
            # tira operadores até chegar no "(" correspondente
            while pilha and pilha[-1] != "(":
                saida.append(pilha.pop())
            if not pilha:  # esvaziou sem achar "(" -> ")" sobrando
                raise ValueError("parênteses incompatíveis: ')' sem '('")
            pilha.pop()  # descarta o "(" (parênteses não vão para a saída)

        elif t in OPERADORES:
            while pilha and pilha[-1] != "(" and \
                    precedencia(pilha[-1]) >= precedencia(t):
                saida.append(pilha.pop())
            pilha.append(t)

        else:  # é um número
            saida.append(t)

    # transfere o que restou na pilha
    while pilha:
        topo = pilha.pop()
        if topo == "(":  # sobrou "(" sem ")" correspondente
            raise ValueError("parênteses incompatíveis: '(' sem ')'")
        saida.append(topo)

    return saida


# ---------------------------------------------------------------------
# SEÇÃO 8: CONSTRUIR A ÁRVORE A PARTIR DA PÓS-FIXA
# ---------------------------------------------------------------------
# Lemos a pós-fixa da esquerda para a direita com uma pilha de NÓS:
#   - número   : cria um nó (folha) e empilha.
#   - operador : desempilha 2 nós. O PRIMEIRO pop é o filho DIREITO,
#                o SEGUNDO é o ESQUERDO (ordem essencial para - e /).
#                Cria o nó do operador, liga os filhos e empilha de volta.
# No final, sobra exatamente 1 nó na pilha: a raiz.
def construir_arvore(posfixa):
    if not posfixa:
        raise ValueError("expressão vazia")

    pilha = []
    for t in posfixa:
        if t in OPERADORES:
            if len(pilha) < 2:  # faltam operandos, ex.: "8 +"
                raise ValueError("expressão inválida: operador sem operandos")
            no = No(t)
            no.direita = pilha.pop()   # 1º pop = direito
            no.esquerda = pilha.pop()  # 2º pop = esquerdo
            pilha.append(no)
        else:
            pilha.append(No(t))

    if len(pilha) != 1:  # sobrou mais de um nó, ex.: "8 4" (faltou operador)
        raise ValueError("expressão inválida: operandos sem operador")

    return pilha[0]


# ---------------------------------------------------------------------
# SEÇÃO 9: PERCURSOS (recursivos)
# ---------------------------------------------------------------------
# Cada função devolve uma LISTA de valores na ordem em que visitou os nós.
#
# RELAÇÃO COM AS NOTAÇÕES:
#   pré-ordem  (raiz, esq, dir) -> notação PREFIXA   (+ 8 * 4 2)
#   em ordem   (esq, raiz, dir) -> notação INFIXA    (8 + 4 * 2)
#                                  (sem parênteses; a ordem fica certa,
#                                   mas a hierarquia fica ambígua)
#   pós-ordem  (esq, dir, raiz) -> notação PÓS-FIXA  (8 4 2 * +)
#
# Caso base: nó vazio (None) -> lista vazia. A recursão para aí.
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


# ---------------------------------------------------------------------
# SEÇÃO 10: RECONSTRUIR A EXPRESSÃO A PARTIR DA ÁRVORE
# ---------------------------------------------------------------------
# Folha: devolve o número. Operador: junta  "(" esquerda op direita ")".
# Os parênteses em todo nó interno deixam a estrutura da árvore explícita.
def gerar_expressao(no):
    if eh_folha(no):
        return no.valor
    esq = gerar_expressao(no.esquerda)
    dir_ = gerar_expressao(no.direita)
    return "(" + esq + " " + no.valor + " " + dir_ + ")"


# ---------------------------------------------------------------------
# SEÇÃO 11: CALCULAR PELA ÁRVORE
# ---------------------------------------------------------------------
def calcular(no):
    # 1) folha: converte o texto para número e devolve
    if eh_folha(no):
        return float(no.valor)

    # 2) e 3) calcula recursivamente os dois lados
    a = calcular(no.esquerda)
    b = calcular(no.direita)

    # 4) aplica o operador do nó
    if no.valor == "+":
        return a + b
    if no.valor == "-":
        return a - b
    if no.valor == "*":
        return a * b
    if no.valor == "/":
        if b == 0:
            raise ZeroDivisionError("divisão por zero")
        return a / b


def formatar_resultado(n):
    # 42.0 aparece como 42; 22.5 continua 22.5
    if n == int(n):
        return str(int(n))
    return str(round(n, 10))


# ---------------------------------------------------------------------
# EXTRA (desafio opcional): mostrar a árvore deitada no terminal
# ---------------------------------------------------------------------
def mostrar_arvore(no, nivel=0):
    if no is None:
        return
    mostrar_arvore(no.direita, nivel + 1)
    print("    " * nivel + no.valor)
    mostrar_arvore(no.esquerda, nivel + 1)


# ---------------------------------------------------------------------
# SEÇÃO 12: SAÍDA DO PROGRAMA
# ---------------------------------------------------------------------
def processar(expressao):
    """Executa todo o pipeline e imprime cada etapa."""
    if expressao.strip() == "":
        raise ValueError("expressão vazia")

    tokens = tokenizar(expressao)
    posfixa = para_posfixa(tokens)
    raiz = construir_arvore(posfixa)

    print("Tokens:           ", tokens)
    print("Pós-fixa:         ", " ".join(posfixa))
    print("Pré-ordem:        ", " ".join(pre_ordem(raiz)))
    print("Em ordem:         ", " ".join(em_ordem(raiz)))
    print("Pós-ordem:        ", " ".join(pos_ordem(raiz)))
    print("Expr. reconstruída:", gerar_expressao(raiz))
    print("Árvore:")
    mostrar_arvore(raiz)
    resultado = calcular(raiz)
    print("Resultado:        ", formatar_resultado(resultado))
    return resultado


# ---------------------------------------------------------------------
# SEÇÃO 13 e 14: TESTES OBRIGATÓRIOS E VALIDAÇÃO
# ---------------------------------------------------------------------
def calcular_texto(expressao):
    # atalho sem prints, usado nos testes
    return calcular(construir_arvore(para_posfixa(tokenizar(expressao))))


def executar_testes():
    casos = [
        ("8 + 4 * 2", 16),
        ("(8 + 4) * 2", 24),
        ("((15 - 3) / 4) + (2 * 5)", 13),
        ("((20 / 5) + 3) * (9 - (2 + 1))", 42),
        ("12.5 + 2.5 * 4", 22.5),
    ]
    for expr, esperado in casos:
        obtido = calcular_texto(expr)
        status = "OK" if abs(obtido - esperado) < 1e-9 else "FALHOU"
        print(f"[{status}] {expr} = {formatar_resultado(obtido)} "
              f"(esperado {esperado})")

    # Testes de erro: cada um DEVE levantar uma exceção.
    invalidos = ["8 / 0", "(8 + 4", "8 + 4)", "", "   ", "8 + a", "8 +", "8 4",
                 "1.2.3 + 1"]
    for expr in invalidos:
        try:
            calcular_texto(expr) if expr.strip() else processar(expr)
            print(f"[FALHOU] '{expr}' deveria dar erro")
        except (ValueError, ZeroDivisionError) as e:
            print(f"[OK] '{expr}' -> erro tratado: {e}")


# ---------------------------------------------------------------------
# PROGRAMA PRINCIPAL (permite várias expressões sem reiniciar)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("Calculadora de expressões com árvore binária")
    print("Digite uma expressão, 'testes' para rodar os testes ou 'sair'.")
    while True:
        entrada = input("\nDigite uma expressão: ")
        if entrada.strip().lower() == "sair":
            break
        if entrada.strip().lower() == "testes":
            executar_testes()
            continue
        try:
            processar(entrada)
        except (ValueError, ZeroDivisionError) as e:
            print("Erro:", e)


# =====================================================================
# SEÇÃO 15: QUESTÕES DE ANÁLISE
# (revise e reescreva com suas palavras antes de entregar)
# =====================================================================
# 1) Por que tokenizar?
#    O texto é só uma sequência de caracteres. A tokenização agrupa
#    esses caracteres em unidades com significado (números com vários
#    algarismos, operadores, parênteses). Sem ela, "15" seria lido como
#    '1' e '5' separados. Também é nela que descartamos espaços e
#    detectamos caracteres inválidos.
#
# 2) Por que uma pilha para operadores e parênteses?
#    Pilha é LIFO: o último a entrar é o primeiro a sair. O último "("
#    aberto é o primeiro a ser fechado, e o operador empilhado mais
#    recentemente é o primeiro a ser comparado/desempilhado. Isso
#    reproduz o aninhamento dos parênteses e a ordem de precedência.
#
# 3) Por que o primeiro pop é o filho direito?
#    Na pós-fixa o operador vem depois dos operandos: "a b op". O
#    operando b foi empilhado por último, portanto está no topo e sai
#    primeiro. Assim, b é o direito e a é o esquerdo. Inverter trocaria
#    "a - b" por "b - a" (o mesmo vale para a divisão).
#
# 4) Relação entre pós-ordem e pós-fixa:
#    A pós-ordem visita esquerda, direita e só depois a raiz. Para a
#    árvore de expressão isso produz operando, operando, operador, que
#    é exatamente a notação pós-fixa.
#
# 5) Complexidade de calcular uma árvore de n nós:
#    O(n). Cada nó é visitado exatamente uma vez e o trabalho feito em
#    cada visita (uma comparação e uma operação aritmética) é constante.
#
# 6) O que determina o máximo de chamadas recursivas simultâneas?
#    A ALTURA h da árvore. Em cada momento, as chamadas ativas formam
#    um caminho da raiz até o nó atual, então no máximo h+1 chamadas
#    estão empilhadas. Árvore balanceada: h ~ log n. Pior caso (árvore
#    em "fila", ex.: 1+(2+(3+...))): h ~ n, e o Python pode estourar o
#    limite de recursão (cerca de 1000 chamadas).
# =====================================================================