def solution(numbers):
    answer = 0
    mul_list = []
    while numbers:
        first = numbers[0]
        numbers.remove(first)
        for i in numbers:
            mul_list.append(first*i)
    return max(mul_list)