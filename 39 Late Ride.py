import math

def solution(n):

    cont = 0
    minu =  n % 60
    hora = n // 60
    tiempo = str(minu) + str(hora)

    for i in tiempo:
        cont += int(i)
    
    return cont


n = 1439
print(solution(n))
