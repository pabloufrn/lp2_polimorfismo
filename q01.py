class Viajante:
    def dizerOla(self):
        pass

class Brasileiro(Viajante):
    def dizerOla(self):
        print('Ola!')

class Espanhol(Viajante):
    def dizerOla(self):
        print('Hola!')

class Americano(Viajante):
    def dizerOla(self):
        print('Hello!')

class TestandoNacionalidade:
    def __init__(self):
        self.v1 = Brasileiro()
        self.v2 = Americano()
        self.v3 = Espanhol()
    def main(self):
        self.v1.dizerOla()
        self.v2.dizerOla()
        self.v3.dizerOla()

if(__name__ == '__main__'):
    teste = TestandoNacionalidade()
    teste.main()
