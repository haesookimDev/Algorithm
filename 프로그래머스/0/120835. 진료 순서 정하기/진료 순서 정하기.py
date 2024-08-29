def solution(emergency):
    answer = []
    num_poe = len(emergency)
    
    for i in emergency:
        lt = 1
        for j in emergency:
            if i<j:
                lt+=1
        answer.append(lt)
    return answer