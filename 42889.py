def solution(N, stages):
    answer = []
    rateList = [] # 실패율, stage level 저장
    curLevel = [0 for i in range(N + 2)] # 해당 idx를 도전중인 player 중 (N + 1 idx는 올클)
    playerSum = [0 for i in range(N + 2)]
    stages.sort()
    for level in stages:
        curLevel[level] += 1
    for i in range(1, N + 2):
        if i == 1:
            playerSum[i] = curLevel[i]
        else:
            playerSum[i] = playerSum[i - 1] + curLevel[i]
    for level in range(1, N + 2):
        arrive = playerSum[N + 1] - playerSum[level - 1] # 도달한 플레이어의 수
        noClear = curLevel[level] # 현재 해당 level을 클리어 중인 플레이어의 수
        if level != N + 1:
            if arrive != 0:
                rateList.append([noClear / arrive, -level])
            else:
                rateList.append([0, -level])
    rateList.sort(reverse=True)
    for i in range(len(rateList)):
        answer.append(-1 * rateList[i][1])
    return answer
