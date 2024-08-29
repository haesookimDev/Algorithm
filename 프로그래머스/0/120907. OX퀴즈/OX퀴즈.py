def solution(quiz):
    answer = []
    for i in quiz:
        oper = i.split(' ')
        if oper[1]=='-':
            if (int(oper[0])-int(oper[2]))==int(oper[4]):
                answer.append("O")
            else:
                answer.append("X")
        if oper[1]=='+':
            if (int(oper[0])+int(oper[2]))==int(oper[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer