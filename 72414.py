def solution(play_time, adv_time, logs):
    answer = ''
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    timetable = [0 for i in range(play_time + 1)]
    for log in logs:
        
    

    return answer


def time_to_sec(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def sec_to_time(sec):
    return ''
