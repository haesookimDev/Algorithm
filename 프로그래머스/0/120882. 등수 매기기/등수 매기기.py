def solution(score):
    answer = [1]*len(score)
    avg_sc = [sum(i)/len(i) for i in score]
    for idx, i in enumerate(avg_sc):
        for j in avg_sc:
            if i<j:
                answer[idx]+=1
    return answer