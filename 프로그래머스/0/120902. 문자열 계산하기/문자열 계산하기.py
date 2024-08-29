def solution(my_string):
    oper = []
    numbers = []
    for i in my_string.split():
        if i.isdigit():
            numbers.append(int(i))
        else:
            oper.append(i)
    answer = numbers[0]
    numbers.remove(answer)
    while oper:
        operation = oper[0]
        oper.remove(operation)
        number = numbers[0]
        numbers.remove(number)
        if operation=='+':
            answer+=number
        elif operation=='-':
            answer-=number
        
    return answer