def solution(array):
    answer = 0
    dic={}
    for i in array:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    dic_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    if len(dic_list)==1:
        return dic_list[0][0]
    
    if dic_list[0][1]==dic_list[1][1]:
        return -1
    else:
        return dic_list[0][0]