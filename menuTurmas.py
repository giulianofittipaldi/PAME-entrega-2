import funcionalidades

ListaTurmas = []

def menu_Turma():
    opcaoMenuTurma = 0
    while(opcaoMenuTurma != 8):
        print("\nMenu de Turmas \n")
        print("Selecione a opção desejada")
        print("Aperte 1 para cadastrar uma nova turma")
        print("Aperte 2 designar um professor para uma turma")
        print("Aperte 3 para adicionar alunos em uma turma")
        print("Aperte 4 para remover alunos em uma turma")
        print("Aperte 5 para dar nota final aos alunos de uma turma")
        print("Aperte 6 para Mostrar todos os alunos de uma turma")
        print("Aperte 7 Mostras todas as turmas cadastradas")
        print("Aperte 8 para voltar ao menu principal")
        opcaoMenuTurma = int(input())

        if (opcaoMenuTurma == 1):
            nome_Turma = input("Qual o nome da nova turma? ")
            funcionalidades.cadastroTurma(ListaTurmas, nome_Turma)

        elif (opcaoMenuTurma == 2):
            nome_Turma = input("Qual o nome da turma? ")
            nome_Professor = input("Qual o nome do professor? ")
            funcionalidades.DesignaProfessor(ListaTurmas, nome_Turma, nome_Professor)

        #elif (opcao == 3):
            #nome_Aluno = input("Qual o nome do aluno?")
            #funcionalidades.
            
        
        #elif (opcao == 4):
            #funcionalidades.

        #elif (opcao == 5):
            #funcionalidades.

        #elif (opcao == 6):
            #funcionalidades.

        elif (opcaoMenuTurma == 7):
            funcionalidades.printLista(ListaTurmas)
    return