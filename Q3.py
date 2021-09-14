def solution(fees, records):
    answer = []
    minTime = fees[0]
    minPrice = fees[1]
    stdTime = fees[2]
    stdPrice = fees[3]
    recordsBook = [[None, None] for i in range(10000)]
    usedTime = [0] * 10000
    price = [0] * 10000
    lastT = 23 * 60 + 59
    for record in records:
        time, number, state = map(str, record.split())
        h, m = map(int, time.split(':'))
        time = h * 60 + m
        number = int(number)
        if state == "IN": # 들어왔음
            recordsBook[number][0] = time
        else:
            recordsBook[number][1] = time ## 이때 사용시간 추가 후 리셋
            usedTime[number] += recordsBook[number][1] - recordsBook[number][0]
            recordsBook[number] = [None, None]
    for i in range(10000):
        if recordsBook[i][0] != None and recordsBook[i][1] == None: #나간기록 없음
            usedTime[i] += lastT - recordsBook[i][0]
    for i in range(10000):
        thisTime = usedTime[i]
        if thisTime != 0: # 사용한것만 계산
            price[i] = minPrice  #기본요금
            if thisTime > minTime:  #기본요금 초과
                leftTime = thisTime - minTime  # 기본요금 결제후 남은시간
                size = leftTime // stdTime
                if leftTime % stdTime != 0:
                    size += 1
                price[i] += (stdPrice * size)
            answer.append(price[i])
    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
