from itertools import combinations


def solution(orders, course):
    answer = []
    for num in course: # num개의 메뉴로 만드는 경우의 수를 구함
        cnt = {}
        for tmp in orders:
            if len(tmp) < num:
                continue
            cases = list(combinations(tmp, num)) # tmp 주문 속에서 num개 고를 수 있는 경우를 나열
            for case in cases:
                picked = ''
                case = sorted(list(case))
                for c in case:
                    picked += c
                if cnt.get(picked) == None:
                    cnt[picked] = 1
                else:
                    cnt[picked] += 1
        cntItems = cnt.items()
        tmpList = []
        for tmp in cntItems:
            tmpList.append([tmp[1], tmp[0]])
        tmpList.sort()
        if len(tmpList) == 0:
            break
        maxCnt = tmpList[-1][0]
        if maxCnt > 1:
            for tmp in tmpList:
                if tmp[0] == maxCnt:
                    answer.append(tmp[1])
    answer.sort()
    return answer
