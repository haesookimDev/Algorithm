def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in arr:
        if len(answer)==0:
            answer.append(i)
        if i == answer[-1]:
            continue
        else:
            answer.append(i)
    return answer