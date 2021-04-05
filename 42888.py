def solution(record):
    global curName
    curName = {} # 현재 update 된 id
    answer = []
    logging = []
    for tmp in record:
        tmpList = list(map(str, tmp.split()))
        status, id = tmpList[0], tmpList[1]
        if status == 'Enter':
            name = tmpList[2]
            logging.append('Enter %s' %id)
            if curName.get(id) == None:
                curName[id] = name
            else:
                curName[id] = name
        if status == 'Leave':
            logging.append('leaving %s' %id)
        if status == 'Change':
            name = tmpList[2]
            curName[id] = name
    for log in logging:
        status, id = map(str, log.split())
        if status == 'Enter':
            answer.append('%s님이 들어왔습니다.' %curName[id])
        else:
            answer.append('%s님이 나갔습니다.' %curName[id])
    return answer
