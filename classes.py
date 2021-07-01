class Materia:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
    
    def __str__(self):
        return f'Matéria: {self.nome}\nCódigo: {self.codigo}'

class Professor:
    def __init__(self, nome, departamento):
        self.nome = nome
        self.departamento = departamento
    
    def __str__(self):
        return f'Nome: {self.nome}\nDepto: {self.departamento}'

class Aluno:
    def __init__(self, nome, dre, periodo):
        self.nome = nome
        self.dre = dre
        self.periodo = periodo

    def __str__(self):
        return f'Nome: {self.nome}\nDRE: {self.dre}\nPeríodo: {self.periodo}'


class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.listaAlunosTurma = []
    
    def AddAluno(self, aluno):
        self.listaAlunosTurma.append(aluno)

    def RemvAluno(self, aluno):
        self.listaAlunosTurma.remove(aluno)

    def DesProfessor(self, professor):
        if(isinstance(professor, str)):
            self.professor = professor        

    def __str__(self):
        return f'Turma: {self.nome}\nProfessor: {self.professor}'
    
    def MostraAlunos(self):
        for aluno in self.listaAlunosTurma:
            print(aluno)


