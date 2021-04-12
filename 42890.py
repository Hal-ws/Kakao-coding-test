from itertools import combinations


def solution(relation):
    answer = 0
    l = len(relation[0])
    totalKey = [i for i in range(l)]
    cKeyList = []
    for kCnt in range(1, l + 1): # kCnt개의 key를 뽑아서 확인한다
        cases = list(combinations(totalKey, kCnt))
        for keys in cases:
            if chkCanKey(relation, keys, cKeyList):
                cKeyList.append(keys)
                answer += 1
    return answer


def chkCanKey(relation, keys, cKeyList):
    dic = {}
    for i in range(len(relation)):
        keyVal = ''
        for j in keys:
            keyVal += relation[i][j]
        if keyVal in dic: # 겹침
            return 0
        dic[keyVal] = 1
    for cKey in cKeyList:
        if chkIn(cKey, keys): # cKey가 keys에 완전히 포함됨
            return 0
    return 1


def chkIn(key1, key2): # key1이 key2에 완전히 포함됨
    flag = 0
    for val in key1:
        if val not in key2: # 포함되지 않은 값이 있음
            flag = 1
            break
    if flag:
        return 0
    return 1
