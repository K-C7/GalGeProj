# import renpy.store as store
# import renpy.exports as renpy
import random
import csv
import os

#定数の設定
QN_PART1 = 400
QN_PART2 = 1000
QN_PART3 = 1400
QN_PART4 = 1935

LEAP_PATH = ""

examNumberList = []
examTFList = []


def leapPathSet(path):
    global LEAP_PATH
    LEAP_PATH = path

def ranNoKaburi(min, max, n, remove = []):
    """乱数の下限, 上限, 個数, 除外リスト(省略可) -> 乱数のリスト"""
    result = []
    while(len(result) < n):
        ran = random.randint(min, max)
        if not(ran in result):
            if not(ran in remove):
                result.append(ran)
    return result


def verifyValue(min,max,numOfQue) -> bool:
    """出題範囲の最小値、最大値、出題数 -> 問題が作れるかどうか"""
    tf = True
    
    if(min < 1):
        tf = False
    if(max > 1935):
        tf = False
    if(max - min + 1 < numOfQue):
        tf = False

    return tf


def partToRange(part):
    """パート番号(1~4) -> 最初の問題番号, 最後の問題番号"""
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

    return min, max


def getLastNum():
    """-> LEAPの最後の問題番号"""
    return QN_PART4

'''
def makeExam(min,max,num):
    # 乱数を用いた基本的(そして無駄が多い)アルゴリズムで実装
    global examNumberList
    examNumberList = ranNoKaburi(min,max,num)
'''

def makeExam(min, max, numOfQue):
    """問題番号の下限, 上限、問題数でテスト問題のリスト作成(返り値なし)"""
    global examNumberList
    global examTFList
    examNumberList = ranNoKaburi(min, max ,numOfQue)
    examTFList = [0 for i in range(0, numOfQue)]

"""
def makeExamFromPart(part,numOfQue):
    #パート番号, 問題数でテスト問題のリスト作成(返り値なし)
    global examNumberList
    global examTFList
    examTFList = []
    minMax = []

    minMax = partToRange(part)
    examNumberList = ranNoKaburi(minMax[0],minMax[1],numOfQue)
"""


def getExamFourChoice(questionNumber,optMin,optMax,optNum):
    """問題番号,選択肢の問題番号範囲の下限,〃の上限,選択肢の数 -> Leap上の問題番号,解答,問題,選択肢(リスト)"""
    global examNumberList
    questionNumber -= 1
    ans = ''
    que = ''
    with open(LEAP_PATH, encoding='UTF-8') as L:
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


def getExamSpell(questionNumber):
    """問題番号 -> Leap上の問題番号,解答,問題"""
    global examNumberList
    questionNumber -= 1
    ans = ''
    que = ''
    with open(LEAP_PATH, encoding='UTF-8') as L:
        leap = list(csv.reader(L))
        ans = leap[examNumberList[questionNumber]][0]
        que = leap[examNumberList[questionNumber]][1]
    
    return examNumberList[questionNumber], ans, que


def ansExam(questionNumber, tf):
    """問題番号、その正誤"""
    #各問題の正誤を0か1かで記録する

    global examTFList

    if tf:
        examTFList[questionNumber - 1] = 1
    else:
        examTFList[questionNumber - 1] = 0

def resultExam():
    """-> 問題の正解数"""
    return sum(examTFList)