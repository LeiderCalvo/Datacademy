#Reto 1 - Área de un triángulo
#El área de un triángulo se describe de la siguiente manera: A = (b * h) / 2 .
#Escribe un programa que tome la base y la altura como parámetros y calcule el área del triángulo.

from math import sqrt

def run():
    height = int(input('Please, provide a height: '))
    base = int(input('Please, provide a base: '))
    area = (base * height) / 2
    print('the triangle area is:' + str(area))

if __name__ == "__main__":
    run()
