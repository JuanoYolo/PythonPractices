def solution(n):
    num = str(n)
    mid = len(num)//2
    cont = 0
    cont1 = 0
    for i in range(mid):
        cont += int(num[i])

    for i in range(mid,len(num)):
        cont1 += int(num[i])

    if cont == cont1:
        return True

    else:
        return False

n = 1230
print(solution(n))
