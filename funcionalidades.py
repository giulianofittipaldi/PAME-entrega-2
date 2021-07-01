import classes

def cadastroMateria(lista, nome, codigo):
    lista.append(classes.Materia(nome, codigo))
    
def cadastroProfessor(lista, nome, departamento):
    lista.append(classes.Professor(nome, departamento))

def cadastroAluno(lista, nome, dre, periodo):
    lista.append(classes.Aluno(nome, dre, periodo))

def cadastroTurma(lista, nome):
    lista.append(classes.Turma(nome))

def DesignaProfessor(lista, nome_turma, nome_professor):
    for i in range(len(lista)):
        if(nome_turma == lista[i].nome):
            lista[i].DesProfessor(nome_professor)

def printLista(lista):
    for i in range (len(lista)):
        print(f'\n{lista[i]}\n')


    