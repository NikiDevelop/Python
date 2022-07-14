from random import *


def generarNumeroAleatorio(minimo, maximo):
    try:
        if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux

        return randint(minimo, maximo)
    except TypeError:
        print("Debes escribir números")
        return -1


numeroBuscado = generarNumeroAleatorio(1, 100)

encontrado = False
intentos = 0

while not encontrado:
    numeroUsuario = int(input("Introduce un número del 1 al 100: "))

    if numeroUsuario > numeroBuscado:
        print("¡El número que buscas es menor!")
        intentos = intentos + 1
    elif numeroUsuario < numeroBuscado:
        print("¡El número que buscas es mayor!")
        intentos = intentos + 1
    else:
        encontrado = True
        print(f"¡Has acertado el número es {numeroBuscado}! \nTe ha llevado {intentos} intentos.")
