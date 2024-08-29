def solution(my_string, letter):
    answer = ''
    my_string=list(my_string)
    while letter in my_string:
        my_string.remove(letter)
    return "".join(my_string)