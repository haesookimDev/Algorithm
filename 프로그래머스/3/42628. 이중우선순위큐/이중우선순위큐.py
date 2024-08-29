def solution(operations):
    answer = []
    
    for i in operations:
        oper = i.split()
        if oper[0]=='I':
            answer.append(int(oper[1]))
        elif oper[0]=='D':
            if len(answer)==0:
                continue
            else:
                if oper[1]=='-1':
                    answer.remove(min(answer))
                elif oper[1]=='1':
                    answer.remove(max(answer))
        answer=sorted(answer, reverse=True)
        
    if len(answer)==0:
        answer=[0,0]
    else:
        answer=[max(answer), min(answer)]
    return answer