def solution(spell, dic):
    check = [1]*len(dic)
    for idx, i in enumerate(dic):
        for j in spell:
            if j in i:
                continue
            else:
                check[idx]=0
    check = list(set(check))
    try:
        check.index(1)
        return 1
    except:
        return 2