class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = nome

    def __str__(self):
        return '''
        ---------
        nome: {}
        endereco: {}
        telefone: {}
        '''.format(self.nome, self.endereco, self.telefone)
class PessoaFisica(Pessoa):
    def __init__(self, nome, endereco, telefone, cpf):
        super(type(self), self).__init__(nome, endereco, telefone)
        self.cpf = cpf
    def __str__(self):
        return super(type(self), self).__str__() + '''
        cpf: {}
        ---------'''.format(self.cpf)

class PessoaJuridica(Pessoa):
    def __init__(self, nome, endereco, telefone, cnpj, fantasia):
        super(type(self), self).__init__(nome, endereco, telefone)
        self.cnpj = cnpj
        self.fantasia = fantasia
    def __str__(self):
        return super(type(self), self).__str__() + '''
        cnpj: {}
        nome fantasia: {}
        ---------'''.format(self.fantasia)

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
    def __str__(self):
        return 
        '''Pessoas fisicas: {qtd_fisicas}
        Pessoas juridicas: {qtd_juridicas}
        Total de pessoas: {qtd_fisicas}
        Clientes:\n {}'''.format(qtd_fisicas, qtd_juridicas, qtd_fisicas + qtd_juridicas)

if(__name__ == "__main__"):
    Pablo = PessoaFisica("Pablo", "Rua de Pablo", "4002 8922", "000.000.000-00")
    Leonardo = PessoaJuridica("Leonardo", "Rua do Python", "4349987377", "000.000/321", "Python World")

    emp = Empresa()
    emp.cadastrar(Pablo)
    emp.cadastrar(Leonardo)

    print(emp)

