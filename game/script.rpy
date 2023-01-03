define L = Character('Leapちゃん', color="#26aa5d")
define Me = Character('自分', color="#000000")
define God = DynamicCharacter("godName",color="#adbb5d")

init:
    $ import module.leapModule as leapModule

    image bg classroom evening = im.Scale("bg classroom evening notrim.jpg", 1280, 720)

label start:

    scene bg black

    $ godName = "???"

    God "...よ ...よ"

    God "名はなんと申す?"

    $ playerName = renpy.input()

    $ godName = "神(?)"

    God "わしは全国の受験生を合格へ導く受験神じゃ!"

    jump modeSelect

label modeSelect:

    scene bg classroom evening

    show leap at center:
        zoom 1.2

    $ part = 0
    $ numOfQue = 0

    L "それでは、今日はどのPartを練習しますか？"

    menu:
        "Part1":
            Me "じゃあPart1で。"
            $ part = 1

        "Part2":
            Me "じゃあPart2で。"
            $ part = 2
        
        "Part3":
            Me "じゃあPart3で。"
            $ part = 3

        "Part4":
            Me "じゃあpart4で。"
            $ part = 4
    
    L "分かりました、Part[part]ですね。"
    L "何問ほど出したらいいでしょうか？"

    menu:
        "10問":
            Me "10問で。"
            $ numOfQue = 10

        "20問":
            Me "20問で。"
            $ numOfQue = 20

        "50問":
            Me "50問で。"
            $ numOfQue = 50

        "100問":
            Me "100問で。"
            $ numOfQue = 100

    L "了解です。それでは、Part[part]を[numOfQue]問出題するのでよろしいでしょうか。"

    menu:
        "Yes":
            L "はい、ではいきますよ。"
            call examMode(part,numOfQue)

        "No":
            L "あれ、聞き間違えたかしら..."
            jump modeSelect
    

label examMode(part,numOfQue):
    $ optNum = 3 #ここを変えると選択肢を手動で増やす必要アリ、触らないことを勧める
    $ questionNumber = 1
    $ minMax = []
    
    $ resultList = []

    $ leapModule.makeExam(part,numOfQue)
    $ minMax = leapModule.partToRange(part)

    while questionNumber <= numOfQue:
        $ exam = leapModule.getExam(questionNumber,minMax[0],minMax[1],optNum)
        $ leapNum = exam[0]
        $ ans = exam[1]
        $ que = exam[2]
        $ opt = exam[3]

        $ selected = 0

        # L "第[questionNumber]問、Leap[leapNum]番です。\n[que]は？"

        menu:
            L "第[questionNumber]問、Leap[leapNum]番です。\n[que] は？"

            "[opt[0]]":
                $ selected = 0
            "[opt[1]]":
                $ selected = 1
            "[opt[2]]":
                $ selected = 2
            "[opt[3]]":
                $ selected = 3
        
        if(opt[selected] == ans):
            $ leapModule.ansExam(True)
            L "正解です！\n{color=#26aa5d}[ans]{/color} の意味は [que] です。"
            $ resultList.append([leapNum, ans, que, 1])
        else:
            $ leapModule.ansExam(False)
            L "不正解です。\n[que] は {color=#26aa5d}[ans]{/color} です。"
            $ resultList.append([leapNum, ans, que, 0])
        
        $ questionNumber += 1
            
    $ sumT = leapModule.resultExam()

    L "結果は、[numOfQue]問中[sumT]問正解でした。"
    L "この後どうされますか？"

    menu:
        "今回の単語を復習する。":
            L "了解です。"
            "復習モードに移行します。"
            jump review
        
        "間違った単語をMy単語帳に保存する。":
            "保存中です..."
            pause 1.0
            "My単語帳に保存されました。"
            jump exit

        "同じ条件で続ける。":
            L "了解です。ではいきますよ。"
            call examMode(part,numOfQue)
            jump exit

        "条件を変えて続ける。":
            L "了解です。"
            "モード選択画面に戻ります。"
            jump modeSelect
        
        "休憩する。":
            L "了解です。今日もお疲れさまでした。"
            jump exit


label review:
    $ questionNumber = 1

    while questionNumber <= numOfQue:
        $ leapNum = resultList[questionNumber-1][0]
        $ ans = resultList[questionNumber-1][1]
        $ que = resultList[questionNumber-1][2]
        $ tf = resultList[questionNumber-1][3]

        if(tf == 1):
            L "第[questionNumber]問、Leap[leapNum]番は正解でした。\n[que] は [ans] です。"
        else:
            L "第[questionNumber]問、Leap[leapNum]番は不正解でした。\n[que] は [ans] です。"
        
        $ questionNumber += 1
    
    menu:
        "同じ条件で続ける。":
            L "了解です。ではいきますよ。"
            call examMode(part,numOfQue)
        "条件を変えて続ける。":
            L "了解です。"
            "モード選択画面に戻ります。"
            jump modeSelect
        "休憩する。":
            L "了解です。今日もお疲れさまでした。"
            jump exit
    

label exit:
    $ renpy.quit()