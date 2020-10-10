def solution(s):
    ls = len(s)
    answer = 1001
    for i in range(1, ls // 2 + 1):
        temp = getans(s, i)
        if temp <= answer:
            answer = temp
    print(answer)
    return answer


def getans(s, d):
    ls = len(s)
    repeated, word = [1], [s[0:d]]
    lr = len(repeated) - 1
    i = d
    while i + d <= ls:
        if word[lr] == s[i:i + d]:
            repeated[lr] += 1
        else:
            word.append(s[i:i + d])
            repeated.append(1)
            lr += 1
        i += d
    if i < ls:
        repeated.append(1)
        word.append(s[i:ls])
        ls += 1
    lr = len(repeated)
    ans = ''
    for i in range(lr):
        if repeated[i] == 1:
            ans += word[i]
        else:
            temp = str(repeated[i]) + word[i]
            ans += temp
    return len(ans)


solution("d")
