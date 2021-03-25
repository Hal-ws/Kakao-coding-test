def solution(user_id, banned_id):
    global bancase
    bancase = set()
    chk = [0] * len(user_id) # user_ID 중 ban한 id는 1로 표시
    banList = []
    for idIdx in range(len(user_id)):
        if chkban(user_id[idIdx], banned_id[0]): # BAN 할수 있음
            chk[idIdx] = 1
            banList.append(user_id[idIdx])
            dfs(user_id, banned_id, 1, banList, chk)
            banList.pop()
            chk[idIdx] = 0
    answer = len(list(bancase))
    return answer


def dfs(user_id, banned_id, banIdx, banList, chk): # banIdx번째 banid를 ban해야함
    global bancase
    if banIdx == len(banned_id): # banned_id의 모든 id를 다 ban함
        ansList = sorted([banList[i] for i in range(len(banList))])
        tmp = ''
        for id in ansList:
            tmp += id
        bancase.add(tmp)
        return
    for idIdx in range(len(user_id)):
        if chk[idIdx] == 0:
            if chkban(user_id[idIdx], banned_id[banIdx]): # BAN 할수 있음
                chk[idIdx] = 1
                banList.append(user_id[idIdx])
                dfs(user_id, banned_id, banIdx + 1, banList, chk)
                banList.pop()
                chk[idIdx] = 0


def chkban(ID, banID):
    if len(ID) != len(banID):
        return 0
    for i in range(len(ID)):
        if ID[i] != banID[i] and banID[i] != '*':
            return 0
    return 1
