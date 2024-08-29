def solution(array):
    answer = 0
    array = sorted(array)
    mid = len(array)
    mid = mid//2
    answer = array[mid]
    return answer