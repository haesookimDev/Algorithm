def solution(before, after):
    answer = 1
    before = list(before)
    after = list(after)
    while before:
        first = before[0]
        before.remove(before[0])
        try:
            after.remove(first)
        except:
            return 0
    
    return answer