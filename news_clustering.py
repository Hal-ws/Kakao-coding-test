def solution(str1, str2):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    str1, str2, l1, l2, set1, set2 = str1.lower(), str2.lower(), len(str1), len(str2), [], []
    for i in range(l1 - 1):
        if str1[i].lower() in characters and str1[i + 1].lower() in characters:
            set1.append(str1[i] + str1[i + 1])
    for i in range(l2 - 1):
        if str2[i].lower() in characters and str2[i + 1].lower() in characters:
            set2.append(str2[i] + str2[i + 1])
    set1, set2, intersection, i, j, l1, l2 = sorted(set1), sorted(set2), [], 0, 0, len(set1), len(set2)
    while i < l1 and j < l2:
        if set1[i] == set2[j]:
            intersection.append(set1[i])
            i += 1
            j += 1
        elif set1[i] < set2[j]:
            i += 1
        else:
            j += 1
    sumofval = list(set(set(set1) | set(set2)))
    ls, unionlen = len(sumofval), 0
    for i in range(ls):
        unionlen += max(set1.count(sumofval[i]), set2.count(sumofval[i]))
    if unionlen == 0:
        answer = 65536
    else:
        answer = int(len(intersection) / unionlen * 65536)
    return answer
