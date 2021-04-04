from collections import deque


def solution(board, r, c):
    global answer, dy, dx
    answer = 100000000
    pos = [[] for i in range(7)]
    start = [r, c]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0: # 빈칸이 아니면
                pos[board[i][j]].append([i, j])
    chk = [[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0 and chk[i][j] == 0:
                cnt = getcnt(start, [i, j], board, chk) + 1
                chk[i][j] = 1
                dfs([i, j], cnt, board, pos, chk)
                chk[i][j] = 0
    return answer


def dfs(cur, cnt, board, pos, chk): # 현재 선택한 좌표, 현재까지 입력 횟수, board, chk
    global answer
    y, x = cur[0], cur[1]
    curCard = pos[board[y][x]] # 현재 카드의 좌표
    y1, x1, y2, x2 = curCard[0][0], curCard[0][1], curCard[1][0], curCard[1][1]
    nxt = None
    if chk[y1][x1] and chk[y2][x2]: #현재 카드는 다 matching 시킴
        for i in range(4):
            for j in range(4):
                if board[i][j] != 0 and chk[i][j] == 0:
                    add = getcnt(cur, [i, j], board, chk) + 1 # 이동 + 선택
                    chk[i][j] = 1
                    nxt = [i, j]
                    dfs(nxt, cnt + add, board, pos, chk)
                    chk[i][j] = 0
        if nxt == None: # 모든 카드 매칭 다시킴
            if cnt < answer:
                answer = cnt
    else: # 현재 카드와 matching시킬 카드 찾아야함
        if chk[y1][x1]: # y1, x1 좌표의 카드는 이미 선택
            nxt = y2, x2
        else:
            nxt = y1, x1
        add = getcnt(cur, nxt, board, chk) + 1
        chk[nxt[0]][nxt[1]] = 1
        dfs([nxt[0], nxt[1]], cnt + add, board, pos, chk)
        chk[nxt[0]][nxt[1]] = 0


def getcnt(p1, p2, board, chk):
    global dy, dx
    q = deque()
    visit = [[10000 for j in range(4)] for i in range(4)]
    visit[p1[0]][p1[1]] = 0 # 시작점
    q.append([p1[0], p1[1], 0])
    while len(q) > 0:
        tmp = q.popleft()
        y, x, dis = tmp[0], tmp[1], tmp[2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4 and dis + 1 < visit[ny][nx]: # 더 적은 입력으로 움직일 수 있을때
                q.append([ny, nx, dis + 1])
                visit[ny][nx] = dis + 1
        # move to up
        if y > 0:
            for i in range(1, 4):
                ny, nx = y - i, x
                if ny > 0:
                    if board[ny][nx] != 0 and chk[ny][nx] == 0: #빈칸이 아니고 제거한 칸도 아닐 때
                        if dis + 1 < visit[ny][nx]:
                            q.append([ny, nx, dis + 1])
                            visit[ny][nx] = dis + 1
                        break
                else:
                    if dis + 1 < visit[ny][nx]:
                        q.append([ny, nx, dis + 1])
                        visit[ny][nx] = dis + 1
                    break
        # move to down
        if y < 3:
            for i in range(1, 4):
                ny, nx = y + i, x
                if ny < 3:
                    if board[ny][nx] != 0 and chk[ny][nx] == 0: #빈칸이 아니고 제거한 칸도 아닐 때
                        if dis + 1 < visit[ny][nx]:
                            q.append([ny, nx, dis + 1])
                            visit[ny][nx] = dis + 1
                        break
                else:
                    if dis + 1 < visit[ny][nx]:
                        q.append([ny, nx, dis + 1])
                        visit[ny][nx] = dis + 1
                    break
        # move to left
        if x > 0:
            for i in range(1, 4):
                ny, nx = y, x - i
                if nx > 0:
                    if board[ny][nx] != 0 and chk[ny][nx] == 0: #빈칸이 아니고 제거한 칸도 아닐 때
                        if dis + 1 < visit[ny][nx]:
                            q.append([ny, nx, dis + 1])
                            visit[ny][nx] = dis + 1
                        break
                else:
                    if dis + 1 < visit[ny][nx]:
                        q.append([ny, nx, dis + 1])
                        visit[ny][nx] = dis + 1
                    break
        # move to right
        if x < 3:
            for i in range(1, 4):
                ny, nx = y, x + i
                if nx < 3:
                    if board[ny][nx] != 0 and chk[ny][nx] == 0: #빈칸이 아니고 제거한 칸도 아닐 때
                        if dis + 1 < visit[ny][nx]:
                            q.append([ny, nx, dis + 1])
                            visit[ny][nx] = dis + 1
                        break
                else:
                    if dis + 1 < visit[ny][nx]:
                        q.append([ny, nx, dis + 1])
                        visit[ny][nx] = dis + 1
                    break
    return visit[p2[0]][p2[1]]


print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
