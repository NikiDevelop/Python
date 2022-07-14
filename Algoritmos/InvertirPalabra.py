cadena = "Python"
palabra = "Java"

for i in range(len(cadena)-1, -1,-1):
    print(cadena[i], end="")

print()

print(palabra[::-1])