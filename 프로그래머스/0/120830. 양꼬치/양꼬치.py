def solution(n, k):
    answer = 0
    free_drink=n//10
    answer = n*12000+(k-free_drink)*2000
    return answer