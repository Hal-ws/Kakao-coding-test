from bisect import bisect_left


def solution(info, query):
    answer = []
    tree = [[] for i in range(24)]
    allChk, cppChk, javaChk, pythonChk, frontChk, backChk, juniorChk, seniorChk, chickenChk, pizzaChk = \
        16777215, 16711680, 65280, 255, 15790320, 986895, 13421772, 3355443, 11184810, 5592405
    for tmp in info:
        lang, jGroup, career, food, score = map(str, tmp.split())
        score = int(score)
        idx = 0
        if lang == 'java':
            idx += pow(2, 3)
        if lang == 'python':
            idx += pow(2, 4)
        if jGroup == 'backend':
            idx += pow(2, 2)
        if career == "senior":
            idx += pow(2, 1)
        if food == "pizza":
            idx += pow(2, 0)
        tree[idx].append(score)
    lenList = []
    for i in range(24):
        tree[i].sort()
        lenList.append(len(tree[i]))
    for tmp in query:
        tmpList = list(map(str, tmp.split()))
        lang, jGroup, career, food, score = tmpList[0], tmpList[2], tmpList[4], tmpList[6], int(tmpList[7])
        possIdx = 16777215
        if lang == 'cpp':
            possIdx = possIdx & cppChk
        if lang == 'java':
            possIdx = possIdx & javaChk
        if lang == 'python':
            possIdx = possIdx & pythonChk
        if jGroup == 'frontend':
            possIdx = possIdx & frontChk
        if jGroup == 'backend':
            possIdx = possIdx & backChk
        if career == 'junior':
            possIdx = possIdx & juniorChk
        if career == 'senior':
            possIdx = possIdx & seniorChk
        if food == 'chicken':
            possIdx = possIdx & chickenChk
        if food == 'pizza':
            possIdx = possIdx & pizzaChk
        possIdx = str(bin(possIdx))
        possIdx = possIdx[2:]
        possIdx = '0' * (24 - len(possIdx)) + possIdx
        cnt = 0
        for i in range(24):
            if possIdx[i] == '1' and lenList[i] > 0:
                if score <= tree[i][-1]:
                    minIdx = bisect_left(tree[i], score)
                    cnt += lenList[i] - minIdx
        answer.append(cnt)
    return answer
