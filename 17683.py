def solution(m, musicinfos):
    newMusicInfos = []
    for i in range(len(musicinfos)):
        start, end, name, sheet = map(str, musicinfos[i].split(','))
        sh, sm = map(int, start.split(':'))
        start = sh * 60 + sm
        eh, em = map(int, end.split(':'))
        end = eh * 60 + em
        newMusicInfos.append([-1 * (end - start + 1), i, name, sheet])
    newMusicInfos.sort()
    for music in newMusicInfos: # 멜로디 가능한지 확인
        if chkMelody(m, music[3], -1 * music[0]):
            return music[2]
    return "(None)"


def chkMelody(melody, sheet, runningT):
    sList = [] # sheet를 list로 표현
    repeated = []
    mList = []
    for i in range(len(melody)):
        if melody[i] == '#':
            mList[-1] = mList[-1] + '#'
        else:
            mList.append(melody[i])
    mLen = len(mList)
    for i in range(len(sheet)):
        if sheet[i] == '#':
            sList[-1] = sList[-1] + '#'
        else:
            sList.append(sheet[i])
    for t in range(runningT):
        repeated.append(sList[t % len(sList)])
    for sIdx in range(len(repeated) - mLen + 1):
        flag = 1
        for i in range(mLen):
            if repeated[sIdx + i] != mList[i]:
                flag = 0
                break
        if flag:
            return 1
    return 0
