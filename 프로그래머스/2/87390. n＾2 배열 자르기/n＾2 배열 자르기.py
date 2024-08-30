def solution(n, left, right):
    result = []
    for i in range(left, right+1):
        # left ~ right 사이의 숫자를 n으로 나누면
        # 몫은 y(index) 좌표를
        # 나머지는 x(index) 좌표를 알 수 있다.
        y, x = i//n, i%n
        # 넣을 값은 (y,x 좌표중 큰 값) + 1
        # [0][0]=1 [0][1]=2 [0][2]=3 [0][3]=4
        # [1][0]=2 [1][1]=2 [1][2]=3 [1][3]=4
        # [2][0]=3 [2][1]=3 [2][2]=3 [2][3]=4
        # [3][0]=4 [3][1]=4 [3][2]=4 [3][3]=4
        value = max(y,x) + 1
        result.append(value)
    return result