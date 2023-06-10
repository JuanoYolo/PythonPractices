from sys import stdin
def cuenta_frecuencia(lista):
    numeros = []  # Lista para almacenar los números únicos en 'lista'
    frecuencias = []  # Lista para almacenar las frecuencias correspondientes a los números en 'numeros'

    for num in lista:
        if num not in numeros:
            numeros.append(num)  # Si el número es nuevo, añádelo a la lista de números
            frecuencias.append(1)  # Y añade un 1 a la lista de frecuencias
        else:
            indice = numeros.index(num)  # Si el número ya está en la lista, encuentra su índice
            frecuencias[indice] += 1  # E incrementa su frecuencia

    return list(zip(numeros, frecuencias))  # Devuelve una lista de tuplas (número, frecuencia)

def main():
    lista = stdin.readline().strip().split(",")
    int_x = list(map(int, lista))
    print(cuenta_frecuencia(lista))

main()