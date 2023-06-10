def solution(inputArray):
##    cont = len(inputArray[0])
##    lis = []
##    for i in inputArray:
##        if len(i) == cont:
##            lis.append(i)
##
##        elif len(i) > cont:
##            cont = len(inputArray[i])
##            lis.clear()
##            lis.append(i)
##
##    return lis
    inputArray.sort(key=len)
    print(inputArray)
    cont = inputArray[-1]
    for i in inputArray:
        if len(cont) != len(i):
            inputArray.remove(i)
    return inputArray        



inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(solution(inputArray))

