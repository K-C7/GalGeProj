import random
import csv

LEAP_PATH = ""

examNumberList = []

def leapPathSet(path):
    """leap.csvのパス(返り値なし)"""
    global LEAP_PATH
    LEAP_PATH = path

def getWords(leapNumber):
    """LEAP番号 -> 英単語、意味"""
    with open(LEAP_PATH, encoding='UTF-8') as L:
        leap = list(csv.reader(L))
        en = leap[leapNumber-1][0]
        jp = leap[leapNumber-1][1]

        return en, jp

def ranNoKaburi(min, max, n, remove = []):
    """乱数の下限,上限,個数,除外リスト(省略可) -> 乱数のリスト"""
    result = []
    while(len(result) < n):
        ran = random.randint(min, max)
        if not(ran in result):
            if not(ran in remove):
                result.append(ran)

    return result

def makeExam(min, max, numOfQue):
    """問題番号の下限,上限,問題数でテスト問題のリスト作成(返り値なし)"""
    global examNumberList
    examNumberList = ranNoKaburi(min, max ,numOfQue)

def getOption(questionNumber, optMin, optMax, optNum):
    """問題番号,選択肢の問題番号の下限、上限、選択肢の数 -> 選択肢(リスト)"""
    opt = []
    optRemove = [examNumberList[questionNumber]]
    optQueNum = ranNoKaburi(optMin, optMax, optNum, optRemove)
    for i in range(optNum):
        opt.append(leap[optQueNum[i]][0])
    opt.append(ans)
    random.shuffle(opt)

    return opt

def getExam(questionNumber):
    """問題番号 -> Leap上の問題番号,解答,問題"""
    # 解答方法が'spell'の時は（）内は飛ばされる
    global examNumberList
    questionNumber -= 1 #leap.csvとのつじつま合わせ
    ans, que = getWords(examNumberList[questionNumber])

    return examNumberList[questionNumber], ans, que

def verifyValue(rangeNum, minNum=1):
    """出題範囲が正しいか確認"""
    try:
        rangeNum = int(rangeNum)
        if rangeNum < minNum:
            rangeNum = minNum
        elif rangeNum > 1935:
            rangeNum = 1935
            
    except:
        return -1
            
    else:
        return rangeNum