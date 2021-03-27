from math import inf


def solution(n, s, a, b, fares):
    s, a, b = s - 1, a - 1, b - 1
    disMatrix = [[inf for j in range(n)] for i in range(n)]
    answer = inf
    for i in range(n):
        disMatrix[i][i] = 0
    for road in fares:
        p1, p2, dis = road[0] - 1, road[1] - 1, road[2]
        disMatrix[p1][p2] = dis
        disMatrix[p2][p1] = dis
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if disMatrix[i][k] + disMatrix[k][j] < disMatrix[i][j]:
                    disMatrix[i][j] = disMatrix[i][k] + disMatrix[k][j]
    for m in range(n):
        tmp = disMatrix[s][m] + disMatrix[m][a] + disMatrix[m][b]
        if tmp < answer:
            answer = tmp
    if disMatrix[s][a] + disMatrix[s][b] < answer:
        answer = disMatrix[s][a] + disMatrix[s][b]
    if disMatrix[s][a] + disMatrix[a][b] < answer:
        answer = disMatrix[s][a] + disMatrix[a][b]
    if disMatrix[s][b] + disMatrix[b][a] < answer:
        answer = disMatrix[s][b] + disMatrix[b][a]
    return answer
