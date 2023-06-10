from sys import stdin
def pote(n):
    if int(n[1]) == 1:
        return int(n[0])

    else:
        return int(n[0]) * pote([n[0], str(int(n[1]) - 1)])
def main():
    n = stdin.readline().strip().split(",")
    print(pote(n))

main()
