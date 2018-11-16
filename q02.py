class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = nome

    def __str__(self):
        return f'''
            nome: {self.nome}
            endereco: {self.endereco}
            telefone: {self.telefone}'''
class PessoaFisica(Pessoa):
    def __init__(self, nome, endereco, telefone, cpf):
        super(type(self), self).__init__(nome, endereco, telefone)
        self.cpf = cpf

    def __str__(self):
        return \
        f'''{super(type(self), self).__str__()}
            cpf: {self.cpf}
        '''

    def __repr__(self):
        return str(self)

class PessoaJuridica(Pessoa):
    def __init__(self, nome, endereco, telefone, cnpj, fantasia):
        super(type(self), self).__init__(nome, endereco, telefone)
        self.cnpj = cnpj
        self.fantasia = fantasia

    def __str__(self):
        return \
        f'''{super(type(self), self).__str__()}
            cnpj: {self.cnpj}
            nome fantasia: {self.fantasia}
        '''
    def __repr__(self):
        return str(self)

class Empresa:
    qtd_fisicas = 0
    qtd_juridicas = 0
    def __init__(self):
        self.clientes = []
    def cadastrar(self, cliente):
        if(type(cliente) == PessoaJuridica):
            type(self).qtd_juridicas += 1
        else:
            type(self).qtd_fisicas += 1
        self.clientes.append(cliente)
    def __str__(self):
        return f'''\
        Pessoas fisicas: {type(self).qtd_fisicas}
        Pessoas juridicas: {type(self).qtd_juridicas}
        Total de pessoas: {type(self).qtd_fisicas + type(self).qtd_juridicas}
        Clientes:
        {self.clientes}'''

if(__name__ == "__main__"):
    primeira_pessoa = PessoaFisica("Primeira", "Rua um", "(11) 11111-1111", "010.101.010-01")
    segunda_pessoa = PessoaJuridica("Segundo", "Rua dois", "(22) 22222-2222", "222.222.222/2222-22", "Dois Tech Informática")

    emp = Empresa()
    emp.cadastrar(primeira_pessoa)
    emp.cadastrar(segunda_pessoa)

    print(emp)

