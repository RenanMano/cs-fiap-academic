LIMITE_WIP = 2                                  # limite de trabalho em andamento

quadro = {"A fazer": ["login", "cadastro", "relatório", "dashboard"],
          "Fazendo": [], "Feito": []}

def puxar():
    """Puxa a próxima tarefa somente se houver espaço na coluna Fazendo."""
    if len(quadro["Fazendo"]) >= LIMITE_WIP:
        print("WIP cheio: termine algo antes de começar outra tarefa")
    elif quadro["A fazer"]:
        quadro["Fazendo"].append(quadro["A fazer"].pop(0))

def concluir(tarefa):
    quadro["Fazendo"].remove(tarefa)
    quadro["Feito"].append(tarefa)

puxar(); puxar(); puxar()                       # a 3ª é bloqueada pelo limite
concluir("login")
puxar()
for coluna, tarefas in quadro.items():
    print(f"{coluna:<8}: {tarefas}")
