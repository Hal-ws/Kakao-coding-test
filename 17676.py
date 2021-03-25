def solution(lines):
    answer = 0
    timeTable = []
    for l in lines:
        day, eTime, pTime = map(str, l.split())
        timeTable.append(getmt(eTime, pTime))
    timeTable.sort()
    for i in range(len(timeTable)):
        tmpAns = 1 # 자기자신은 일단 들어감
        pStartT, pEndT = timeTable[i][1], timeTable[i][0]
        for j in range(i + 1, len(timeTable)):
            if timeTable[j][1] <= pEndT + 999:
                tmpAns += 1
        if answer < tmpAns:
            answer = tmpAns
    return answer


def getmt(eTime, pTime):
    baseT = 4000 # 4000 밀리초에서 시작 (전날에 시작해서 넘어온 데이터 있음)
    h, m, s = map(str, eTime.split(':'))
    s, ms = map(str, s.split('.'))
    pTime = int(float(pTime[:len(pTime) - 1]) * 1000) - 1
    ms = '0.' + ms
    end = baseT + (int(h) * 3600000 + int(m) * 60000 + int(s) * 1000 + int(float(ms) * 1000))
    return [end, end - pTime]
