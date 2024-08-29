'''
한명 제외 완주
참여자 = participant
완주자 = completion
return 완주 x
'''
def solution(participant, completion):
    p_dict: dict = dict()
    for person in participant:
        if person in p_dict:
            p_dict[person] += 1
        else:
            p_dict[person] = 1
    
    for person in completion:
        if person in p_dict:
            p_dict[person] -= 1
    
    for person, cnt in p_dict.items():
         if p_dict[person] == 1:
            return person