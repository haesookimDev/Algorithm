from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:
        return len(cities)*5
    cache = deque()
    cities = deque(cities)
    
    while cities:
        city = cities.popleft()
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer+=1
            continue
        if len(cache)<cacheSize:
            cache.append(city)
            answer+=5
            continue
        if len(cache)==cacheSize:
            cache.popleft()
            cache.append(city)
            answer+=5
            continue
    return answer