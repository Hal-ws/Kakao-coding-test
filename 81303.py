def solution(n, k, cmd):
    answer = ''
    cursor = k
    linkedList = [[0, 0] for i in range(n)] # 앞의 행, 다음 행
    linkedList[0][0], linkedList[0][1] = None, 1
    linkedList[n - 1][0], linkedList[n - 1][1] = n - 2, None
    stack = []
    for i in range(1, n - 1):
        linkedList[i][0] = i - 1
        linkedList[i][1] = i + 1
    print('start')
    print(linkedList)
    print('----------------------------------------')
    for tmp in cmd:
        print('cursor: %s' %cursor)
        print('tmp: %s' %tmp)
        if tmp[0] == 'U' or tmp[0] == 'D':
            ud, dis = map(str, tmp.split())
            dis = int(dis)
            if ud == 'U':
                ud = 0
            else:
                ud = 1
            cursor = moving(ud, dis, cursor, linkedList)
        if tmp[0] == 'C':
            cursor = delLine(cursor, linkedList, stack)
        if tmp[0] == 'Z':
            recover(stack, linkedList)
        print('after cursor: %s' %cursor)
        print('stack: %s' %stack)
        print('result: %s' %linkedList)
        print('----------------------------------------')
    for i in range(n):
        if linkedList[i][0] == linkedList[i][1] == None: # 삭제된 행
            answer += 'X'
        else:
            answer += 'O'
    return answer


def moving(ud, dis, cursor, linkedList): # 위/아래 방향, 거리, 현재 커서 위치
    cnt = 0
    while cnt < dis:
        if linkedList[cursor][ud] != None: # 끝이 아닌 상태
            cursor = linkedList[cursor][ud]
            cnt += 1
        else:
            break
    return cursor


def delLine(cursor, linkedList, stack):
    bCursor = linkedList[cursor][0]
    aCursor = linkedList[cursor][1]
    tmpCursor = cursor # 지울 위치 저장
    stack.append([bCursor, tmpCursor, aCursor])
    cursor = moving(1, 1, cursor, linkedList) # 아래칸으로 이동
    if bCursor != None:
        linkedList[bCursor][1] = linkedList[tmpCursor][1]
    if aCursor != None:
        linkedList[aCursor][0] = linkedList[tmpCursor][0]
    linkedList[tmpCursor][0], linkedList[tmpCursor][1] = None, None
    return cursor


def recover(stack, linkedList):
    tmp = stack.pop()
    bCursor, rCursor, aCursor = tmp[0], tmp[1], tmp[2]
    if bCursor != None:
        linkedList[rCursor][0] = bCursor
        linkedList[rCursor][1] = aCursor
    if aCursor != None:
        linkedList[bCursor][1] = rCursor
        linkedList[aCursor][0] = rCursor


print(solution(8, 2, 	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
