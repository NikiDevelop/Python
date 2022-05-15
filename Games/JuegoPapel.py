import random
# 1 = Papel
# 2 = Piedra
# 3 = Tijera
#Pedimos al usuario que elija entre piedra, papel o tijera
num = input("Escoge: Piedra, Papel o  Tijera: ").lower()

#Creamos un numero aleatorio entre 1 y 3
ale = random.randrange(1, 4)

#Le asignamos a cada numero un valor mediante la variable game
if ale == 1:
    game = "Papel".lower()
elif ale == 2:
    game = "Piedra".lower()
elif ale == 3 :
    game = "Tijera".lower()
else:
    print("Error!")

#Creamos una condicional para cada caso dado
for i in range(3):

            if  num == "papel" and game == "papel":
                print(f"Maquina: {game}".capitalize())
                print("¡Empate!")
                break
            elif  num == "papel" and game == "piedra" :
                print(f"Maquina: {game.capitalize()}")
                print("¡Has ganado!")
                break
            elif num == "papel" and game == "tijera":
                print(f"Maquina: {game.capitalize()}")
                print("¡Has perdido!")
                break
            if num == "piedra" and game == "papel":
                print(f"Maquina: {game.capitalize()}")
                print("¡Has perdido!")
                break
            elif num == "piedra" and game == "piedra":
                print(f"Maquina: {game.capitalize()}")
                print("¡Empate!")
                break
            elif num == "piedra" and game == "tijera":
                print(f"Maquina: {game.capitalize()}")
                print("¡Has ganado!")
                break
            if num == "tijera" and game == "papel":
                print(f"Maquina: {game.capitalize()}")
                print("¡Has ganado!")
                break
            elif num == "tijera" and game  == "piedra":
                print(f"Maquina: {game.capitalize()}")
                print("¡Has perdido!")
                break
            elif num == "tijera" and game == "tijera":
                print(f"Maquina: {game.capitalize()}")
                print("¡Empate!")
                break
            else:
                print("Error2")
                break
