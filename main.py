import pymysql.cursors
import  menu as menu
import classes as c

funcoes = list()
funcionario = list()

def cadastrarFuncao():
    nome_funcao = input("\nNOME: ")
    cod_funcao = input("\nCÓDIGO: ")
    

def cadastrarFuncionario():
    cpf = input("\nCPF: ")
    nome = input("NOME: ")
    funcao = int(input("FUNÇÃO: "))
    salario = float(input("SALÁRIO: "))
    telefone = input("TELEFONE: ")

#def pesquisarFuncionario(cpf):
#    with connection.cursor() as c:
#        sql = "SELECT * FROM funcionario WHERE cpf = %s"
#        c.execute(sql, cpf)
#        res_one = c.fetchone()
#        print(res_one)
#

while True:
    menu.menuInicial()
    opcao = int(input())
    
    if opcao == 0:
        break

    elif opcao == 1:
        if len(funcoes) == 0: # Caso não haja função cadastrada
            menu.menuManterFuncao_I()
            opcao_I = int(input())

            while True:
                if opcao_I == 0:
                    break
                elif opcao_I == 1:
                    #cadastrarFuncao()
                    pass
                else:
                    print("\nOpção inválida!\n")

        else:
            menu.menuManterFuncao_II()
            opcao_I = int(input())

            while True:
                if opcao_I == 0:
                    break
                elif opcao_I == 1:
                    pass
                elif opcao_I == 2:
                    pass
                elif opcao_I == 3:
                    pass
                elif opcao_I == 4:
                    pass
                else:
                    print("\nOpção inválida!\n")

    elif opcao == 2:
        if len(funcionario) == 0: # Caso não haja funcionário cadastrado
            menu.menuManterFuncionario_I()
            opcao_II = int(input())

            while True:
                if opcao_II == 0:
                    break
                elif opcao_II == 1:
                    pass
                else:
                    print("\nOpção inválida!\n")
        else:
            menu.menuManterFuncionario_II()
            opcao_II = int(input())

            while True:
                if opcao_II == 0:
                    break
                elif opcao_II == 1:
                    pass
                elif opcao_II == 2:
                    pass
                elif opcao_II == 3:
                    pass
                elif opcao_II == 4:
                    pass
                else:
                    print("\nOpção inválida!\n")

    else:
        print("Opção inválida!\n")

#print(funcoes)
#connection.close()