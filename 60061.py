def solution(n, build_frame):
    pillar = [[0 for i in range(n + 1)] for j in range(n + 1)]
    plate = [[0 for i in range(n + 1)] for j in range(n + 1)]
    lb = len(build_frame)
    for i in range(lb):
        if build_frame[i][2] == 0 and build_frame[i][3] == 1:
            setpillar(pillar, plate, build_frame[i], n)
        if build_frame[i][2] == 1 and build_frame[i][3] == 1:
            setplate(pillar, plate, build_frame[i], n)
        if build_frame[i][2] == 0 and build_frame[i][3] == 0:
            dispillar(pillar, plate, build_frame[i], n)
        if build_frame[i][2] == 1 and build_frame[i][3] == 0:
            displate(pillar, plate, build_frame[i], n)
        print('pillar')
        for j in range(n + 1):
            print(pillar[j])
        print('plate')
        for j in range(n + 1):
            print(plate[j])
        print('****************************')
    answer = []
    for i in range(n + 1):
        for j in range(n + 1):
            if pillar[i][j] == 1:
                answer.append([j, n - i, 0])
            if plate[i][j] == 1:
                answer.append([j, n - i, 1])
    answer.sort()
    return answer


def setpillar(pillar, plate, command, n):
    if command[1] == 0:
        pillar[n - command[1]][command[0]] = 1
    else:
        if pillar[n - command[1] + 1][command[0]] == 1:
            pillar[n - command[1]][command[0]] = 1
        if command[0] > 0:
            if plate[n - command[1]][command[0] - 1] == 1:
                pillar[n - command[1]][command[0]] = 1
        if command[0] < n:
            if plate[n - command[1]][command[0]] == 1:
                pillar[n - command[1]][command[0]] = 1


def setplate(pillar, plate, command, n):
    if command[1] == 0:
        plate[n - command[1]][command[0]] = 1
    else:
        if pillar[n - command[1] + 1][command[0]] == 1 or pillar[n - command[1] + 1][command[0] + 1] == 1:
            plate[n - command[1]][command[0]] = 1
        if command[0] > 0:
            if plate[n - command[1]][command[0] - 1] == 1 and plate[n - command[1]][command[0] + 1] == 1:
                plate[n - command[1]][command[0]] = 1


def dispillar(pillar, plate, command, n):
    pillar[n - command[1]][command[0]] = 0
    flag = 1
    for i in range(n + 1):
        for j in range(n + 1):
            if stable(pillar, plate, 0, [i, j], n) == 0:
                flag = 0
                break
    if flag == 0:
        pillar[n - command[1]][command[0]] = 1


def displate(pillar, plate, command, n):
    plate[n - command[1]][command[0]] = 0
    flag = 1 # flag가 1일때 해체 가능
    for i in range(n + 1):
        for j in range(n + 1):
            if stable(pillar, plate, 1, [i, j], n) == 0:
                flag = 0
                break
    if flag == 0: ## 해체하면 안될시 되돌림
        plate[n - command[1]][command[0]] = 1


def stable(pillar, plate, type, pos, n): ## type: 0은 pillar, type: 1은 plate
    if pos[0] == n:
        return 1
    if type == 0:
        if pillar[pos[0]][pos[1]] == 0:
            return 1
        if pillar[pos[0] + 1][pos[1]] == 1:
            return 1
        if pos[1] > 0 and plate[pos[0]][pos[1] - 1] == 1:
            return 1
        if pos[1] < n and plate[pos[0]][pos[1] + 1] == 1:
            return 1
    else:
        if plate[pos[0]][pos[1]] == 0:
            return 1
        if pillar[pos[0] + 1][pos[1]] == 1 or pillar[pos[0] + 1][pos[1] + 1] == 1:
            return 1
        if 0 < pos[1] < n - 1 and plate[pos[0]][pos[1] - 1] == 1 and plate[pos[0]][pos[1] + 1] == 1:
            return 1
    return 0


solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[3,2,1,1],[4,2,1,1]])
