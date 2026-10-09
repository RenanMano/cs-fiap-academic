class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_info(self):
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")

# temporário
model_mat = Disciplina("Modelagem matemática", "Igor")
# print(model_mat)
model_mat.exibir_info()