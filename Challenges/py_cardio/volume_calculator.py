#Reto 4 - Calculadora de volúmenes
#Escribe un programa donde apliques las diferentes fórmulas matemáticas para calcular el volumen de un cilindro. Recuerda que la base del cilindro es un círculo y necesitarás calcular su área. Aplica las fórmulas en tu programa recibiendo datos como altura y radio.

import math

def run():
    height = int(input('Please, provide a height: '))
    radius = int(input('Please, provide a radius: '))
    volume = math.pi * (radius ** 2) * height
    print('the volume of the cylinder is: ' + str(volume))

if __name__ == "__main__":
    run()