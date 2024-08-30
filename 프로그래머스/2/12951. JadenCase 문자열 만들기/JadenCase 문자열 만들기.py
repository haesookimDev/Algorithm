def solution(s):
    answer = ''
    result=[]
    s = s.lower().split(" ")
    for i in s:
        if i:
            Z = i[0].upper() + i[1:]
        else:
            Z = i
        result.append(Z)
    
    return ' '.join(result)