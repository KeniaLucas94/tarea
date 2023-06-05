import math

from Figura_geometrica import  FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, ancho:float=0.0, alto:float=0.0):
        super().__init__(ancho= ancho, alto=alto)


    def __str__(self):
        return f'Triangulo [alto = {self.alto}, ancho = {self.ancho}]'

    def calcular_area(self):
        return (self.alto * self.ancho) / 2

    def calcular_perimetro(self):
        return 3 * self.alto

if __name__ == '__main__':
    tri1 = Triangulo( ancho=4, alto=6)
    print(tri1)
    print(f'El área del Triangulo es: {tri1.calcular_area()}')
    print(f'El perimetro del Triangulo es: {tri1.calcular_perimetro()}')
