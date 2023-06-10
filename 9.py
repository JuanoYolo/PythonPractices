from sys import stdin

print("Ingresa una lista de números:")
palabra = stdin.readline().strip().split(",")

numeros = [int(num) for num in palabra]

print("El número más grande es: "+ str(max(numeros)))
