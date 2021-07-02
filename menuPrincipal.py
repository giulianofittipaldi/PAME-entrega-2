from funcionalidades import *
import menuTurmas
from Listas import *



opcao = 0
while(opcao != '8'):
    
    print('Selecione a opção desejada')
    print('Aperte 1 para cadastrar uma nova materia')
    print('Aperte 2 para cadastrar um novo professor')
    print('Aperte 3 para cadastrar um nova aluno')
    print('Aperte 4 para mostrar todas as materias cadastradas')
    print('Aperte 5 para mostrar todos os professores cadastradas')
    print('Aperte 6 para mostrar todos os alunos cadastrados')
    print('Aperte 7 para abrir o Menu de Turmas')
    print('Aperte 8 para Sair do programa\n')
    opcao = input()
    if (opcao == '1'):
        nome_Materia = input('Qual o nome da matéria? ')
        codigo_Materia = input('Qual o código da matéria? ')
        if VerificaVazio(codigo_Materia) or VerificaVazio(nome_Materia):
                print('\nUm dos nomes não foi informado, verifique a opção e selecione novamente\n')
        else:
            cadastroMateria(ListaMaterias, nome_Materia, codigo_Materia)
    
    elif (opcao == '2'):
        nome_Professor = input('Qual o nome do professor? ')
        departamento_professor = input('Qual seu departamento? ')
        if VerificaVazio(nome_Professor) or VerificaVazio(departamento_professor):
                print('\nUm dos nomes não foi informado, verifique a opção e selecione novamente\n')
        else:
            cadastroProfessor(ListaProfessores, nome_Professor, departamento_professor)
    
    elif (opcao == '3'):
        nome_Aluno = input('Qual o nome do aluno? ')
        dre_Aluno = input('Qual o DRE do aluno? ')
        periodo_Aluno = input('Qual o periodo do aluno? ')
        if VerificaVazio(nome_Aluno) or VerificaVazio(dre_Aluno) or VerificaVazio(periodo_Aluno):
                print('\nUm dos nomes não foi informado, verifique a opção e selecione novamente\n')
        else:
            cadastroAluno(ListaAlunos, nome_Aluno, dre_Aluno, periodo_Aluno)
        
    elif (opcao == '4'):
        printLista(ListaMaterias)

    elif (opcao == '5'):
        printLista(ListaProfessores)

    elif (opcao == '6'):
        printLista(ListaAlunos)

    elif (opcao == '7'):
        menuTurmas.menu_Turma()
    elif (not '8'):
        print('A opção não existe')