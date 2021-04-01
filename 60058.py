def solution(p):
    answer = getans(p)
    return answer


def getans(w):
    cnt1, cnt2 = 0, 0
    if w == '':
        return ''
    for i in range(len(w)):
        if w[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 != 0 and (cnt1 == cnt2):
            u, v = w[:i + 1], w[i + 1:]
            break
    if chkright(u):
        return u + getans(v)
    else:
        vResult = '('
        vResult += getans(v)
        vResult += ')'
        u = u[1:len(u) - 1]
        uResult = ''
        for c in u:
            if c == '(':
                uResult += ')'
            else:
                uResult += '('
        return vResult + uResult


def chkright(w):
    stack = []
    for i in range(len(w)):
        stack.append(w[i])
        if len(stack) >= 2:
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        return 1
    return 0
