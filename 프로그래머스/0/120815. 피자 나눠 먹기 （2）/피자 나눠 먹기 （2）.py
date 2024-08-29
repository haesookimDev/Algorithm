def solution(n):
    answer = 0
    answer = (n*6)//GCD(n, 6)
    return answer//6

def GCD(a, b):
    while(b>0):
        a, b = b, a%b
    return a
