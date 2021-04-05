def solution(food_times, k):
    left, right = min(food_times), max(food_times)
    if sum(food_times) <= k:
        return -1
    minEat = right + 1
    l = len(food_times)
    while left <= right:
        eat = (left + right) // 2 # eat개를 먹음
        totalTime = 0  # eat개를 먹었을 때 누적시간 기록
        flag = 0
        for i in range(l):
            time = food_times[i]
            if time >= eat:
                totalTime += eat
            else:
                totalTime += time
            if totalTime >= k: # eat씩 먹으면서 진행할땐 다 먹음
                flag = 1
                break
        if flag: # 다먹을수 있음
            right = eat - 1
            if eat < minEat:
                minEat = eat
        else: # 다 못먹음
            left = eat + 1
    totalTime = 0
    for i in range(l):
        time = food_times[i]
        if time >= minEat - 1:
            totalTime += minEat - 1
        else:
            totalTime += time
    for i in range(l):
        time = food_times[i]
        if time >= minEat:
            totalTime += 1
        if totalTime > k: # i번 idx의 음식을 먹어야 함
            return i + 1
    minEat += 1
    for i in range(l):
        if food_times[i] >= minEat:
            return i + 1
