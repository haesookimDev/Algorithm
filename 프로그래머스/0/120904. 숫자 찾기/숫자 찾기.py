def solution(num, k):
    answer = 0
    for idx, i in enumerate(str(num)):
        if int(i)==k:
            return idx+1
    
    return -1