def solution(new_id):
    step1 = ''
    for c in new_id:
        if 65 <= ord(c) <= 90:
            step1 += chr(ord(c) + 32)
        else:
            step1 += c
    step2 = ''
    for c in step1:
        if 97 <= ord(c) <= 122:
            step2 += c
        elif 48 <= ord(c) <= 57:
            step2 += c
        elif c == '-' or c == '_' or c == '.':
            step2 += c
    step3 = ''
    for i in range(len(step2)):
        c = step2[i]
        if c == '.':
            if i == len(step2) - 1:
                step3 += c
            elif step2[i + 1] != '.':
                step3 += c
        else:
            step3 += c
    step4 = ''
    for i in range(len(step3)):
        c = step3[i]
        if i == 0 or i == len(step3) - 1:
            if c != '.':
                step4 += c
        else:
            step4 += c
    if step4 == '':
        step5 = 'a'
    else:
        step5 = step4
    if len(step5) >= 16:
        step6 = step5[:15]
        if step6[14] == '.':
            step6 = step6[:14]
    else:
        step6 = step5
    if len(step6) <= 2:
        step7 = step6 + (step6[-1] * (3 - len(step6)))
    else:
        step7 = step6
    answer = step7
    return answer
