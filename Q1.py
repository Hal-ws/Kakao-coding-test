def solution(id_list, report, k):
    l = len(id_list)
    answer = [0] * l
    reportCnt = [0] * l  #idx별로 신고당한 횟수 추가
    idxBook = {}
    for i in range(l):
        idxBook[id_list[i]] = i
    reportId = [[0 for j in range(l)] for i in range(l)]  # i를 신고한아이디들을 표시
    for log in report:
        a, b = map(str, log.split())
        aIdx = idxBook[a]
        bIdx = idxBook[b]
        if reportId[bIdx][aIdx] == 0:
            reportId[bIdx][aIdx] = 1  ## bIdx를 aIdx가 신고함
            reportCnt[bIdx] += 1
    for i in range(l):
        if reportCnt[i] >= k: # 해당 유저 정지
            for j in range(l):
                if reportId[i][j]:
                    answer[j] += 1
    return answer


print(solution(["con", "ryan"],
               ["ryan con", "ryan con", "ryan con", "ryan con"],
         3))
