from math import inf
from collections import deque


def solution(board):
    N = len(board)
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    visit = [[[inf for j in range(N)] for i in range(N)] for k in range(4)]
    answer = inf
    for k in range(4):
        visit[k][0][0] = 0 # 시작장소에 도착하는 비용은 0
    q = deque()
    if board[1][0] == 0:
        q.append([1, 0, 1, 1, 0]) #현재 위치 y, x, 방향, 직선도로 갯수, 꺾인갯수
        visit[1][1][0] = 100
    if board[0][1] == 0:
        q.append([0, 1, 3, 1, 0])
        visit[3][0][1] = 100
    while len(q) > 0:
        tmp = q.popleft()
        y, x, d, s, c = tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                if i == d: # 같은 방향으로 진행
                    if (s + 1) * 100 + c * 500 < visit[i][ny][nx]:
                        visit[i][ny][nx] = (s + 1) * 100 + c * 500
                        q.append([ny, nx, i, s + 1, c])
                else: # 다른 방향으로 진행
                    if (s + 1) * 100 + (c + 1) * 500 < visit[i][ny][nx]:
                        visit[i][ny][nx] = (s + 1) * 100 + (c + 1) * 500
                        q.append([ny, nx, i, s + 1, c + 1])
    for k in range(4):
        if visit[k][N - 1][N - 1] < answer:
            answer = visit[k][N - 1][N - 1]
    return answer
