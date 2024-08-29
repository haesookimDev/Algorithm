def solution(array, n):
    answer = 0
    differ = float('inf')
    for i in array:
        temp = n-i
        if temp<0:
            temp*=-1
        if differ>temp:
            differ=temp
            answer = i
        if differ==temp:
            if answer>i:
                answer = i
    return answer