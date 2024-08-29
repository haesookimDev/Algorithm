def solution(n):
    answer = 0
    com=1
    while True:
        if com>n:
            return answer-1
        answer+=1
        com=com*answer
        
    return answer