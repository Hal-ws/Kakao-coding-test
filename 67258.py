def solution(gems):
    answer = [1, 100001] # 제일 긴 범위로 지정
    idxBook = {} # 보석의 이름에 따른 idx 저장
    l = len(gems)
    gIdx = 0
    for gName in gems:
        if idxBook.get(gName) == None:
            idxBook[gName] = gIdx
            gIdx += 1
    cntInRange = [0 for i in range(gIdx)] # 보석 idx별로 현재 범위 내에 몇개 있는지 표시
    start, end = 0, 0
    cntInRange[idxBook[gems[0]]] = 1
    dCnt = 1 # range 안에 있는 서로 다른 보석의 종류
    if dCnt == gIdx:
        return [1, 1]
    while start != l - 1 and end != l - 1:
        if end < l - 1:
            end += 1
            newGIdx = idxBook[gems[end]] # 새 보석의 idx
            if cntInRange[newGIdx] == 0:
                dCnt += 1
            cntInRange[newGIdx] += 1
        if start < l - 1:
            while 1:
                delGIdx = idxBook[gems[start]]
                if cntInRange[delGIdx] > 1:
                    cntInRange[delGIdx] -= 1
                    start += 1
                else:
                    break
        if dCnt == gIdx:
            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]
            if end - start == answer[1] - answer[0]:
                if start + 1 < answer[0]:
                    answer = [start + 1, end + 1]
    return answer
