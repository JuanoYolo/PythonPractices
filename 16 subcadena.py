from sys import stdin

cadena = stdin.readline().strip().split(",")
prim = int(cadena[0])
lis = []
lis.append(prim)


for i in cadena:
    if int(i) > prim:
        prim = int(i)
        lis.append(int(i))
    
print(len(lis))

    
    
