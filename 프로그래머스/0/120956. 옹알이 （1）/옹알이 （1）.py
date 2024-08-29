def solution(babbling):
    babs = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        for bab in babs:
            babbling[i] = babbling[i].replace(bab, ' ')
            
        babbling[i] = babbling[i].replace(' ', '')
        
    return babbling.count('')