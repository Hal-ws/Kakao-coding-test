def solution(files):
    answer = []
    sList = [] # sorted 되는 list
    for i in range(len(files)):
        sList.append(getComponent(files[i], i))
    sList.sort()
    for i in range(len(sList)):
        answer.append(files[sList[i][2]])
    return answer


def getComponent(filename, idx):
    head = ''
    number = ''
    nIdx = -1
    for i in range(len(filename)):
        if 48 <= ord(filename[i]) <= 57:
            nIdx = i
            break
        else:
            head += filename[i]
    head = head.lower() # 대소문자 구별 안하므로
    for i in range(nIdx, len(filename)):
        if 48 <= ord(filename[i]) <= 57:
            number += filename[i]
        else:
            break
        if len(number) == 5:
            break
    number = int(number)
    return [head, number, idx]
