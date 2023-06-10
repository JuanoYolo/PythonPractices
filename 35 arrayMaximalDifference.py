def solution(inputArray):
    cont = 0
    for i in range(len(inputArray)-1):
        if (abs(inputArray[i+1] - inputArray[i])) > cont:    
            cont = (abs(inputArray[i+1] - inputArray[i]))

        

    return cont
        
inputArray = [2, 4, 1, 0]
print(solution(inputArray))
