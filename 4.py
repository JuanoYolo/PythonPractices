from sys import stdin

palabra = stdin.readline().strip()

cont = 0
for i in palabra:
    if i == " ":
        cont += 1

print("La cantidad de palabras es: " + str(cont+1))
