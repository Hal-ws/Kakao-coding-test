def solution(m, n, board):
    newboard = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            newboard[i][j] = board[i][j]
    answer = [0]
    i, cnt = 1, 0
    while 1:
        cnt = abolish(m, n, newboard, cnt)
        answer.append(cnt)
        if answer[i] == answer[i - 1]:
            break
        i += 1
    return cnt

def abolish(m, n, board, cnt):
    chk = [[0 for i in range(n)] for j in range(m)]
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] != "0" and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                cnt += 4 - (chk[i][j] + chk[i + 1][j] + chk[i][j + 1] + chk[i + 1][j + 1])
                chk[i][j], chk[i + 1][j], chk[i][j + 1], chk[i + 1][j + 1] = 1, 1, 1, 1
    for i in range(m):
        for j in range(n):
            if chk[i][j]:
                board[i][j] = "0"
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if board[j][i] == "0":
                emptybox = j
                for k in range(j - 1, -1, -1):
                    if board[k][i] != "0":
                        board[emptybox][i] = board[k][i]
                        board[k][i] = "0"
                        emptybox -= 1
    return cnt
