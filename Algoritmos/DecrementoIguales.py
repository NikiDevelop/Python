def iguales(a, b):
    while a > 0 and b > 0:

        if  (a - b and a > 0):
            a = a - 1
            b = b - 1

            return a
    return b

resultado = iguales(20, 19)
print(resultado)
