from sys import stdin
import math

def fact(n):
    if n == 0:
        return 1

    elif n == 1:
        return 1
    

    else: return n*fact(n-1)

def main():
    n = int(stdin.readline())
    print(fact(n))

main()


            
    

