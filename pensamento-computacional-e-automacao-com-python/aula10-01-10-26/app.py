from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("João", "123456", "Ciência da Computação")
# print(aluno.notas_por_disciplina)

# criar / instanciar 2 disciplina
dsa = Disciplina("Data Structures", "Alvaro")
model_lin = Disciplina("Modelagem Linear", "Rodolfo")
# print(model_lin.professor)
# model_lin.exibir_info()

# matricular o aluno nas disciplinas
aluno1.matricular(dsa)
aluno1.matricular(model_lin)
# print(aluno1.disciplinas[1].professor)
