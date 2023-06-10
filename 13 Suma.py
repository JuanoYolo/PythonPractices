from sys import stdin
def suma(n):

    if len(n) == 1:
        return int(n[0])

    else:
        return int(n[0]) + suma(n[1:])

def main():
    n = stdin.readline().strip().split(",")
    print(suma(n))
main()
