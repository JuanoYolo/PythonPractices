def solution(inputString):
    
    contains_letters = any(j.isalpha() for j in inputString)
    
    if contains_letters == False:
        b = inputString.strip().split(".")
        for i in b:
            if i == "":
                b.remove(i)

            
        lis = list(map(int, b))

        if len(lis) == 4:
            for i in lis:
                if i > 255 or i < 0:
                    return False

                else:
                    return True

        else:
            return False
        
    else:
        return False
        

#inputString = ".16.254.1"
#inputString = "172.316.254.1"
inputString = "1.1.1.1a"
print(solution(inputString))
