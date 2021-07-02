from funcionalidades import *
from Listas import ListaTurmas, ListaAlunos, ListaMaterias, ListaProfessores


def menu_Turma():
    opcaoMenuTurma = 0
    while(opcaoMenuTurma != 8):
        print('\nMenu de Turmas \n')
        print('Selecione a opção desejada')
        print('Aperte 1 para cadastrar uma nova turma')
        print('Aperte 2 designar um professor para uma turma')
        print('Aperte 3 para adicionar alunos em uma turma')
        print('Aperte 4 para remover alunos em uma turma')
        print('Aperte 5 para dar nota final aos alunos de uma turma')
        print('Aperte 6 para Mostrar todos os alunos de uma turma')
        print('Aperte 7 Mostrar todas as turmas cadastradas')
        print('Aperte 8 para voltar ao menu principal\n')
        opcaoMenuTurma = int(input())

        if (opcaoMenuTurma == 1):
            nome_Turma = input('Qual o nome da nova turma? ')
            nome_Materia = input('Qual a matéria da nova turma? ')
            if VerificaVazio(nome_Turma) or VerificaVazio(nome_Materia):
                print('Um dos nomes não foi informado, verifique a opção e selecione novamente')
            else:
                cadastroTurma(ListaTurmas, nome_Turma)
                materia = ProcuraLista(ListaMaterias, nome_Materia)
                if not materia:
                    print('\nA matéria não foi cadastrada\n')
                else:
                    turma = ProcuraLista(ListaTurmas, nome_Turma)
                    turma.AddMateria(materia)

        elif (opcaoMenuTurma == 2):
            nome_Turma = input('Qual o nome da turma? ')
            nome_Professor = input('Qual o nome do professor? ')
            if VerificaVazio(nome_Turma) or VerificaVazio(nome_Professor):
                print('Um dos nomes não foi informado, verifique a opção e selecione novamente')
            else:
                turma = ProcuraLista(ListaTurmas, nome_Turma)
                professor = ProcuraLista(ListaProfessores, nome_Professor)
                if not turma:
                    print('Turma não cadastrada\n')
                else:
                    if not professor:
                        print('O professor não é cadastrado\n')
                    else:
                        DesignaProfessor(ListaTurmas, nome_Turma, nome_Professor)

        elif (opcaoMenuTurma == 3):
            nome_Turma = input('Qual o nome da turma? ')
            nome_Aluno = input('Qual o nome do aluno? ')
            if VerificaVazio(nome_Turma) or VerificaVazio(nome_Aluno):
                print('Um dos nomes não foi informado, verifique a opção e selecione novamente')
            else:
                turma = ProcuraLista(ListaTurmas, nome_Turma)
                aluno = ProcuraLista(ListaAlunos, nome_Aluno)
                if not turma:
                    print('Turma não cadastrada\n')
                else:
                    if not aluno:
                        print('Aluno não cadastrado\n')
                    else:
                        turma.AddAluno(aluno)
            

        elif (opcaoMenuTurma == 4):
            nome_Turma = input('Qual o nome da turma? ')
            nome_Aluno = input('Qual o nome do aluno? ')
            if VerificaVazio(nome_Turma) or VerificaVazio(nome_Aluno):
                print('Um dos nomes não foi informado, verifique a opção e selecione novamente')
            else:
                turma = ProcuraLista(ListaTurmas, nome_Turma)
                aluno = ProcuraLista(ListaAlunos, nome_Aluno)
                if not turma:
                    print('Turma não cadastrada\n')
                else:
                    if not aluno:
                        print('Aluno não cadastrado\n')
                    else:
                        turma.RemvAluno(aluno)

        elif (opcaoMenuTurma == 5):
            nome_Turma = input('Qual o nome da turma? ')
            nome_Aluno = input('Qual o nome do aluno? ')
            nota = input('Qual a nota do aluno? ')
            if VerificaVazio(nome_Turma) or VerificaVazio(nome_Aluno) or VerificaVazio(nota):
                print('Um dos nomes não foi informado, verifique a opção e selecione novamente')
            else:
                turma = ProcuraLista(ListaTurmas, nome_Turma)
                aluno = ProcuraLista(ListaAlunos, nome_Aluno)
                if not turma:
                    print('Turma não cadastrada\n')
                else:
                    if not aluno:
                        print('Aluno não cadastrado\n')
                    else:
                        

                        if nota < 0 or (not VerificaInteiro(nota)):
                            print('Nota não é valida, deve ser um numero real e positivo\n')
                        else:
                            float(nota)
                            aluno.AddNota(nota)
                        
                

        elif (opcaoMenuTurma == 6):
            nome_Turma = input('Qual o nome da turma? ')
            if VerificaVazio(nome_Turma) or VerificaVazio(nome_Materia):
                print('Um dos nomes não foi informado, verifique a opção e selecione novamente')
            else:
                if not turma:
                    print('Turma não cadastrada\n')
                else:
                    turma = ProcuraLista(ListaTurmas, nome_Turma)
                    turma.listaAlunosTurma.sort(key=lambda x: x.nome)
                    printLista(turma.listaAlunosTurma)


        elif (opcaoMenuTurma == 7):
            ListaTurmas.sort(key=lambda x: len(x.listaAlunosTurma), reverse=True)
            printLista(ListaTurmas)
    return