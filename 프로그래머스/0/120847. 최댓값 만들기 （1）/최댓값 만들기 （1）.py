def solution(numbers):
    answer = 0
    while numbers:
        first = numbers[0]
        numbers.remove(numbers[0])
        for i in numbers:
            temp = i*first
            if answer<temp:
                answer=temp
    return answer