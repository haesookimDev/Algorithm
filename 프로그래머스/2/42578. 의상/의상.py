'''
매일 다른 옷을 입어야함
한 부위라도 달라야함
종류별로 한가지 의상만 착용
한가지만 입어도됨

한 종류 일때 > 의상 개수
두 종류 일때 > x, y > x + y + xy
세 종류 일때 > x, y, z > x + y + z + xy + yz + zx + xyz

> 

'''
def solution(clothes):
    answer = 1
    clothes_dict = dict(clothes)
    
    type_cnt = len(set(clothes_dict.values()))
    
    type_cnt_dict = dict()
    
    for key, value in clothes_dict.items():
        if value in type_cnt_dict:
            type_cnt_dict[value]+=1
        else:
            type_cnt_dict[value]=1
    
    for key, value in type_cnt_dict.items():
        answer *= value+1
        
    return answer-1