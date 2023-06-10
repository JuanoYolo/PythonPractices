from sys import stdin


def find_pairs(lista, objetivo):
    visto = set()
    pares = []

    for num in lista:
        complemento = objetivo - num
        if complemento in visto:
            pares.append((num, complemento))
        visto.add(num)
    
    return pares

    

def main():
    lista = stdin.readline().strip().split(",")
    objetivo = int(stdin.readline())
    print(find_pairs(lista, objetivo))
main()
