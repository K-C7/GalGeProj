# import renpy.store as store
# import renpy.exports as renpy
import random
import csv

#定数の設定
QN_PART1 = 400
QN_PART2 = 1000
QN_PART3 = 1400
QN_PART4 = 1935

LEAP_PATH = "C:/Users/Shiina/Desktop/Projects/Renpy/LEAPer_beta/game/module/leap.csv"

examNumberList = []
examTFList = []


def ranNoKaburi(min, max, n, remove = []):
    # (乱数の下限, 上限, 個数, 除外リスト)
    result = []
    while(len(result) < n):
        ran = random.randint(min, max)
        if not(ran in result):
            if not(ran in remove):
                result.append(ran)
    return result


def verifyValue(min,max,numOfQue) -> bool:
    # ここでは引数として設定される予定の値の不正がないかを見る
    tf = True

    if not(type(min) is int):
        tf = False
    elif not(type(max) is int):
        tf = False
    elif not(type(numOfQue) is int):
        tf = False
    
    if(min < 1):
        tf = False
    if(max > 1935):
        tf = False
    if(max - min < numOfQue):
        tf = False

    return tf


def partToRange(part):
    # パート番号(1~4)を突っ込むと問題番号の範囲をリストとして返す
    min = 0
    max = 0

    if(part == 1):
        min = 1
        max = QN_PART1
    elif(part == 2):
        min = QN_PART1 + 1
        max = QN_PART2
    elif(part == 3):
        min = QN_PART2 + 1
        max = QN_PART3
    elif(part == 4):
        min = QN_PART3 + 1
        max = QN_PART4
    else:
        pass

    return [min, max]


'''
def makeExam(min,max,num):
    # 乱数を用いた基本的(そして無駄が多い)アルゴリズムで実装
    global examNumberList
    examNumberList = ranNoKaburi(min,max,num)
'''

def makeExam(part,numOfQue):
    global examNumberList
    global examTFList
    examTFList = []
    minMax = []

    minMax = partToRange(part)
    examNumberList = ranNoKaburi(minMax[0],minMax[1],numOfQue)


def getExam(questionNumber,optMin,optMax,optNum):
    global examNumberList
    questionNumber -= 1
    ans = ''
    que = ''
    with open(LEAP_PATH, encoding = 'cp932') as L:
        # leap = csv.reader(L)
        leap = list(csv.reader(L))
        ans = leap[examNumberList[questionNumber]][0]
        que = leap[examNumberList[questionNumber]][1]
        opt = []
        optRemove = [examNumberList[questionNumber]]
        optQueNum = ranNoKaburi(optMin, optMax, optNum, optRemove)
        for i in range(optNum):
            opt.append(leap[optQueNum[i]][0])
        opt.append(ans)
        random.shuffle(opt)
        
    return examNumberList[questionNumber], ans, que, opt


def ansExam(ans):
    # 答え合わせ、および不正解時の解答表示はできればRenpy側で実装したい <- しました
    # ここでは正誤の結果を保存するのみ
    global examTFList

    if(ans):
        examTFList.append(1)
    else:
        examTFList.append(0)

def resultExam():
    return sum(examTFList)