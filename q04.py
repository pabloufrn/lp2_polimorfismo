import abc

class ContaBancaria(metaclass=abc.ABCMeta):
    def __init__(self):
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if(self._saldo  < valor):
            raise ValueError
        self._saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @abc.abstractmethod
    def calcularSaldo(self):
        pass
            
class ContaCorrente(ContaBancaria):
    def calcularSaldo(self):
        return self._saldo - self._saldo*0.1

class ContaInvestimento(ContaBancaria):
    def calcularSaldo(self):
        return self._saldo + self._saldo*0.05

if(__name__ == "__main__"):
    primeira_conta = ContaCorrente()
    primeira_conta.depositar(110)
    primeira_conta.sacar(10)
    print(primeira_conta.calcularSaldo())

    segunda_conta = ContaInvestimento()
    segunda_conta.depositar(110)
    segunda_conta.sacar(10)
    print(segunda_conta.calcularSaldo())


