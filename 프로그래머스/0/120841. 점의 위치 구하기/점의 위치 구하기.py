def solution(dot):
    answer = 0
    x=dot[0]
    y=dot[1]
    
    if x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    elif x>0 and y<0:
        return 4
    return answer