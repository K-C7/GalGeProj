import random
import csv

LEAP_PATH = ""

examNumberList = []
examTFList = []

def leapPathSet(path):
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
    global examTFList
    examNumberList = ranNoKaburi(min, max ,numOfQue)
    examTFList = [0 for i in range(0, numOfQue)]

def getExam(questionNumber, answerWay, optMin=0, optMax=0, optNum=3):
    """問題番号,解答方法,選択肢の問題番号範囲の下限,〃の上限,選択肢の数 -> Leap上の問題番号,解答,問題(,選択肢(リスト))"""
    global examNumberList
    questionNumber -= 1
    ans = ''
    que = ''

    with open(LEAP_PATH, encoding='UTF-8') as L:
        leap = list(csv.reader(L))
        ans = leap[examNumberList[questionNumber]][0]
        que = leap[examNumberList[questionNumber]][1]

        if answerWay == 'fourChoice':
            opt = []
            optRemove = [examNumberList[questionNumber]]
            optQueNum = ranNoKaburi(optMin, optMax, optNum, optRemove)
            for i in range(optNum):
                opt.append(leap[optQueNum[i]][0])
            opt.append(ans)
            random.shuffle(opt)
            return examNumberList[questionNumber], ans, que, opt
        
        elif answerWay == 'spell':
            return examNumberList[questionNumber], ans, que
        
        else:
            raise Exception("変数\"answerWay\"の設定がバグってるっぴ!")

def ansExam(questionNumber, tf):
    """問題番号,その正誤"""
    #各問題の正誤を0か1かで記録する

    global examTFList

    if tf:
        examTFList[questionNumber - 1] = 1

    else:
        examTFList[questionNumber - 1] = 0

def resultExam():
    """-> 問題の正解数"""
    return sum(examTFList)