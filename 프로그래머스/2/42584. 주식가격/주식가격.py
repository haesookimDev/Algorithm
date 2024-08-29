def solution(prices):
    leng_prices=len(prices)
    answer = [0] * leng_prices
    for idx, i in enumerate(prices):
        for j in range(idx+1, leng_prices):
            if i <= prices[j]:
                answer[idx] += 1
            else: 
                answer[idx] = j - idx
                break 
        
    return answer