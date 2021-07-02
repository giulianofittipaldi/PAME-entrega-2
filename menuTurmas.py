import funcionalidades
from Listas import ListaTurmas, ListaAlunos


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
        print("Aperte 7 Mostrar todas as turmas cadastradas")
        print("Aperte 8 para voltar ao menu principal")
        opcaoMenuTurma = int(input())

        if (opcaoMenuTurma == 1):
            nome_Turma = input("Qual o nome da nova turma? ")
            funcionalidades.cadastroTurma(ListaTurmas, nome_Turma)

        elif (opcaoMenuTurma == 2):
            nome_Turma = input("Qual o nome da turma? ")
            nome_Professor = input("Qual o nome do professor? ")
            funcionalidades.DesignaProfessor(ListaTurmas, nome_Turma, nome_Professor)

        elif (opcaoMenuTurma == 3):
            nome_Turma = input("Qual o nome da turma? ")
            nome_Aluno = input("Qual o nome do aluno? ")
            turma = funcionalidades.ProcuraLista(ListaTurmas, nome_Turma)
            aluno = funcionalidades.ProcuraLista(ListaAlunos, nome_Aluno)
            if not turma:
                print("Turma não cadastrada")
            else:
                if not aluno:
                    print("Aluno não cadastrado")
                else:
                    turma.AddAluno(aluno)
            

        elif (opcaoMenuTurma == 4):
            nome_Turma = input("Qual o nome da turma? ")
            nome_Aluno = input("Qual o nome do aluno? ")
            turma = funcionalidades.ProcuraLista(ListaTurmas, nome_Turma)
            aluno = funcionalidades.ProcuraLista(ListaAlunos, nome_Aluno)
            if not turma:
                print("Turma não cadastrada")
            else:
                if not aluno:
                    print("Aluno não cadastrado")
                else:
                    turma.RemvAluno(aluno)

        elif (opcaoMenuTurma == 5):
            nome_Turma = input("Qual o nome da turma? ")
            nome_Aluno = input("Qual o nome do aluno? ")
            nota = int(input("Qual a nota do aluno? "))
            turma = funcionalidades.ProcuraLista(ListaTurmas, nome_Turma)
            aluno = funcionalidades.ProcuraLista(ListaAlunos, nome_Aluno)
            if not turma:
                print("Turma não cadastrada")
            else:
                if not aluno:
                    print("Aluno não cadastrado")
                else:
                    aluno.AddNota(nota)

        elif (opcaoMenuTurma == 6):
            nome_Turma = input("Qual o nome da turma? ")
            if not turma:
                print("Turma não cadastrada")
            else:
                turma = funcionalidades.ProcuraLista(ListaTurmas, nome_Turma)
                turma.listaAlunosTurma.sort(key=lambda x: x.nome)
                funcionalidades.printLista(turma.listaAlunosTurma)


        elif (opcaoMenuTurma == 7):
            ListaTurmas.sort(key=lambda x: len(x.listaAlunosTurma), reverse=True)
            funcionalidades.printLista(ListaTurmas)
    return