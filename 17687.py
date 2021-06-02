def solution(n, t, m, p):
    turn = ''
    answer = ''
    for num in range(30001):
        turn += changeJinsu(n, num)
    for i in range(t):
        answer += turn[m * i + p - 1]
    return answer


def changeJinsu(n, num):
    result = ''
    while 1:
        add = num % n
        if add < 10:
            result = str(add) + result
        else:
            result = chr(add + 55) + result
        num = num // n
        if num == 0:
            break
    return result
