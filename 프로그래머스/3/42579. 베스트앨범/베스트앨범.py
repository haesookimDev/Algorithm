'''
장르별 최대 두개
노래: 고유번호
1. 많이 재생된 장르먼저 수록
2. 많이 재생된 노래먼저 수록
3. 고유번호가 낮은 노래먼저 

input: genres, plays
output: album index list
'''
def solution(genres, plays):
    answer = []
    total_plays=dict()
    genre_list=dict()
    for idx, genre in enumerate(genres):
        if genre in total_plays:
            total_plays[genre]+=plays[idx]
            genre_list[genre].append((idx, plays[idx]))
        else:
            total_plays[genre]=plays[idx]
            genre_list[genre]=[(idx, plays[idx])]
    
    sorted_total_plays = sorted(total_plays.items(), key=lambda x : x[1], reverse=True)
    
    for value in sorted_total_plays:
        play_list = genre_list[value[0]]
        play_list=sorted(play_list, key=lambda x:x[1], reverse=True)
        for i in play_list[:2]:
            answer.append(i[0])
    
            
    
    
    
    return answer