#La máquina genera un número aleatorio entre el 1 al 100 
#Tendrás que adivinar que número es.
from random import *

#Creamos una funcion para generar un número aleatorio
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

#Invocamos nuestra funcion y le decimos el rango que queremos del 1 al 100 
numeroBuscado = generarNumeroAleatorio(1, 100)

encontrado = False
intentos = 0

#Con el bucle While se va a estar ejecutando hasta que adivines el número
#La máquina te irá dando pistas y llevará la cuenta de los intentos que has necesitado
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
