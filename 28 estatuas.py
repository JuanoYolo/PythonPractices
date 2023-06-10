def solution(statues):
    start = min(statues)
    end = max(statues)
    a = sorted(set(range(start, end + 1)).difference(statues))
    return len(a)

statues = [6, 2, 3, 8]
print(solution(statues))

##def missing_numbers(num_list):
##    start = num_list[0]
##    end = num_list[-1]
##    a = sorted(set(range(start, end + 1)).difference(num_list))
##    return len(a)
##
##nums = [1, 2, 5, 7]
##print(missing_numbers(nums))
