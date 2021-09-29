import requests
import json


base_url = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod/"
key = "32826d28ba026eadf506f3d4a2a185b0"

start_header = {
    'Content-Type':'application/json',
    'X-Auth-Token':key
}

headers = {
    'Content-Type':'application/json',
    'Authorization':key
}

userScore = {} # 각 유저별 점수를 기록함
for i in range(901):
    userScore[i] = 0 #


def getUserInfo():
    response = requests.get(base_url + "user_info", headers=headers)
    data = response.json()["user_info"]  # 모든 유저의 아이디, 등급 배열
    return data


def start():
    data = {}
    data["problem"] = 2 ## 시나리오 번호
    response = requests.post(base_url + "start", headers=start_header, data=json.dumps(data))
    newKey = response.json()['auth_key']
    headers['Authorization'] = newKey
    return response


def getScore():
    response = requests.get(base_url + 'score', headers=headers)
    tmp = response.json()
    print("efficiency_score: %s" %tmp["efficiency_score"])
    print("accuracy_score1: %s" %tmp["accuracy_score1"])
    print("accuracy_score2: %s" %tmp["accuracy_score2"])
    print("total score: %s" %tmp["score"])
    return tmp


def waiting():
    response = requests.get(base_url + "waiting_line", headers=headers)
    data = response.json()['waiting_line']  ## 기다리고 있는 id, 대기 시작한 시간.  대기 15분 이상 안기다림
    return data


def changeGrade():
    scoreList = []
    for j in range(1, 901):
        scoreList.append([userScore[j], j])
    scoreList.sort()
    newGrade = []
    for j in range(900):
        uInfo = scoreList[j]
        tmp = {}
        tmp['id'] = uInfo[1]
        tmp['grade'] = j
        newGrade.append(tmp)
    d = {
        "commands":newGrade
    }
    response = requests.put(base_url + 'change_grade', headers=headers, data=json.dumps(d))
    return response


def matching(mList):
    d = {
        "pairs":mList
    }
    response = requests.put(base_url + 'match', headers=headers, data=json.dumps(d))
    return


def getResult():
    response = requests.get(base_url + "game_result", headers=headers)
    data = response.json()['game_result']  ## 승자, 패자, 소요시간 순서대로 정리
    for tmp in data:
        winner = tmp['win']
        loser = tmp['lose']
        time = tmp['taken']
        userScore[winner] += 100
        userScore[winner] += time - 3
        if userScore[loser] > 0 and userScore[winner] > 0: # 어뷰저 판단
            if userScore[loser] > userScore[winner] - 100 and time <= 10:
                userScore[winner] -= 100
                userScore[winner] -= (time - 3)
                userScore[loser] += 100
                userScore[loser] += (time - 3)
        if time >= 30:
            sumScore = userScore[winner] + userScore[loser]
            userScore[winner] = sumScore * 0.52
            userScore[loser] = sumScore * 0.48
    return data


def getMatchingList(wList, cTime):
    candidates = []  # 후보자들
    for user in wList:
        id, wTime = user["id"], user["from"]
        if cTime - wTime < 15:  # 15분 이하로 대기할때
            candidates.append([userScore[id], id])
    candidates.sort()
    mList = []
    for i in range(1, len(candidates), 2):
        id1, id2 = candidates[i][1], candidates[i - 1][1]
        score1, score2 = userScore[id1], userScore[id2]
        if abs(score1 - score2) <= 300:
            mList.append([id1, id2])
    return mList


start()  # 시작
for i in range(1, 556):  #1 ~ 556턴까지 진행
    print('time: %s' %i)
    wList = waiting()  # 현재 대기열에서 매칭을 대기 중인 유저들의 정보를 얻는다.
    userGrade = getUserInfo() # 모든 유저들의 현재 등급을 얻는다.
    gameResult = getResult() # 이번 턴에 게임이 끝난 유저들의 게임 결과를 얻는다.
    mList = getMatchingList(wList, i)
    matching(mList)
for i in range(556, 596): # 게임 결과만 받으면서 등급 수정함
    print('time: %s' %i)
    getResult()
    if i == 595:
        changeGrade()
    matching([])  # 매칭 안시킴
matching([]) # 게임 종료 명령
getScore()
