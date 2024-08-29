def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    answer=sorted(list(my_string))
    return ''.join(answer)