import pymysql.cursors

connection = pymysql.connect(host='localhost', user='root', 
                            password='admin', database='prova03', 
                            charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor) 





class Funcao:
    def __init__(self, nome: str, codigo: str) -> None:
        self.nome = nome
        self.cod = codigo
        with connection.cursor() as c:
            sql = "INSERT INTO funcao (cod, nome) VALUES (%s, %s)"
            c.execute(sql, (codigo, nome))
        connection.commit()


class Funcionario:
    def __init__(self, nome: str , cpf: str, funcao: Funcao, salario: float, telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

        with connection.cursor() as c:
            sql = "INSERT INTO funcionario (cpf, nome, funcao, salario, telefone) VALUES(%s, %s, %d, %f, %s)"
            c.execute(sql, (cpf, nome, funcao, salario, telefone))
        connection.commit()
connection.close()