def solution(my_string):
    answer = ''
    str_list = list(my_string)
    while 'a' in str_list:
        str_list.remove('a')
    while 'e' in str_list:
        str_list.remove('e')
    while 'i' in str_list:
        str_list.remove('i')
    while 'o' in str_list:
        str_list.remove('o')
    while 'u' in str_list:
        str_list.remove('u')
    answer = ''.join(str_list)
    return answer