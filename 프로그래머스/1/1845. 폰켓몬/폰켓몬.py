'''
N마리 > 절반 획득
번호로 구분
절반을 가져갈 때 가장 많은 종류를 획득하는 방법

input: nums: 1D-array, 1 =< len(num) <= 10,000
종류 번호 개수 200,000
output: answer: int > 가장 많은 종류 번호의 개수 최대값 한개
'''
def solution(nums):
    answer = 0
    gettable_number: int = len(nums)//2
    set_list = set(nums)
    species_number: int = len(list(set_list))
    
    if species_number>=gettable_number:
        answer=gettable_number
    else:
        answer=species_number
    return answer