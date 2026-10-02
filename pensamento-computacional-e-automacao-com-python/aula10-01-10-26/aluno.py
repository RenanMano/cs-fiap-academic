from disciplina import Disciplina
class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplina = {}

    def matricular(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        self.notas_por_disciplina