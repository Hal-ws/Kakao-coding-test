def solution(n, arr1, arr2):
    map1, map2 = [], []
    for i in range(n):
        map1.append(changetomap(n, arr1[i]))
        map2.append(changetomap(n, arr2[i]))
    answer = [''] * n
    for i in range(n):
        for j in range(n):
            if map1[i][j] or map2[i][j]:
                answer[i] += '#'
            else:
                answer[i] += ' '
    return answer


def changetomap(n, num):
    a = [0] * n
    i = 1
    while num > 1:
        a[n - i] = num % 2
        num = num // 2
        i += 1
    a[n - i] = num
    return a
