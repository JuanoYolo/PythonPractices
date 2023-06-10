from sys import stdin

    
def fibo(n):
    lis = [0,1]

    for i in range(n-2):
        cont = lis[-1-1] + lis[-1]
        lis.append(cont)

    return lis
    
    
def main():
    n = int(stdin.readline())
    print(fibo(n))

main()
