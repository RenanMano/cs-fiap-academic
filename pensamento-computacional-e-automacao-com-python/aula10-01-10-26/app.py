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

# adicionar notas do aluno referente as disciplinas
aluno1.adicionar_nota(dsa, 10)
aluno1.adicionar_nota(dsa, 8)
aluno1.adicionar_nota(model_lin, 5)
aluno1.adicionar_nota(model_lin, 3)
print(aluno1.notas_por_disciplina)