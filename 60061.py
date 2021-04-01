def solution(n, build_frame):
    global pillar_board, plate_board
    pillar_board = [[0 for j in range(n + 1)] for i in range(n + 1)]
    plate_board = [[0 for j in range(n + 1)] for i in range(n + 1)]
    l = len(build_frame)
    for i in range(l):
        x, y, flag1, flag2 = build_frame[i][0], build_frame[i][1], build_frame[i][2], build_frame[i][3]
        setY, setX = n - y, x
        if flag1: #보
            if flag2: # 설치
                plate_board[setY][setX] = 1
                if chk(n) == 0:
                    plate_board[setY][setX] = 0
            else:  # 삭제
                plate_board[setY][setX] = 0
                if chk(n) == 0:
                    plate_board[setY][setX] = 1
        else: # 기둥
            if flag2: #설치
                pillar_board[setY][setX] = 1
                if chk(n) == 0:
                    pillar_board[setY][setX] = 0
            else:
                pillar_board[setY][setX] = 0
                if chk(n) == 0:
                    pillar_board[setY][setX] = 1
    answer = []
    for i in range(n + 1):
        for j in range(n + 1):
            if pillar_board[i][j]:
                x, y = j, n - i
                answer.append([x, y, 0])
            if plate_board[i][j]:
                x, y = j, n - i
                answer.append([x, y, 1])
    answer.sort()
    return answer


def chk(n):
    global pillar_board, plate_board
    for i in range(n + 1):
        for j in range(n + 1):
            if pillar_board[i][j]: # pillar가 설치됐을때.
                if i != n: # i가 n이면 무조건 가능함. 불가능한 경우를 찿음
                    if pillar_board[i + 1][j] != 1:# # 밑에 기둥도 없음
                        if j == 0:
                            if plate_board[i][j] == 0: # 왼쪽 끝인데 오른쪽에 plate 없음
                                return 0
                        elif j == n: # 오른쪽 끝인데 왼쪽에 plate 없음
                            if plate_board[i][j - 1] == 0:
                                return 0
                        else:
                            if plate_board[i][j] == 0 and plate_board[i][j - 1] == 0: # 양쪽 다 plate가 없음
                                return 0
            if plate_board[i][j]:
                if pillar_board[i + 1][j] == 0 and pillar_board[i + 1][j + 1] == 0: #밑에 pillar 없음
                    if j == 0 or j == n - 1: # 한쪽 끝에 있어서 양쪽에 plate가 올수 없음
                        return 0
                    if plate_board[i][j - 1] == 0 or plate_board[i][j + 1] == 0:
                        return 0
    return 1
