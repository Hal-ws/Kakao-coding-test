from math import sqrt


def solution(n, k):
    answer = 0
    newN = changeDigit(n, k)
    for i in range(len(newN)):
        tmpNum = ''
        for j in range(i, len(newN)):
            tmpNum += newN[j]
            if newN[j] == '0':  # 0 포함 안됨
                break
            if isPrime(int(tmpNum)): # 만약 소수일 때
                if i > 0 and j < len(newN) - 1:
                    if newN[i - 1] == '0' and newN[j + 1] == '0':
                        answer += 1
                elif j < len(newN) - 1:
                    if newN[j + 1] == '0':
                        answer += 1
                elif i > 0:
                    if newN[i - 1] == '0':
                        answer += 1
                elif i == 0 and j == len(newN) - 1:
                    answer += 1
    return answer


def isPrime(n):
    if n == 1:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def changeDigit(n, k):
    ans = ''
    while n > 0:
        ans = str(n % k) + ans
        n = n // k
    return str(ans)


print(solution(437674, 3))
