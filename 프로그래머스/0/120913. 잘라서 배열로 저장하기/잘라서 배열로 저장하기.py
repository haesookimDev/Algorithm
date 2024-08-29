def solution(my_str, n):
    answer = []
    idx =0
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
        idx=i+n
    # answer.append(my_str[idx:])
    return answer