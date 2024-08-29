def solution(numbers, k):
    answer = 0
    ball = 1
    while True:
        if k==ball:
            return numbers[0]
        first = numbers[:2]
        numbers.remove(first[0])
        numbers.remove(first[1])
        numbers.extend(first)
        ball+=1
    return answer
