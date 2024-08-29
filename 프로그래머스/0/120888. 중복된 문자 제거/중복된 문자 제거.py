def solution(my_string):
    answer = ''
    str_dict = {}
    for i in my_string:
        if i not in str_dict:
            answer+=i
            str_dict[i]=0
    return answer