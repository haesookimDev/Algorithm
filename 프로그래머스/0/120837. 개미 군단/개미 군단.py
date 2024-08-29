def solution(hp):
    answer = 0
    genaral = hp//5
    soldier = (hp - genaral*5)//3
    work = (hp - (genaral*5+soldier*3))//1
    return genaral+soldier+work