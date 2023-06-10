def solution(n):
    cont = n
    if n == 1:
        return 1
        
    elif n == 2:
        return 5
        
    else:
        print(n)
        return solution(n-1)+(4*(n-1))

n = int(input())

print(solution(n))
