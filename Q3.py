def solution(fees, records):
    answer = []
    inTime, outTime = 0, 1
    minTime, minPrice, stdTime, stdPrice = fees[0], fees[1], fees[2], fees[3]
    recordsBook = [[None, None] for i in range(10000)]
    usedTime = [0] * 10000
    price = [0] * 10000
    lastT = 23 * 60 + 59
    for record in records:
        time, carNumber, state = map(str, record.split())
        h, m = map(int, time.split(':'))
        time = h * 60 + m
        carNumber = int(carNumber)
        if state == "IN": # 들어왔음
            recordsBook[carNumber][inTime] = time
        else:
            recordsBook[carNumber][outTime] = time ## 이때 사용시간 추가 후 리셋
            usedTime[carNumber] += recordsBook[carNumber][outTime] - recordsBook[carNumber][inTime]
            recordsBook[carNumber] = [None, None]
    for carNumber in range(10000):
        if recordsBook[carNumber][0] != None and recordsBook[carNumber][1] == None: #나간기록 없음
            usedTime[carNumber] += lastT - recordsBook[carNumber][0]
    for carNumber in range(10000):
        thisTime = usedTime[carNumber]
        if thisTime != 0: # 사용한것만 계산
            price[carNumber] = minPrice  #기본요금
            if thisTime > minTime:  #기본요금 초과
                leftTime = thisTime - minTime  # 기본요금 결제후 남은시간
                size = leftTime // stdTime
                if leftTime % stdTime != 0:
                    size += 1
                price[carNumber] += (stdPrice * size)
            answer.append(price[carNumber])
    return answer
