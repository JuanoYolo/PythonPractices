from sys import stdin

def fibo(n):
    if n == 1:
        return 1

    elif n == 2:
        return 1

   
    return fibo(n-2)+fibo(n-1)



def main():
    n = int(stdin.readline())
    print(fibo(n))
    

main()
