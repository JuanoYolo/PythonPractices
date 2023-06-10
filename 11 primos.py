from sys import stdin
import math

def primo(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(stdin.readline())
    lisprim = []
    for i in range(1,n+1):
        if primo(i):
            lisprim.append(i)
    print(lisprim)

main()


            
    

