def solution(inputArray):
    res = inputArray[0] * inputArray[1]
    cont = 0
    lis = []
    for i in range(len(inputArray)-1):
        cont = inputArray[i+1] * inputArray[i]
        lis.append(cont)
        
    return max(lis)

def main():
    inputArray = [3, 6, -2, -5, 7, 3]
    print(solution(inputArray))

main()
    
