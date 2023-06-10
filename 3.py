from sys import stdin

#frase = stdin.readline().strip()

frase = "Hola, cómo estás?"

cont = 0
for i in frase:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "á" or i == "é" or i == "í" or i == "ó" or i == "ú" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        cont += 1

print("La cantidad de vocales es: " + str(cont))
