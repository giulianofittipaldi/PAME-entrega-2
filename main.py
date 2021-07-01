import funcionalidades
import classes

ListaMaterias = []
ListaProfessores = []
ListaAlunos = []
ListaTurmas = []
opcao = 0
while(opcao != 8):
    
    print("Selecione a opção desejada")
    print("Aperte 1 para cadastrar uma nova materia")
    print("Aperte 2 para cadastrar um novo professor")
    print("Aperte 3 para cadastrar uma nova aluno")
    print("Aperte 4 para mostrar todas as materias cadastradas")
    print("Aperte 5 para mostrar todos os professores cadastradas")
    print("Aperte 6 para mostrar todos os alunos cadastrados")
    print("Aperte 7 para abrir o Menu de Turmas")
    print("Aperte 8 para Sair do programa")
    opcao = int(input())
    if (opcao == 1):
        nome_Materia = input("Qual o nome da matéria?")
        funcionalidades.cadastroMateria(ListaMaterias,nome_Materia)
    
    elif (opcao == 2):
        nome_Professor = input("Qual o nome do professor?")
        funcionalidades.cadastroProfessor(ListaProfessores,nome_Professor)
    
    elif (opcao == 3):
        nome_Aluno = input("Qual o nome do aluno?")
        funcionalidades.cadastroAluno(ListaAlunos,nome_Aluno)
        
    
    elif (opcao == 4):
        funcionalidades.printLista(ListaMaterias)

    elif (opcao == 5):
        funcionalidades.printLista(ListaProfessores)

    elif (opcao == 6):
        funcionalidades.printLista(ListaAlunos)

    #elif (opcao == 7):
