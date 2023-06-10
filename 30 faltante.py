##def solution(sequence):
##    cont = sequence[0]
##    cont1 = 0
##    lis2=[]
##    for i in sequence:
##        if i >= cont and cont1 <= 1:
##            if i == cont:
##                cont1 += 1
##                
##        else:
##            lis2.append(i)
##                
##    if len(lis2) > 1:
##        return False
##        
##    else:
##        return True
##
##sequence = [0, -2, 5, 6]
###sequence = [1, 1, 1, 2, 3]
##print(solution(sequence))

def solution(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            #cont += 1
            sequence.pop(i)
            print(sequence)
            solution(sequence)
    return sequence

sequence = [1,3,2,1]
