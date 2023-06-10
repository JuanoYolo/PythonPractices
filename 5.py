from sys import stdin

palabra = stdin.readline().strip()

lis = []
lis1 = []

for i in palabra:
    lis.append(i)
    lis1.append(i)

lis.reverse()
if lis1 == lis:
    print("Es un palíndromo")

else:
    print("No es un palíndromo")
