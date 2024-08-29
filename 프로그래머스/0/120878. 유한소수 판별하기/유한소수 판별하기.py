def get_factors(n):
    factors = []
    div = 2
    while n > 1:
        if n % div == 0:
            factors.append(div)
            n //= div
        else:
            div += 1
    return factors

def solution(a, b):
    answer = 2
    for i in range(2, a+1):
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i

    factors = get_factors(b)

    if all([x in [2,5] for x in factors]):
        answer = 1

    return answer