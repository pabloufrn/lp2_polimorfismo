import math
class AreaCalculavel:
    def calcular_area(self):
        pass

class Quadrado(AreaCalculavel):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado**2

class Retangulo(AreaCalculavel):
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.largura * self.altura

class Circulo(AreaCalculavel):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio**2

if(__name__ == "__main__"):
    quadrado = Quadrado(3)
    print(f"Area de quadrado com lado 3: {quadrado.calcular_area()}")

    retangulo = Retangulo(3, 10)
    print(f"Area do retangulo com altura 3 e largura 10: {retangulo.calcular_area()}")

    circulo = Circulo(3)
    print(f"Area do circulo com raio 3: {circulo.calcular_area()}")
