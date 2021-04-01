from itertools import permutations


def solution(n, weak, dist):
    global cases
    answer = 10
    cases = list(permutations(dist))
    l = len(weak)
    for sIdx in range(l):
        tmp = wallchk(n, sIdx, weak)
        if tmp != 0 and tmp < answer:
            answer = tmp
    if answer == 10:
        answer = -1
    return answer


def wallchk(n, sIdx, weak): # start weak point의 idx를 변수로 받음. n: 외벽의 길이
    global cases
    result = 10
    l = len(cases[0])
    weakL = len(weak)
    pos = []
    for i in range(weakL):
        curIdx = sIdx + i
        if curIdx == sIdx: # 시작 좌표는 0으로 잡음
            pos.append(0)
        else:
            if curIdx < weakL: # 원 한바퀴 아직 안돌았음
                pos.append(weak[curIdx] - weak[sIdx])
            else: # 돌았음
                pos.append((n - weak[sIdx]) + weak[curIdx - weakL])
    for case in cases:
        chk = [0] * weakL
        pIdx = 0
        for i in range(l): # i번 친구부터 l - 1친구까지 한명씩 배치한다
            dis = case[i]
            chk[pIdx] = 1
            nxtPidx = None
            for j in range(pIdx + 1, weakL):
                p = pos[j]
                if p - pos[pIdx] > dis: # 못닿음
                    if nxtPidx == None:
                        nxtPidx = pIdx + 1
                    break
                else: # 닿음
                    chk[j] = 1
                    nxtPidx = j + 1 # j번 포인트까지는 닿음
            if chk[weakL - 1] == 1: # 마지막 포인트까지 다 도착했음
                cnt = i + 1 # i + 1명을 사용함
                if cnt < result:
                    result = cnt
                break
            pIdx = nxtPidx # 다음으로 확인 시작할 point의 idx
    return result


print(solution(10, [1, 5], [1, 2]))
