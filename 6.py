from sys import stdin

numero = stdin.readline().split(",")

numeros = [int(num) for num in numero]

lis = []

for i in numeros:
    if i%2==0:
        lis.append(i)

print(sum(lis))
