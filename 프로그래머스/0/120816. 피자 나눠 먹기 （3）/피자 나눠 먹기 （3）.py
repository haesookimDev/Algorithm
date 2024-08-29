def solution(slice, n):
    answer = 0
    if n//slice == n/slice:
        return n//slice
    else:
        return n//slice+1