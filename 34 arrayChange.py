def solution(inputArray):
    lis = [inputArray[0]]
    inputArray.remove(inputArray[0])
    cont = 0

    for i in inputArray:
        if i > lis[-1]:
            lis.append(i)

        else:
            cont1 = lis[-1] - i + 1
            cont += cont1
            lis.append(i+cont1)

    return cont

inputArray = [-1000, 0, -2, 0]
#inputArray = [0,-2]
#inputArray = [2, 1, 10, 1]
print(solution(inputArray))
