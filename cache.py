from collections import deque

def solution(cacheSize, cities):
    l = len(cities)
    for i in range(l):
        cities[i] = cities[i].lower()
    cache, spareCache, answer = deque([0] * cacheSize), cacheSize, 0
    if cacheSize == 0:
        answer = 5 * l
    else:
        for i in range(l):
            try:
                cacheIndex = cache.index(cities[i])
            except Exception as e:
                cacheIndex = None
            if cacheIndex == None:
                cache.append(cities[i])
                cache.popleft()
                answer += 5
            else:
                del cache[cacheIndex]
                cache.append(cities[i])
                answer += 1
    return answer
