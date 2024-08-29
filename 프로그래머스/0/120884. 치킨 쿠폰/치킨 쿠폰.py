def solution(chicken):
    answer = 0
    if chicken<=9:
        return answer
    
    while chicken>=10:
        answer+=1
        chicken-=10
        chicken+=1
    return answer