from itertools import combinations


def solution(n, info):  ## info: 어치피가 맞춘 점수의 갯수. 10점~0점 순서대로 배치
    scoreChoice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #
    diffCase = [[] for i in range(101)]  # 최대 점수차: 100점
    for i in range(1, n + 1):
        cases = list(combinations(scoreChoice, i))  # winList중에 i번을 이기는 경우를 고른다
        for case in cases:
            resultList, diff = simulation(n, info, case)
            if resultList != []:
                diffCase[diff].append(resultList)
    candidates = []
    for i in range(100, -1, -1):
        if diffCase[i] != []:
            candidates = diffCase[i]
            break
    if candidates == []:
        return [-1]
    smallCntList = []
    for i in range(len(candidates)):
        tmpCnt = [0] * 11  #
        for score in range(11):
            tmpCnt[score] = candidates[i][10 - score]
        smallCntList.append([tmpCnt, i])
    smallCntList.sort(reverse=True)
    ansIdx = smallCntList[0][1]
    return candidates[ansIdx]


def simulation(n, info, case):
    result = [0] * 11
    arrowCnt = n
    for winTarget in case:  #이겨야 하는 점수
        scoreIdx = 10 - winTarget # 점수판의 idx
        muziShot = info[scoreIdx]  # 무지가 맞춘 타겟의 수
        if arrowCnt > muziShot: # 해당 점수를 얻을 수 있을 때
            result[scoreIdx] = muziShot + 1
            arrowCnt -= (muziShot + 1)
        else:
            return [], 0
    lionScore, muziScore = 0, 0
    for i in range(11):
        if result[i] > info[i]: # 10 - i점 target에서 line이 이김
            lionScore += (10 - i)
        elif info[i] != 0:
            muziScore += (10 - i)
    if arrowCnt > 0: # 아직 안쏜 화살이 있을때
        for i in range(10, -1, -1):
            if result[i] == 0: #
                if info[i] > 0:
                    if arrowCnt >= info[i]:  # 지금 무지가 맞춘 화살만큼 다 집어넣을 수 있음
                        result[i] = info[i]
                        arrowCnt -= info[i]
                    else:
                        result[i] = arrowCnt
                        arrowCnt = 0
            if arrowCnt == 0:
                break
    if lionScore > muziScore:
        return result, lionScore - muziScore
    return [], 0

print(solution(5,
         [2,1,1,1,0,0,0,0,0,0,0]))
