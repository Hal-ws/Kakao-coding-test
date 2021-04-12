from collections import deque


def solution(board):
    global dy, dx
    answer = 0
    N = len(board)
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    while 1:
        bFlag = 0 # 제거 가능한 block 발견했을 때
        for j in range(N):
            for i in range(N):
                if board[i][j] != 0: # block 발견
                    tmp = breakchk(board, i, j, N)
                    lu, pFlag, blockType = tmp[0], tmp[1], tmp[2]
                    lux, luy = lu[0], lu[1]
                    if pFlag: # 부수는거 가능
                        if blockType == 0:
                            board[luy][lux], board[luy + 1][lux], board[luy + 2][lux], board[luy + 2][lux + 1] = 0, 0, 0, 0
                        if blockType == 1:
                            board[luy][lux], board[luy][lux + 1], board[luy - 1][lux + 1], board[luy - 2][lux + 1] = 0, 0, 0, 0
                        if blockType == 2:
                            board[luy][lux], board[luy + 1][lux], board[luy + 1][lux + 1], board[luy + 1][lux + 2] = 0, 0, 0, 0
                        if blockType == 3:
                            board[luy][lux], board[luy][lux + 1], board[luy][lux + 2], board[luy - 1][lux + 2] = 0, 0, 0, 0
                        if blockType == 4:
                            board[luy][lux], board[luy][lux + 1], board[luy - 1][lux + 1], board[luy][lux + 2] = 0, 0, 0, 0
                        answer += 1
                        bFlag = 1
                    break # block 에 대한 연산 끝났으면 오른쪽으로 이동함
        if bFlag == 0: # 부술 수 있는 block이 없을때
            break
    return answer


def breakchk(board, y, x, N):
    global dy, dx
    block = board[y][x]
    pos = [[x, y]]
    q = deque()
    q.append([x, y])
    visit = [[0 for j in range(N)] for i in range(N)]
    visit[y][x] = 1
    while len(q) > 0:
        cur = q.popleft()
        x, y = cur[0], cur[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0 and board[ny][nx] == block:
                q.append([nx, ny])
                pos.append([nx, ny])
                visit[ny][nx] = 1
    pos.sort()
    lu, ld, ru, rd = pos[0], pos[1], pos[2], pos[3]
    lux, luy = lu[0], lu[1]
    rdx, rdy = rd[0], rd[1]
    flag = 0
    blockType = -1
    if lux <= N - 2 and luy <= N - 3:
        if board[luy][lux] == board[luy + 1][lux] == board[luy + 2][lux] == board[luy + 2][lux + 1] == block:
            flag = 1
            blockType = 0
    if lux <= N - 2 and luy >= 2:
        if board[luy][lux] == board[luy][lux + 1] == board[luy - 1][lux + 1] == board[luy - 2][lux + 1] == block:
            flag = 1
            blockType = 1
    if lux <= N - 3 and luy <= N - 2:
        if board[luy][lux] == board[luy + 1][lux] == board[luy + 1][lux + 1] == board[luy + 1][lux + 2] == block:
            flag = 1
            blockType = 2
    if lux <= N - 3 and luy >= 1:
        if board[luy][lux] == board[luy][lux + 1] == board[luy][lux + 2] == board[luy - 1][lux + 2] == block:
            flag = 1
            blockType = 3
    if lux <= N - 3 and luy >= 1:
        if board[luy][lux] == board[luy][lux + 1] == board[luy - 1][lux + 1] == board[luy][lux + 2] == block:
            flag = 1
            blockType = 4
    if flag:
        if blockType == 0:
            for i in range(rdy):
                if board[i][rdx] != 0:
                    flag = 0
                    break
        if blockType == 1:
            for i in range(luy):
                if board[i][lux] != 0:
                    flag = 0
                    break
        if blockType == 2:
            for j in range(lux + 1, rdx + 1):
                for i in range(rdy):
                    if board[i][j] != 0:
                        flag = 0
                        break
        if blockType == 3:
            for j in range(lux, rdx):
                for i in range(luy):
                    if board[i][j] != 0:
                        flag = 0
                        break
        if blockType == 4:
            for j in range(lux, lux + 3, 2):
                for i in range(luy):
                    if board[i][j] != 0:
                        flag = 0
                        break
    return [lu, flag, blockType]
