def solution(n, t, m, timetable):
    from collections import deque
    l, leftcnt, leftbus, endflag, bustable = len(timetable), 0, [], 0, [540]
    for i in range(l):
        timetable[i] = int(timetable[i][:2]) * 60 + int(timetable[i][3:5])
    timetable = deque(sorted(timetable))
    for i in range(1, n):
        bustable.append(i * t + 540)
    for i in range(n): # i번 버스가 와서 j명의 사람을 데려감
        bus = [0] * m
        for j in range(m):
            if timetable[0] <= bustable[i]:
                bus[j] = timetable.popleft()
                leftcnt += 1
                if leftcnt == l:
                    endflag = 1
                    break
            else:
                bus[j] = 0
        leftbus.append(bus)
        if endflag:
            break
    if 0 in leftbus[n - 1]:
        answer = 540 + (n - 1) * t
    else:
        answer = findtime(leftbus[n - 1], n, t, m)
    hour, minutes = answer // 60, answer % 60
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    return hour + ':' + minutes

def findtime(lastbus, n, t, m):
    for j in range(m - 1): # 각 버스의 맨 뒷자리 사람의 시간부터 조사
        if lastbus[m - 1 - j] > lastbus[m - 1 - j - 1]:
            return lastbus[m - 1 - j] - 1
    return lastbus[0] - 1



solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
