def solution(numlist, n):
    answer = []
    
    min_diff=float('inf')
    min_num = 0
    numlist=sorted(numlist, reverse=True)
    
    while numlist:
        for i in numlist:
            diff=n-i
            if diff<0:
                diff*=-1
            if diff<min_diff:
                min_diff=diff
                min_num=i
        
        answer.append(min_num)
        numlist.remove(min_num)
        min_diff=float('inf')
        
    return answer