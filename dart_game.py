def solution(dartResult):
    l = len(dartResult)
    scores, bonusIdx, optionIdx = [], [], []
    for i in range(l):
        if dartResult[i] == "S" or dartResult[i] == "D" or dartResult[i] == "T":
            bonusIdx.append(i)
        elif dartResult[i] == "#" or dartResult[i] == "*":
            optionIdx.append(i)
    for i in range(3):
        try:
            score = int(dartResult[bonusIdx[i] - 1])
            if score == 0:
                if bonusIdx[i] >= 2 and dartResult[bonusIdx[i] - 2] == "1":
                    scores.append(10)
                else:
                    scores.append(0)
            else:
                scores.append(score)
        except Exception as e:
            continue
    for i in range(3):
        if dartResult[bonusIdx[i]] == "D":
            scores[i] = pow(scores[i], 2)
        elif dartResult[bonusIdx[i]] == "T":
            scores[i] = pow(scores[i], 3)
    for i in range(len(optionIdx)):
        a = bonusIdx.index(optionIdx[i] - 1)
        if dartResult[optionIdx[i]] == "#":
            scores[a] *= -1
        else:
            if a >= 1:
                scores[a] *= 2
                scores[a - 1] *= 2
            else:
                scores[a] *= 2
    print(scores)
    return sum(scores)
