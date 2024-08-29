def solution(progresses, speeds):
    answer = []
    stack = []
    remain_days=[]
    minimum_day=0
    
    for idx, i in enumerate(progresses):
        progress = i
        speed=speeds[idx]
        
        remain_prog = 100-progress
        days = remain_prog/speed
        
        if int(days) == days:
            remain_days.append(int(days))
        else:
            remain_days.append(int(days)+1)
        
    for idx, i in enumerate(remain_days):
        if idx==0:
            minimum_day=i
            stack.append(idx)
        else:
            if minimum_day < i:
                answer.append(len(stack))
                stack=[]
                minimum_day = i
                stack.append(idx)
            else:
                stack.append(idx)
        
        

    answer.append(len(stack))
    
    return answer