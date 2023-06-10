from sys import stdin

def move_list(lista, objetivo):
    
        if objetivo > len(lista):
            objetivo = objetivo - ((objetivo//(len(lista)))*len(lista))
            return move_thelist(lista, objetivo)
            
        else:
            return move_thelist(lista, objetivo)

def move_thelist(lista, objetivo):
    lis = [0]*len(lista)
    cont = 0
    for i in range(len(lista)): 
        if (objetivo + i) >= len(lista):
            cont += (objetivo+i) - len(lista)
            lis[cont]=lista[i]

        else:
            lis[(objetivo+i)]=lista[i]
        cont=0
    return lis

def main():
    lista = stdin.readline().strip().split(",")
    objetivo = int(stdin.readline())
    print(move_list(lista, objetivo))
    
main()

