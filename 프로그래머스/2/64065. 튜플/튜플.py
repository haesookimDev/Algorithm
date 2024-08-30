def solution(s):
    answer = []
    count_dic=dict()
    
    s = s.replace('{','').replace('}','').split(',')
    
    for i in s:
        n = int(i)
        if n in count_dic:
            count_dic[n]+=1
            continue
        if n not in count_dic:
            count_dic[n]=1
    
    sorted_count = sorted(count_dic.items(), key=lambda x:x[1], reverse=True)
    
    for i in sorted_count:
        answer.append(i[0])
    
    return answer