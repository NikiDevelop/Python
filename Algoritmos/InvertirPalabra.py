#Vamos a ver 2 formas de invertir una palabra
palabra1 = "Python"
palabra2 = "Java"

#Forma 1
for i in range(len(palabra1)-1, -1,-1):
    print(palabra1[i], end="")

print()
#Forma 2
print(palabra2[::-1])
