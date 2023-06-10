from sys import stdin

def main():
    cadena = stdin.readline().lower().replace(".","").strip().split()
    lis = []
    dic = {}
    
    for i in cadena:
        cont = 1
        if i in dic:
            cont += 1
            dic.update({i:cont})

        else: dic[i] = 1
        
    print(dic)
main()
