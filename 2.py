from sys import stdin

print("Base: ")
base = float(stdin.readline())
print("Altura: ")
altura = float(stdin.readline())
print("Salida: ")
salida = ((base*altura)/2)
print("El área del triángulo es: " + str(round(salida,2)))
