def solution(msg):
    answer = []
    dictionary = ['']
    for i in range(65, 91):
        dictionary.append(chr(i))
    sIdx = 0
    while sIdx < len(msg):
        tmp = getLongest(sIdx, dictionary, msg)
        lgstIdx, lgstLen = tmp[0], tmp[1]
        answer.append(lgstIdx)
        if sIdx + lgstLen < len(msg):
            nWord = msg[sIdx:sIdx + lgstLen + 1]
            dictionary.append(nWord)
        sIdx = sIdx + lgstLen
    return answer


def getLongest(sIdx, dictionary, msg): # sIdx에서 시작하는 제일 긴 문자열을 구함
    lgstLen = 0
    lgstIdx = 0
    for i in range(1, len(dictionary)):
        word = dictionary[i]
        lw = len(word)
        if sIdx + lw - 1 < len(msg):
            if word == msg[sIdx:sIdx + lw]:
                if lw > lgstLen:
                    lgstIdx = i
                    lgstLen = lw
    return [lgstIdx, lgstLen]
