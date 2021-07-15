def solution(s):
    answer = ''
    l = len(s)
    i = 0
    while i < l:
        t = s[i]
        if 48 <= ord(t) <= 58:
            answer += str(t)
            i += 1
        else: ## 알파벳으로 주어짐
            if t == 'z':
                answer += '0'
                i += 4
            elif t == 'o':
                answer += '1'
                i += 3
            elif t == 't':
                if s[i + 1] == 'w':
                    answer += '2'
                    i += 3
                elif s[i + 1] == 'h':
                    answer += '3'
                    i += 5
            elif t == 'f':
                if s[i + 1] == 'o':
                    answer += '4'
                elif s[i + 1] == 'i':
                    answer += '5'
                i += 4
            elif t == 's':
                if s[i + 1] == 'i':
                    answer += '6'
                    i += 3
                elif s[i + 1] == 'e':
                    answer += '7'
                    i += 5
            elif t == 'e':
                answer += '8'
                i += 5
            elif t == 'n':
                answer += '9'
                i += 4
    return int(answer)
