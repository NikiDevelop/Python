'''
Palindromo es cuando se puede leer igual una palabra de izquierda a derecha y de derecha a izquierda
Por ejemplo: ana -> si es palindromo
rosa -> no es palindromo
Vamos a crear una aplicación para que nos diga si una palabra es palindromo
La idea es darle la vuelta a la palabra y comprobar si es o no palindromo
'''
palabra = input("Escribe una palabra: ")

palabra_al_reves = palabra[::-1]
print(palabra_al_reves)

if(palabra == palabra_al_reves):
    print("Es palindromo")
else:
    print("No es palindromo")
