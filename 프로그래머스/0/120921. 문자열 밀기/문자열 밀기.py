def solution(A, B):
    answer = 0
    if A==B:
        return 0
    A=list(A)
    for _ in range(len(A)):
        answer+=1
        A.insert(0, A.pop())
        if ''.join(A)==B:
            return answer
    return -1