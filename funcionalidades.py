import classes

def cadastroMateria(lista, nome):
    lista.append(classes.Materia(nome))
    
def cadastroProfessor(lista, nome):
    lista.append(classes.Professor(nome))

def cadastroAluno(lista, nome):
    lista.append(classes.Aluno(nome))

def printLista(lista):
    for i in range (len(lista)):
        print(f'\n{lista[i]}\n')


    