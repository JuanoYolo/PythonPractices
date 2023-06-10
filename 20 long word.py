from sys import stdin

def longer(n):
    cont = n[0]
    lis = []
    for i in n:
        if len(i) == len(cont):
            lis.append(i)

        elif len(i) > len(cont):
            lis.clear()
            lis.append(i)
            cont = i

    return lis
                

def main():
    n = stdin.readline().strip().split()
    print(longer(n))

main()
