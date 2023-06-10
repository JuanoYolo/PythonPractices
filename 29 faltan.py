def solution(statues):
    start = min(statues)
    end = max(statues)
    cont = 0
    for i in range(start,end):
        if i not in statues:
            cont += 1
    return cont
    
statues = [6, 3]
print(solution(statues))    
