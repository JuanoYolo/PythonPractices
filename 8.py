from sys import stdin

palabra = stdin.readline().strip().split()

lista = ""

for palabra in palabra:
    lista += palabra[::-1] + " "

print(lista.strip())
