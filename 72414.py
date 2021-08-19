def solution(play_time, adv_time, logs):
    answer = -1
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    timetable = [0 for i in range(play_time + 1)]
    maxTime = 0
    for log in logs:
        s, e = map(str, log.split('-'))
        s, e = time_to_sec(s), time_to_sec(e)
        timetable[s] += 1
        timetable[e] -= 1
    for i in range(1, len(timetable)):
        timetable[i] = timetable[i] + timetable[i - 1]
    for i in range(1, len(timetable)):
        timetable[i] = timetable[i] + timetable[i - 1] # 누적된 합으로 표시
    for ad_start in range(play_time - adv_time, 0, -1): # 광고가 시작하는 시간마다 표시
        ad_end = ad_start + adv_time
        tmp = timetable[ad_end - 1] - timetable[ad_start - 1]
        if tmp >= maxTime:
            maxTime = tmp
            answer = ad_start
    if timetable[adv_time - 1] >= maxTime:
        answer = 0
    return sec_to_time(answer)


def time_to_sec(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def sec_to_time(sec):
    h = str(sec // 3600)
    h = '0' * (2 - len(h)) + h
    sec = sec % 3600
    m = str(sec // 60)
    m = '0' * (2 - len(m)) + m
    sec = str(sec % 60)
    s = '0' * (2 - len(sec)) + sec
    return h + ':' + m + ':' + s
