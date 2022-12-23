import pymysql
import  menu as menu
from classes import Funcao, Funcionario

connection = pymysql.connect(host='localhost', user='root', 
                            password='masterx', database='prova03', 
                            cursorclass=pymysql.cursors.DictCursor)

def cadastrarFuncao():
    nome_funcao = input("\nNOME: ")
    cod_funcao = input("\nCÓDIGO: ")
    return nome_funcao, cod_funcao
    
def cadastrarFuncionario():
    cpf = input("\nCPF: ")
    nome = input("NOME: ")
    funcao = int(input("Digite o código da função do funcionário: "))
    salario = float(input("SALÁRIO: "))
    telefone = input("TELEFONE: ")
    return cpf, nome, funcao, salario, telefone

while True:
    menu.menuInicial()
    opcao = int(input())
    
    if opcao == 0:
        break

    elif opcao == 1:
        funcoes = Funcao.exibir_funcoes(connection)
        print(funcoes)
        if len(funcoes) == 0: # Caso não haja função cadastrada
            menu.menuManterFuncao_I()
            opcao_I = int(input())

            while True:
                if opcao_I == 0:
                    break
                elif opcao_I == 1:
                    nome, codigo = cadastrarFuncao()
                    f = Funcao(nome, codigo)
                    f.inserir_funcao(connection)
                else:
                    print("\nOpção inválida!\n")

        else:
            while True:
                menu.menuManterFuncao_II()
                opcao_I = int(input())

                if opcao_I == 0:
                    break
                elif opcao_I == 1:
                    nome, codigo = cadastrarFuncao()
                    f = Funcao(nome, codigo)
                    f.inserir_funcao(connection)
                elif opcao_I == 2:
                    cod_funcao = input("\nCÓDIGO: ")
                    f = Funcao(nome=None, codigo=cod_funcao)
                    resultado = f.buscar_funcao(connection)
                    print(resultado)
                elif opcao_I == 3:
                    cod_funcao = input("\nCÓDIGO: ")
                    nome_funcao = input("\nNOME: ")
                    f = Funcao(nome=nome_funcao, codigo=cod_funcao)
                    f.editar_funcao(connection)
                elif opcao_I == 4:
                    cod_funcao = input("\nCÓDIGO: ")
                    f = Funcao(nome=None, codigo=cod_funcao)
                    f.deletar_funcao(connection)
                else:
                    print("\nOpção inválida!\n")

    elif opcao == 2:
        funcionarios = Funcionario.exibir_funcionarios(connection)
        print(funcionarios)
        if len(funcionarios) == 0: # Caso não haja funcionário cadastrado
            while True:
                menu.menuManterFuncionario_I()
                opcao_II = int(input())
                if opcao_II == 0:
                    break
                elif opcao_II == 1:
                    cpf, nome, funcao, salario, telefone = cadastrarFuncionario()
                    f = Funcionario(nome, cpf, funcao, salario, telefone)
                    f.inserir_funcionario(connection)
                else:
                    print("\nOpção inválida!\n")
        else:
            while True:
                menu.menuManterFuncionario_II()
                opcao_II = int(input())

                if opcao_II == 0:
                    break
                elif opcao_II == 1:
                    cpf, nome, funcao, salario, telefone = cadastrarFuncionario()
                    f = Funcionario(nome, cpf, funcao, salario, telefone)
                    f.inserir_funcionario(connection)
                elif opcao_II == 2:
                    cpf = input("\nDigite o CPF: ")
                    f = Funcionario(nome=None, cpf=cpf, funcao=None, salario=None, telefone=None)
                    resultado = f.buscar_funcionario(connection)
                    print(resultado)
                elif opcao_II == 3:
                    cpf = input("\nDigite o CPF para buscar o funcionário: ")
                    nome = input("NOME: ")
                    funcao = int(input("Digite o código da função do funcionário: "))
                    salario = float(input("SALÁRIO: "))
                    telefone = input("TELEFONE: ")
                    f = Funcionario(nome, cpf, funcao, salario, telefone)
                    f.editar_funcionario(connection)
                elif opcao_II == 4:
                    cpf = input("\nDigite o CPF para excluir o funcionário: ")
                    f = Funcionario(nome=None, cpf=cpf, funcao=None, salario=None, telefone=None)
                    f.deletar_funcionario(connection)
                else:
                    print("\nOpção inválida!\n")

    else:
        print("Opção inválida!\n")
connection.close()
