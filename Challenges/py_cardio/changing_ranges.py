#Reto 5 - Rangos cambiantes
#En tu programa pide al usuario ingresar 3 números: un límite inferior, un límite superior y uno de comparación.

#Si tu número de comparación se encuentra en el rango de los dos límites, imprímelo en pantalla.

#En caso de estar por debajo del inferior o arriba del superior, también muéstralo en pantalla y pide ingresar otro número para repetir el proceso.

def run():
    print("Hi 👋🏻,")
    min_limit = int(input('Please, provide a min number: '))
    max_limit = int(input('Please, provide a max number: '))

    comparator = ""

    while comparator not in range(min_limit, max_limit):
        comparator = int(input('Please, provide number to compare them: '))
        print(comparator)


if __name__ == "__main__":
    run()
