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
    for i in range(n + 1):
        print(pillar[i])
    print('--------------------------------')
    for i in range(n + 1):
        print(plate[i])
    print('********************************')
    answer = []
    return answer


def setpillar(pillar, plate, command, n):
    print('command: %s' %command)
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
    print('command: %s' %command)
    if command[1] == 0:
        plate[n - command[1]][command[0]] = 1
    else:
        if pillar[n - command[1] + 1][command[0]] == 1 or pillar[n - command[1] + 1][command[0] + 1] == 1:
            plate[n - command[1]][command[0]] = 1
        if command[0] > 0:
            if plate[n - command[1]][command[0] - 1] == 1 and plate[n - command[1]][command[0] + 1] == 1:
                plate[n - command[1]][command[0]] = 1


def dispillar(pillar, plate, command, n):
    return 0


def displate(pillar, plate, command, n):
    return 0

solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
