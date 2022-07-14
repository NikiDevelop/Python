#Creamos una aplicación para saber cuantas veces se repite un número
numeros = (5,1,4,5,6,7,3,4)

numero = int(input("Dame un número: "))
contador = numeros.count(numero)

print(f"El número {numero} se repite {contador} ")
