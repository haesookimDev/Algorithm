def solution(n):
    answer = 0
    n_list = [i for i in range(n+1) if i%2==0]
    answer = sum(n_list)
    return answer