def solution(my_string):
    answer = 0
    prefix = ''
    
    for i in my_string:
        if i.isdigit():
            prefix+=i
        else:
            if len(prefix)>=1:
                answer+=int(prefix)
                prefix=''
    if len(prefix)>=1:
        answer+=int(prefix)
        prefix=''
    return answer