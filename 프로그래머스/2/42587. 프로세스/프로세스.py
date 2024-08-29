def solution(priorities, location):
    answer = 0
    process=[]
    ordered_process=[]
    
    max_prior=max(set(priorities))
    
    if len(priorities)==1:
        answer=1
        return answer

    for idx, i in enumerate(priorities):
        process.append((idx, i))
    
    while process:
        if len(process)==1:
            ordered_process.append(process[0])
            process.remove(process[0])
            priorities.remove(priorities[0])
        else:
            if process[0][1] == max_prior:
                ordered_process.append(process[0])
                process.remove(process[0])
                priorities.remove(max_prior)
                max_prior = max(set(priorities))
            else:
                process.append(process[0])
                process.remove(process[0])
                
    for idx, i in enumerate(ordered_process):
        if i[0]==location:
            answer=idx
    
    return answer+1