def solution(price):
    answer = 0
    sale_pe = 1
    if 300000>price>=100000:
        sale_pe=0.95
    elif 500000>price>=300000:
        sale_pe=0.9
    elif price>=500000:
        sale_pe=0.8
    
    answer = price*sale_pe
    return int(answer)