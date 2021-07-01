import funcionalidades
import menuTurmas
from Listas import *



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
        nome_Materia = input("Qual o nome da matéria? ")
        codigo_Materia = input("Qual o código da matéria? ")
        funcionalidades.cadastroMateria(ListaMaterias, nome_Materia, codigo_Materia)
    
    elif (opcao == 2):
        nome_Professor = input("Qual o nome do professor? ")
        departamento_professor = input("Qual seu departamento? ")
        funcionalidades.cadastroProfessor(ListaProfessores, nome_Professor, departamento_professor)
    
    elif (opcao == 3):
        nome_Aluno = input("Qual o nome do aluno? ")
        dre_Aluno = input("Qual o DRE do aluno? ")
        periodo_Aluno = input("Qual o periodo do aluno? ")
        funcionalidades.cadastroAluno(ListaAlunos, nome_Aluno, dre_Aluno, periodo_Aluno)
        
    elif (opcao == 4):
        funcionalidades.printLista(ListaMaterias)

    elif (opcao == 5):
        funcionalidades.printLista(ListaProfessores)

    elif (opcao == 6):
        funcionalidades.printLista(ListaAlunos)

    elif (opcao == 7):
        menuTurmas.menu_Turma()