def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    exit=[]
    passage=[]
    copied_truck_weight = truck_weights.copy()
    time=1
    
    passage.append(copied_truck_weight[0])
    passage_time=[1]
    copied_truck_weight.remove(copied_truck_weight[0])
      
    while passage:
        if passage_time[0]==bridge_length:
            exit.append(passage[0])
            passage.remove(passage[0])
            passage_time.remove(passage_time[0])
            passage_time = [i+1 for i in passage_time]
        else:
            passage_time = [i+1 for i in passage_time]
        if exit==truck_weights:
            time+=1
            answer = time
            break
        if copied_truck_weight:
            if (sum(passage)+copied_truck_weight[0])<=weight:
                passage.append(copied_truck_weight[0])
                passage_time.append(1)

                copied_truck_weight.remove(copied_truck_weight[0])
        time+=1
        answer = time
    
    return answer