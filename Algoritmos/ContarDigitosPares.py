#Aquí vamos a saber en número cuantos dígitos pares hay
#Por ejemplo: 2213 -> hay dos números pares
def numeroPar(cadena):

    contador = 0
    for i in cadena:
        digito = int (i)
        #Si el número dividido entre 2 da 0 quiere decir que es par
        if digito % 2 == 0:
            #Incrementamos contador
            contador = contador +1
    return contador

num = int(input("Introduce un número: "))
cadena = str(num)
print("El número de digitos pares es de: ",numeroPar(cadena))
