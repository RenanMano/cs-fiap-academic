class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_informacoes(self):
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")


class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []                 # composição: o aluno "tem" disciplinas
        self.notas_por_disciplina = {}        # nome da disciplina -> [notas]

    def matricular(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina, nota):
        if disciplina.nome not in self.notas_por_disciplina:
            self.matricular(disciplina)       # versão dos slides: matricula se preciso
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def media_em(self, disciplina):
        notas = self.notas_por_disciplina.get(disciplina.nome, [])
        return sum(notas) / len(notas) if notas else 0.0

    def media_geral(self):
        medias = [self.media_em(d) for d in self.disciplinas if self.notas_por_disciplina.get(d.nome)]
        return sum(medias) / len(medias) if medias else 0.0

    def exibir_boletim(self):
        print(f"Aluno: {self.nome} | Matrícula: {self.matricula} | Curso: {self.curso}")
        for d in self.disciplinas:
            d.exibir_informacoes()
            print(f"  Notas: {self.notas_por_disciplina[d.nome]} | Média: {self.media_em(d):.1f}")
        print(f"MÉDIA GERAL: {self.media_geral():.1f}")


aluno1 = Aluno("João Silva", "2025001", "Ciência da Computação")
mat = Disciplina("Matemática", "Prof. Carlos")
fis = Disciplina("Física", "Prof. Ana")
aluno1.matricular(mat)
aluno1.adicionar_nota(mat, 8.0)
aluno1.adicionar_nota(mat, 7.0)
aluno1.adicionar_nota(fis, 9.0)              # Física é matriculada automaticamente
aluno1.adicionar_nota(fis, 8.0)
aluno1.exibir_boletim()
