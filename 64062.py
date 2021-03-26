def solution(stones, k):
    l = len(stones)
    left, right = 0, max(stones) + 1
    while left <= right:
        mid = (left + right) // 2
        tmpDis = 0
        maxDis = 0
        for i in range(l):
            if stones[i] - mid >= 0: # 바위가 남아있음
                tmpDis = 0
            else: # 빈칸이 됨
                tmpDis += 1
            if maxDis < tmpDis:
                maxDis = tmpDis
        if k - 1 < maxDis: # 점프 못함
            right = mid - 1
        else: #점프 가능
            left = mid + 1
            answer = mid
    return answer
