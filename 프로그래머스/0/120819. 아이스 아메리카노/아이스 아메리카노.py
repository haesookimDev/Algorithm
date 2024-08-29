def solution(money):
    answer = []
    if money<5500:
        answer = [0, money]
    else:
        n_coffee = money//5500
        answer = [n_coffee, money-(n_coffee*5500)]
    return answer