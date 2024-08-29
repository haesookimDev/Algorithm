def solution(balls, share):
    answer = fact(balls)/(fact(balls-share)*fact(share))
    
    return answer

def fact(n):
    result=1
    for i in range(n):
        result*=i+1
    return result