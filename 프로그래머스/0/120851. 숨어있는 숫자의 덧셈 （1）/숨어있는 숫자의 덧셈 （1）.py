def solution(my_string):
    answer = 0
    result=[]
    for i in my_string:
        if i.isdigit():
            result.append(int(i))
    return sum(result)