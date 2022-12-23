class Funcao:
    def __init__(self, nome: str, codigo: str) -> None:
        self.nome = nome
        self.codigo = codigo

    def inserir_funcao(self, connection):
        with connection.cursor() as c:
            sql = """INSERT INTO funcao (cod, nome) VALUES (%s, %s)"""
            c.execute(sql, (self.codigo, self.nome))
            connection.commit()
            print('Função inserida com sucesso')

    def editar_funcao(self, connection):
        with connection.cursor() as c:
            sql = """UPDATE funcao set nome = %s where cod = %s"""
            c.execute(sql, (self.nome, self.codigo))
            connection.commit()
            print('Função alterada com sucesso')

    def deletar_funcao(self, connection):
        with connection.cursor() as c:
            sql = """DELETE FROM funcao WHERE cod = %s"""
            c.execute(sql, (self.codigo))
            connection.commit()
            print('Função excluída com sucesso')

    def buscar_funcao(self, connection):
        with connection.cursor() as c:
            sql = """SELECT * FROM funcao WHERE cod = %s"""
            c.execute(sql, (self.codigo))
            rows = c.fetchall()
        return rows

    @staticmethod
    def exibir_funcoes(connection):
        with connection.cursor() as c:
            sql = """SELECT * FROM funcao"""
            c.execute(sql)
            rows = c.fetchall()
        return rows

class Funcionario:
    def __init__(self, nome: str , cpf: str, funcao: Funcao, salario: float, telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

    @staticmethod
    def exibir_funcionarios(connection):
        with connection.cursor() as c:
            sql = """SELECT * FROM funcionario"""
            c.execute(sql)
            rows = c.fetchall()
        return rows

    def inserir_funcionario(self, connection):
        with connection.cursor() as c:
            self.funcao = c.execute("SELECT id from Funcao where cod = %s", (self.funcao))
            if self.funcao:
                sql = """INSERT INTO funcionario (cpf, nome, funcao, salario, telefone) VALUES (%s, %s, %s, %s, %s)"""
                c.execute(sql, (self.cpf, self.nome, self.funcao, self.salario, self.telefone))
                connection.commit()
                print('Funcionário inserido com sucesso')
            else:
                print('Função inexistente')

    def buscar_funcionario(self, connection):
        with connection.cursor() as c:
            sql = """SELECT * FROM funcionario WHERE cpf = %s"""
            c.execute(sql, (self.cpf))
            rows = c.fetchall()
        return rows

    def editar_funcionario(self, connection):
        with connection.cursor() as c:
            self.funcao = c.execute("SELECT id from Funcao where cod = %s", (self.funcao))
            if self.funcao:
                sql = """UPDATE funcionario set nome = %s, funcao = %s, salario = %s, telefone = %s where cpf = %s"""
                c.execute(sql, (self.nome, self.funcao, self.salario, self.telefone, self.cpf))
                connection.commit()
                print('Funcionário alterado com sucesso')
            else:
                print('Função inexistente')

    def deletar_funcionario(self, connection):
        with connection.cursor() as c:
            sql = """DELETE FROM funcionario WHERE cpf = %s"""
            c.execute(sql, (self.cpf))
            connection.commit()
            print('Funcionário excluído com sucesso')
