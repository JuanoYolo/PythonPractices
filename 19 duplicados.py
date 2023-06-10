from sys import stdin

def dupli(n):

    lis = []
    for i in n:
        if int(i) not in lis:
            lis.append(int(i))

    return lis
            

def main():
    n = stdin.readline().strip().split(",")
    print(dupli(n))

main()
