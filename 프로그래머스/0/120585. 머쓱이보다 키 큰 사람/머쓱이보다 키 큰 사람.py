def solution(array, height):
    answer = 0
    array = sorted(array)
    for idx, i in enumerate(array):
        if i>height:
            return len(array)-idx
    return answer