def solution(key, lock):
    M = len(key)
    N = len(lock)
    answer = True
    for k in range(-M + 1, M):
        for l in range(-M + 1, M):
            if open(key, lock, k, l, N): #key의 왼쪽 위 값의 좌표
                return answer
    rotate(key, M)
    for k in range(-M + 1, M):
        for l in range(-M + 1, M):
            if open(key, lock, k, l, N):  # key의 왼쪽 위 값의 좌표
                return answer
    rotate(key, M)
    for k in range(-M + 1, M):
        for l in range(-M + 1, M):
            if open(key, lock, k, l, N):  # key의 왼쪽 위 값의 좌표
                return answer
    rotate(key, M)
    for k in range(-M + 1, M):
        for l in range(-M + 1, M):
            if open(key, lock, k, l, N):  # key의 왼쪽 위 값의 좌표
                return answer
    answer = False
    return answer


def open(key, lock, dy, dx, N): #
    for i in range(N):
        for j in range(N):
            if 0 <= i - dy < N and 0 <= j - dx < N: # 겹치는 부분
                tmp = lock[i][j] + key[i - dy][j - dx]
                if tmp != 1: #겹친부분이 1이 아니면 안열림
                    return 0
            else: # 안겹치는 부분
                if lock[i][j] == 0: #안겹치는 부분은 무조건 다 차있어야함
                    return 0
    return 1 #열수있으면 open


def rotate(key, M):
    if M % 2 == 0:
        depth = M // 2 - 1
    else:
        depth = M // 2

    for layer in range(depth + 1):
        if M % 2 == 0:
            end = 2 * layer
            y, x = M // 2 - 1 - layer, M // 2 - 1 - layer
        else:
            end = 2 * layer + 1
            y, x = M // 2 - layer, M // 2 - layer
        for i in range(end - 1):
            key[y][x + i], key[y + i][x + end - 1], key[y + end - 1][x + end - 1 - i], key[y + end - 1 - i][x]\
                = key[y + end - 1 - i][x], key[y][x + i], key[y + i][x + end - 1], key[y + end - 1][x + end - 1 - i]


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
