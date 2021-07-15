def solution(places):
    answer = []
    for room in places:
        answer.append(chkDistance(room))
    return answer


def chkDistance(room):
    cy = [-1, 1, 0, 0]
    cx = [0, 0, -1, 1]
    cy2 = [-2, 2, 0, 0]
    cx2 = [0, 0, -2, 2]
    dy = [-1, -1, 1, 1]
    dx = [-1, 1, -1, 1]
    flag = 1
    for y in range(5):
        for x in range(5):
            if room[y][x] == 'P': # 사람 있으니 검사 시작
                for d in range(4):
                    ny, nx = y + cy[d], x + cx[d]
                    if 0 <= ny < 5 and 0 <= nx < 5:
                        if room[ny][nx] == 'P':
                            flag = 0
                for d in range(4):
                    ny, nx = y + cy2[d], x + cx2[d]
                    if 0 <= ny < 5 and 0 <= nx < 5:
                        if room[ny][nx] == 'P':
                            if room[y + cy[d]][x + cx[d]] != 'X':
                                flag = 0
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < 5 and 0 <= nx < 5:
                        if room[ny][nx] == 'P': # 대각선에 사람 존재
                            if d == 0: # 좌상
                                if room[y - 1][x] != 'X' or room[y][x - 1] != 'X':
                                    flag = 0
                            if d == 1: # 우상
                                if room[y - 1][x] != 'X' or room[y][x + 1] != 'X':
                                    flag = 0
                            if d == 2: # 좌하
                                if room[y + 1][x] != 'X' or room[y][x - 1] != 'X':
                                    flag = 0
                            if d == 3: # 우하
                                if room[y + 1][x] != 'X' or room[y][x + 1] != 'X':
                                    flag = 0
    return flag
