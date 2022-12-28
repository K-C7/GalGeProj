# import renpy.store as store
# import renpy.exports as renpy
import random
import csv

#定数の設定
QN_PART1 = 400
QN_PART2 = 1000
QN_PART3 = 1400
QN_PART4 = 1935

examNumberList = []

def ranNoKaburi(a, b, c):
    d = []
    while(len(d) < c):
        n = random.randint(a, b)
        if not(n in d):
            d.append(n)
    return d

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

def makeExam(min,max,num):
    # 乱数を用いた基本的(そして無駄が多い)アルゴリズムで実装
    # examNumberList = ranNoKaburi(min,max,num) <- バグるのでナシ
    return ranNoKaburi(min,max,num)

def getExam(questionNumber):
    ans = ''
    que = ''
    with open(r'C:\Users\Shiina\Desktop\Projects\Renpy\LEAPer_beta\game\module\leap.csv') as L:
        leap = csv.reader(L)
        ans = leap[examNumberList[questionNumber]][0]
        que = leap[examNumberList[questionNumber]][1]
    return questionNumber, ans, que

def ansExam(questionNumber, ans):
    # 答え合わせ、および不正解時の解答表示はできればRenpy側で実装したい
    pass

print(examNumberList)
#print(getExam(0))
print(makeExam(1,10,5))
examNumberList = makeExam(1,10,5)
print(examNumberList)