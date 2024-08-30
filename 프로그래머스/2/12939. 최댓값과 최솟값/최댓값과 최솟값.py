def solution(s):
    answer = []
    s_list = s.split(" ")
    s_list = [int(i) for i in s_list]
    answer.append(str(min(s_list)))
    answer.append(str(max(s_list)))
    return ' '.join(answer)