from collections import deque


def solution(board):
    N = len(board)
    q = deque()
    q.append([[0, 0], [0, 1], 0, 0]) #p1, p2 좌표, 가로 세로표시, 시간
    visitP = [[0 for j in range(N)] for i in range(N)] #가로
    visitV = [[0 for j in range(N)] for i in range(N)] #세로
    #visit은 p2 를 기준으로 기록
    visitP[0][1] = 1
    dy = [0, 0, 1, -1]
    dx = [-1, 1, 0, 0]

    while len(q) > 0:
        cur = q[0] #현재 bar
        p1, p2 = cur[0], cur[1] #왼쪽/오른쪽 or 위/아래
        p1y, p1x, p2y, p2x = p1[0], p1[1], p2[0], p2[1]
        time = cur[3]
        for i in range(4):
            n1y, n1x, n2y, n2x = p1y + dy[i], p1x + dx[i], p2y + dy[i], p2x + dx[i]
            if 0 <= n1y < N and 0 <= n1x < N and 0 <= n2y < N and 0 <= n2x < N:
                if board[n1y][n1x] == 0 and board[n2y][n2x] == 0:
                    if cur[2] == 0: #가로로 누움
                        if visitP[n2y][n2x] == 0:
                            visitP[n2y][n2x] = 1
                            q.append([[n1y, n1x], [n2y, n2x], 0, time + 1]) #상태 그대로 움직임
                    else: #세로 bar가 움직임
                        if visitV[n2y][n2x] == 0:
                            visitV[n2y][n2x] = 1
                            q.append([[n1y, n1x], [n2y, n2x], 1, time + 1]) #상태 그대로 움직임
        if cur[2] == 0: #가로bar를 회전
            if p1y > 0 and board[p1y - 1][p1x] == 0 and board[p2y - 1][p2x] == 0: #위로 회전
                if visitV[p1y][p1x] == 0:
                    visitV[p1y][p1x] = 1
                    q.append([[p1y - 1, p1x], [p1y, p1x], 1, time + 1])
                if visitV[p2y][p2x] == 0:
                    visitV[p2y][p2x] = 1
                    q.append([[p2y - 1, p2x], [p2y, p2x], 1, time + 1])
            if p1y < N - 1 and board[p1y + 1][p1x] == 0 and board[p2y + 1][p2x] == 0:
                if visitV[p1y + 1][p1x] == 0:
                    visitV[p1y + 1][p1x] = 1
                    q.append([[p1y, p1x], [p1y + 1, p1x], 1, time + 1])
                if visitV[p2y + 1][p2x] == 0:
                    visitV[p2y + 1][p2x] = 1
                    q.append([[p2y, p2x], [p2y + 1, p2x], 1, time + 1])
        else: #세로 bar를 회전
            if p1x > 0 and board[p1y][p1x - 1] == 0 and board[p2y][p2x - 1] == 0:
                if visitP[p1y][p1x] == 0:
                    visitP[p1y][p1x] = 1
                    q.append([[p1y, p1x - 1], [p1y, p1x], 0, time + 1])
                if visitP[p2y][p2x] == 0:
                    visitP[p2y][p2x] = 1
                    q.append([[p2y, p2x - 1], [p2y, p2x], 0, time + 1])
            if p1x < N - 1 and board[p1y][p1x + 1] == 0 and board[p2y][p2x + 1] == 0:
                if visitP[p1y][p1x + 1] == 0:
                    visitP[p1y][p1x + 1] = 1
                    q.append([[p1y, p1x], [p1y, p1x + 1], 0, time + 1])
                if visitP[p2y][p2x + 1] == 0:
                    visitP[p2y][p2x + 1] = 1
                    q.append([[p2y, p2x], [p2y, p2x + 1], 0, time + 1])
        if p2 == [N - 1, N - 1]:
            answer = time
            break
        q.popleft()
    return answer


print(solution([[0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
