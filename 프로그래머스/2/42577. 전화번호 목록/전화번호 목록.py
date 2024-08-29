'''
전화번호 목록에서 
다른 번호가 특정번호의 접두사인 경우 False
중복 x > set 가능
'''
def solution(phone_book):
    hash_phone = set(phone_book)
    
    for phone in hash_phone:
        for i in range(len(phone)):
            prefix = phone[:i]
            if prefix in hash_phone:
                return False
    return True