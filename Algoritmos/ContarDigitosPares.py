def numeroPar(cadena):

    contador = 0
    for i in cadena:

        digito = int (i)
        if digito % 2 == 0:
            contador = contador +1
    return contador

num = int(input("Introduce un número: "))
cadena = str(num)
print("El número de digitos pares es de: ",numeroPar(cadena))