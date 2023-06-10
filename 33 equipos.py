def solution(a):
    lis = []
    cont = 0
    lis1 = []
    cont1 = 1
    for i in range(len(a)):
        if i % 2 == 0:
            lis.append(a[i])
            
        else:
            lis1.append(a[i])
        

    return [sum(lis),sum(lis1)]

a = [50, 60, 60, 45, 70]
print(solution(a))
